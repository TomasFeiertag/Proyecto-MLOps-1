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
8. [Contribución y Colaboración](#contribución-y-colaboración)

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
/cantidad_filmaciones_mes:

Descripción: Devuelve la cantidad de películas estrenadas en el mes especificado.
Parámetro: mes (Nombre del mes en español).
/cantidad_filmaciones_dia:

Descripción: Devuelve la cantidad de películas estrenadas en el día de la semana especificado.
Parámetro: dia (Nombre del día en español).
/score_titulo:

Descripción: Devuelve la puntuación promedio de una película dada.
Parámetro: titulo_de_la_filmacion (Título de la película).
/votos_titulo:

Descripción: Devuelve la cantidad y promedio de votos de una película, si tiene más de 2000 votos.
Parámetro: titulo_de_la_filmacion (Título de la película).
/get_actor:

Descripción: Devuelve información sobre un actor, incluyendo la cantidad de películas en las que ha participado y el retorno total y promedio de las películas.
Parámetro: nombre_actor (Nombre del actor).
/get_director:

Descripción: Devuelve información sobre un director, incluyendo una lista de películas que ha dirigido con detalles como retorno, costo y ganancia.
Parámetro: nombre_director (Nombre del director).

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
