# Proyecto de Recomendación de Películas

## Descripción

Este proyecto se enfoca en la creación de un sistema de recomendación de películas mediante técnicas de machine learning y análisis de datos. Se ha desarrollado una API que permite recomendar películas similares basadas en la puntuación de similitud entre ellas. El objetivo es ofrecer una herramienta efectiva para sugerir películas a los usuarios en función de sus preferencias.


## Tabla de contenido

1. [Introducción](#introducción)
2. [Instalación y Requisitos](#instalación-y-requisitos)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Uso y Ejecución](#uso-y-ejecución)
5. [Datos y Fuentes](#datos-y-fuentes)
6. [Metodología](#metodología)
7. [Resultados y Conclusiones](#resultados-y-conclusiones)

## Introducción

Este proyecto implementa una API para recomendar películas similares y ofrecer información detallada sobre películas, actores y directores. La API permite realizar consultas sobre la cantidad de películas estrenadas en un mes o día específico, obtener la puntuación y el conteo de votos de una película, y buscar información relacionada con actores y directores.

## Instalación y Requisitos

### Requisitos

- Python 3.7 o superior
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- fastapi
- uvicorn

### Pasos de instalación

1. Clonar el repositorio: 
   ```bash
   git clone https://github.com/TomasFeiertag/Proyecto-MLOps-1.git
2. Crear un entorno virtual: 
   ```bash
   python -m venv venv
   ```
3. Activar el entorno virtual:
   - Windows: 
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux: 
     ```bash
     source venv/bin/activate
     ```
4. Instalar las dependencias: 
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

- `data/`: Contiene los archivos de datos utilizados en el proyecto.
- `notebooks/`: Incluye los notebooks de Jupyter con las tranformaciones solicitadas.
- `src/`: Código fuente del proyecto, incluyendo scripts y módulos. Aquí se encuentra el modelo de machine learning y la API FastAPI.
- `reports/`: Guarda los informes y visualizaciones generados.
- `README.md`: Archivo de documentación del proyecto.

## Uso y Ejecución

Para ejecutar la API, asegúrate de tener el entorno virtual activado y ejecuta el siguiente comando:

bash
uvicorn src.main:app --reload

Esto iniciará la API en http://{tu ip}. Puedes interactuar con ella a través de la interfaz de documentación automática en http://{tu ip}/docs.

La API también está desplegada en Render. Puedes acceder a la versión desplegada en el siguiente enlace:

[Visitar API en Render](https://proyecto-mlops-1-geib.onrender.com/docs)

Endpoints Disponibles
### 1. **Cantidad de Filmaciones por Mes**

**`GET /cantidad_filmaciones_mes`**

Obtiene la cantidad de películas estrenadas en un mes específico.

**Parámetro de consulta:**
- `mes` (string): Nombre del mes en español (e.g., "enero", "febrero").

**Respuesta:**
```json
{
    "mensaje": "X cantidad de películas fueron estrenadas en el mes de Mes"
}
```

### 2. **Cantidad de Filmaciones por Día de la Semana**

**`GET /cantidad_filmaciones_dia`**

Obtiene la cantidad de películas estrenadas en un día específico de la semana.

**Parámetro de consulta:**
- `dia` (string): Nombre del día en español (e.g., "lunes", "martes").

**Respuesta:**
```json
{
    "mensaje": "X cantidad de películas fueron estrenadas en los días Día"
}
```

### 3. **Puntuación de una Película**

**`GET /score_titulo`**

Obtiene la puntuación (score) de una película específica.

**Parámetro de consulta:**
- `titulo_de_la_filmacion` (string): Título de la película.

**Respuesta:**
```json
{
    "titulo": "Título de la Película",
    "ano": Año de Estreno,
    "score": Puntuación
}
```

### 4. **Votos de una Película**

**`GET /votos_titulo`**

Obtiene el número total de votos y el promedio de votos de una película específica. Solo devuelve información si la película tiene al menos 2000 votos.

**Parámetro de consulta:**
- `titulo_de_la_filmacion` (string): Título de la película.

**Respuesta:**
```json
{
    "titulo": "Título de la Película",
    "ano": Año de Estreno,
    "cantidad_votos": Número de Votos,
    "promedio_votos": Promedio de Votos
}
```

### 5. **Información del Actor**

**`GET /get_actor`**

Obtiene información sobre el número de películas en las que ha participado un actor, el retorno total y el promedio de retorno.

**Parámetro de consulta:**
- `nombre_actor` (string): Nombre del actor.

**Respuesta:**
```json
{
    "nombre_actor": "Nombre del Actor",
    "cantidad_peliculas": Número de Películas,
    "retorno_total": Retorno Total,
    "promedio_revenue": Promedio de Retorno
}
```

### 6. **Información del Director**

**`GET /get_director`**

Obtiene información sobre el número de películas dirigidas por un director, el retorno total y el promedio de retorno.

**Parámetro de consulta:**
- `nombre_director` (string): Nombre del director.

**Respuesta:**
```json
{
    "nombre_director": "Nombre del Director",
    "cantidad_peliculas": Número de Películas,
    "retorno_total": Retorno Total,
    "promedio_revenue": Promedio de Retorno
}
```

### 7. **Recomendación de Películas**

**`GET /recomendacion`**

Obtiene una lista de 5 películas similares basadas en la similitud de puntuación con una película dada.

**Parámetro de consulta:**
- `titulo` (string): Título de la película para la cual se desea obtener recomendaciones.

**Respuesta:**
```json
{
    "recomendaciones": ["Película 1", "Película 2", "Película 3", "Película 4", "Película 5"]
}
```

## Datos y Fuentes

Los datos utilizados en este proyecto provienen de los archivos `movies_dataset_transformed.csv` y `filtered_credits.csv`, que contienen información sobre películas, actores y directores. Los archivos de datos se encuentran en la carpeta `data/` en formato CSV.

## Metodología

Se realizó un análisis exploratorio de datos (EDA) para entender mejor los datos y explorar patrones. Se desarrolló un modelo de recomendación de películas basado en la similitud de puntuación. La API FastAPI se utiliza para exponer el sistema de recomendación y permitir consultas en tiempo real.

## Resultados y Conclusiones

- El sistema de recomendación proporciona una lista de 5 películas similares basadas en la similitud de puntuación.
- Se realizaron visualizaciones y análisis que ayudaron a entender mejor las relaciones y patrones en los datos de películas.
- La API funciona correctamente y está disponible para consultas.

### Autores

Este proyecto fue realizado por: [Tomas Feiertag].
