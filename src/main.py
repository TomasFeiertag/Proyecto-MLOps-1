from fastapi import FastAPI, HTTPException
import pandas as pd
from datetime import datetime
import ast

app = FastAPI()

# Cargar los datasets
movies_df = pd.read_csv('data/movies_dataset_transformed.csv')
credits_df = pd.read_csv('data/filtered_credits.csv')

# Asegurarse de que las fechas están en el formato adecuado
movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')
movies_df['release_year'] = movies_df['release_date'].dt.year
movies_df['release_month'] = movies_df['release_date'].dt.month
movies_df['release_day'] = movies_df['release_date'].dt.day

@app.get("/cantidad_filmaciones_mes")
def cantidad_filmaciones_mes(mes: str):
    meses_esp = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5,
        'junio': 6, 'julio': 7, 'agosto': 8, 'septiembre': 9,
        'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    mes_num = meses_esp.get(mes.lower())
    if mes_num is None:
        raise HTTPException(status_code=400, detail="Mes inválido")
    
    cantidad = movies_df[movies_df['release_month'] == mes_num].shape[0]
    return {"mensaje": f"{cantidad} cantidad de películas fueron estrenadas en el mes de {mes}"}

@app.get("/cantidad_filmaciones_dia")
def cantidad_filmaciones_dia(dia: str):
    dias_esp = {
        'lunes': 1, 'martes': 2, 'miércoles': 3, 'jueves': 4, 'viernes': 5,
        'sábado': 6, 'domingo': 7
    }
    dia_num = dias_esp.get(dia.lower())
    if dia_num is None:
        raise HTTPException(status_code=400, detail="Día inválido")
    
    # Convertir a números de semana: 1 (lunes) a 7 (domingo)
    movies_df['day_of_week'] = movies_df['release_date'].dt.dayofweek + 1
    cantidad = movies_df[movies_df['day_of_week'] == dia_num].shape[0]
    return {"mensaje": f"{cantidad} cantidad de películas fueron estrenadas en los días {dia}"}

@app.get("/score_titulo")
def score_titulo(titulo_de_la_filmacion: str):
    pelicula = movies_df[movies_df['title'].str.lower() == titulo_de_la_filmacion.lower()]
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    pelicula_info = pelicula.iloc[0]
    return {
        "titulo": pelicula_info['title'],
        "ano": pelicula_info['release_year'],
        "score": pelicula_info['vote_average']
    }

@app.get("/votos_titulo")
def votos_titulo(titulo_de_la_filmacion: str):
    pelicula = movies_df[movies_df['title'].str.lower() == titulo_de_la_filmacion.lower()]
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    pelicula_info = pelicula.iloc[0]
    if pelicula_info['vote_count'] < 2000:
        raise HTTPException(status_code=400, detail="La película no cumple con el requisito de votos")
    
    return {
        "titulo": pelicula_info['title'],
        "ano": pelicula_info['release_year'],
        "cantidad_votos": pelicula_info['vote_count'],
        "promedio_votos": pelicula_info['vote_average']
    }

@app.get("/get_actor")
def get_actor_info(nombre_actor: str):
    # Buscar los ids en los que el actor está presente
    actor_records = credits_df[credits_df['actor_names'].apply(lambda x: nombre_actor in ast.literal_eval(x))]
    
    if actor_records.empty:
        return {"mensaje": "Actor no encontrado"}

    # Obtener los ids de las películas en las que el actor ha participado
    actor_ids = actor_records['id'].tolist()

    # Buscar las películas en las que el actor ha participado
    peliculas = movies_df[movies_df['id'].isin(actor_ids)]

    # Calcular los datos requeridos
    total_peliculas = len(peliculas)
    total_revenue = peliculas['return'].sum()
    promedio_revenue = total_revenue / total_peliculas if total_peliculas > 0 else 0

    return {
        "nombre_actor": nombre_actor,
        "cantidad_peliculas": total_peliculas,
        "retorno_total": total_revenue,
        "promedio_revenue": promedio_revenue
    }
@app.get("/get_director")
def get_director_info(nombre_director: str):
    # Buscar los IDs en los que el director está presente
    director_records = credits_df[credits_df['director_name'] == nombre_director]
    
    if director_records.empty:
        return {"mensaje": "Director no encontrado"}

    # Obtener los IDs de las películas en las que el director ha trabajado
    director_ids = director_records['id'].tolist()

    # Buscar las películas en las que el director ha trabajado
    peliculas = movies_df[movies_df['id'].isin(director_ids)]

    # Calcular los datos requeridos
    total_peliculas = len(peliculas)
    total_revenue = peliculas['return'].sum()
    promedio_revenue = total_revenue / total_peliculas if total_peliculas > 0 else 0

    return {
        "nombre_director": nombre_director,
        "cantidad_peliculas": total_peliculas,
        "retorno_total": total_revenue,
        "promedio_revenue": promedio_revenue
    }