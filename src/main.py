from fastapi import FastAPI, HTTPException
import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(
    title="Movie Recommendation API",
    description="ML-powered REST API for movie queries and content-based recommendations.",
    version="1.1.0",
)

# ---------------------------------------------------------------------------
# Load & prepare data (runs once at startup)
# ---------------------------------------------------------------------------

movies_df = pd.read_csv('data/movies_dataset_transformed.csv')
credits_df = pd.read_csv('data/filtered_credits.csv')

# Parse dates and derive calendar columns
movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')
movies_df['release_year'] = movies_df['release_date'].dt.year
movies_df['release_month'] = movies_df['release_date'].dt.month
movies_df['day_of_week'] = movies_df['release_date'].dt.dayofweek + 1  # 1=Mon … 7=Sun

# Normalise text lookups
movies_df['title_lower'] = movies_df['title'].str.lower()
credits_df['actor_names'] = credits_df['actor_names'].apply(
    lambda x: [n.lower() for n in ast.literal_eval(x)]
)
credits_df['director_name'] = credits_df['director_name'].str.lower()

# Clean IDs and cast to int
movies_df = movies_df[movies_df['id'].apply(lambda x: str(x).isdigit())].copy()
credits_df = credits_df[credits_df['id'].apply(lambda x: str(x).isdigit())].copy()
movies_df['id'] = movies_df['id'].astype(int)
credits_df['id'] = credits_df['id'].astype(int)
movies_df.reset_index(drop=True, inplace=True)

# ---------------------------------------------------------------------------
# Pre-compute TF-IDF cosine similarity matrix for recommendations
# ---------------------------------------------------------------------------

def _build_content_string(row: pd.Series) -> str:
    """Combine genres and overview into a single string for TF-IDF."""
    genres = str(row.get('genres', '') or '')
    overview = str(row.get('overview', '') or '')
    # Weight genres more by repeating them
    return f"{genres} {genres} {overview}"

movies_df['content'] = movies_df.apply(_build_content_string, axis=1)

tfidf = TfidfVectorizer(stop_words='english', max_features=10_000)
tfidf_matrix = tfidf.fit_transform(movies_df['content'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Map title_lower -> DataFrame index for fast lookups
title_to_idx: dict[str, int] = pd.Series(
    movies_df.index, index=movies_df['title_lower']
).to_dict()

# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

MESES_ESP = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
    'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
    'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12,
}

DIAS_ESP = {
    'lunes': 1, 'martes': 2, 'miércoles': 3, 'jueves': 4,
    'viernes': 5, 'sábado': 6, 'domingo': 7,
}


@app.get("/cantidad_filmaciones_mes")
def cantidad_filmaciones_mes(mes: str):
    mes_num = MESES_ESP.get(mes.lower())
    if mes_num is None:
        raise HTTPException(status_code=400, detail=f"Mes inválido: '{mes}'")
    cantidad = int((movies_df['release_month'] == mes_num).sum())
    return {"mensaje": f"{cantidad} películas fueron estrenadas en {mes.capitalize()}"}


@app.get("/cantidad_filmaciones_dia")
def cantidad_filmaciones_dia(dia: str):
    dia_num = DIAS_ESP.get(dia.lower())
    if dia_num is None:
        raise HTTPException(status_code=400, detail=f"Día inválido: '{dia}'")
    cantidad = int((movies_df['day_of_week'] == dia_num).sum())
    return {"mensaje": f"{cantidad} películas fueron estrenadas los días {dia.capitalize()}"}


@app.get("/score_titulo")
def score_titulo(titulo_de_la_filmacion: str):
    mask = movies_df['title_lower'] == titulo_de_la_filmacion.lower()
    if not mask.any():
        raise HTTPException(status_code=404, detail="Película no encontrada")
    row = movies_df[mask].iloc[0]
    return {
        "titulo": row['title'],
        "ano": int(row['release_year']) if pd.notna(row['release_year']) else None,
        "score": row['vote_average'],
    }


@app.get("/votos_titulo")
def votos_titulo(titulo_de_la_filmacion: str):
    mask = movies_df['title_lower'] == titulo_de_la_filmacion.lower()
    if not mask.any():
        raise HTTPException(status_code=404, detail="Película no encontrada")
    row = movies_df[mask].iloc[0]
    if row['vote_count'] < 2000:
        raise HTTPException(
            status_code=400,
            detail=f"La película tiene {int(row['vote_count'])} votos (mínimo requerido: 2000)"
        )
    return {
        "titulo": row['title'],
        "ano": int(row['release_year']) if pd.notna(row['release_year']) else None,
        "cantidad_votos": int(row['vote_count']),
        "promedio_votos": row['vote_average'],
    }


@app.get("/get_actor")
def get_actor_info(nombre_actor: str):
    nombre_actor = nombre_actor.lower()
    actor_records = credits_df[credits_df['actor_names'].apply(lambda x: nombre_actor in x)]
    if actor_records.empty:
        raise HTTPException(status_code=404, detail="Actor no encontrado")

    actor_ids = actor_records['id'].tolist()
    peliculas = movies_df[movies_df['id'].isin(actor_ids)]
    total = len(peliculas)
    total_revenue = float(peliculas['return'].sum())
    promedio = total_revenue / total if total > 0 else 0.0

    return {
        "nombre_actor": nombre_actor.title(),
        "cantidad_peliculas": total,
        "retorno_total": total_revenue,
        "promedio_revenue": promedio,
    }


@app.get("/get_director")
def get_director_info(nombre_director: str):
    nombre_director = nombre_director.lower()
    director_records = credits_df[credits_df['director_name'] == nombre_director]
    if director_records.empty:
        raise HTTPException(status_code=404, detail="Director no encontrado")

    director_ids = director_records['id'].tolist()
    peliculas = movies_df[movies_df['id'].isin(director_ids)]
    total = len(peliculas)
    total_revenue = float(peliculas['return'].sum())
    promedio = total_revenue / total if total > 0 else 0.0

    return {
        "nombre_director": nombre_director.title(),
        "cantidad_peliculas": total,
        "retorno_total": total_revenue,
        "promedio_revenue": promedio,
    }


@app.get("/recomendacion")
def recomendacion(titulo: str):
    """
    Returns 5 movies similar to the given title using TF-IDF cosine similarity
    computed over genres and overview.
    """
    titulo_lower = titulo.lower()
    idx = title_to_idx.get(titulo_lower)
    if idx is None:
        raise HTTPException(status_code=404, detail="La película no se encuentra en el dataset.")

    # Get similarity scores for this movie vs all others (read-only, thread-safe)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Skip index 0 (the movie itself) and take next 5
    top_indices = [i for i, _ in sim_scores[1:6]]
    return {"recomendaciones": movies_df['title'].iloc[top_indices].tolist()}
