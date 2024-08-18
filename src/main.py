import pandas as pd
from fastapi import FastAPI

# Cargar los datasets correctos
movies_df = pd.read_csv('movies_dataset_transformed.csv')
credits_df = pd.read_csv('filtered_credits.csv')

# Convertir 'release_date' a datetime
movies_df['release_date'] = pd.to_datetime(movies_df['release_date'])

app = FastAPI()

@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    mes = mes.lower()
    movies_df['mes'] = movies_df['release_date'].dt.strftime('%B').str.lower()
    cantidad = movies_df[movies_df['mes'] == mes].shape[0]
    return f"{cantidad} películas fueron estrenadas en el mes de {mes.capitalize()}."

@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
    dia = dia.lower()
    movies_df['dia'] = movies_df['release_date'].dt.strftime('%A').str.lower()
    cantidad = movies_df[movies_df['dia'] == dia].shape[0]
    return f"{cantidad} películas fueron estrenadas en los días {dia.capitalize()}."

@app.get("/score_titulo/{titulo}")
def score_titulo(titulo: str):
    pelicula = movies_df[movies_df['title'].str.contains(titulo, case=False, na=False)]
    if pelicula.empty:
        return "Película no encontrada"
    pelicula = pelicula.iloc[0]
    return f"La película {pelicula['title']} fue estrenada en el año {pelicula['release_year']} con un score/popularidad de {pelicula['popularity']}."

@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo: str):
    pelicula = movies_df[movies_df['title'].str.contains(titulo, case=False, na=False)]
    if pelicula.empty:
        return "Película no encontrada"
    pelicula = pelicula.iloc[0]
    if pelicula['vote_count'] < 2000:
        return "La película no tiene suficientes valoraciones (menos de 2000)."
    return f"La película {pelicula['title']} fue estrenada en el año {pelicula['release_year']}. Tiene un total de {pelicula['vote_count']} valoraciones, con un promedio de {pelicula['vote_average']}."

@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    actor_data = credits_df[credits_df['actor_names'].apply(lambda x: nombre_actor in eval(x))]
    if actor_data.empty:
        return "Actor no encontrado."
    peliculas = actor_data.merge(movies_df, on='id')[['title', 'return']]
    cantidad_peliculas = peliculas.shape[0]
    retorno_total = peliculas['return'].sum()
    promedio_retorno = peliculas['return'].mean()
    return (f"El actor {nombre_actor} ha participado en {cantidad_peliculas} películas, "
            f"con un retorno total de {retorno_total} y un promedio de retorno de {promedio_retorno} por película.")

@app.get("/get_director/{nombre_director}")
def get_director(nombre_director: str):
    director_data = credits_df[credits_df['director_name'] == nombre_director]
    if director_data.empty:
        return "Director no encontrado."
    peliculas = director_data.merge(movies_df, on='id')[['title', 'release_date', 'return', 'budget', 'revenue']]
    peliculas['release_date'] = pd.to_datetime(peliculas['release_date']).dt.strftime('%Y-%m-%d')
    return peliculas.to_dict(orient='records')
