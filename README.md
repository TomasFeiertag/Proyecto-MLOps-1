<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:009688,100:0d1117&height=180&section=header&text=Movie%20Recommendation%20API&fontSize=40&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=ML-powered%20REST%20API%20%7C%20FastAPI%20%2B%20Scikit-learn%20%7C%20Deployed%20on%20Render&descAlignY=60&descSize=17&descColor=a8f0e8" />

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)

</div>

<div align="center">

🚀 **[Live API on Render →](https://proyecto-mlops-1-geib.onrender.com/docs)**

</div>

---

## 📌 Overview

End-to-end MLOps project: from raw data to a **deployed REST API** that recommends similar movies using a cosine similarity model. Includes full ETL pipeline, EDA, ML model, and a production-ready FastAPI service.

---

## 🔄 Pipeline

```
Raw CSV Data ──► ETL (Pandas) ──► EDA ──► Cosine Similarity Model ──► FastAPI ──► Render Deploy
```

---

## 🛠️ API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/cantidad_filmaciones_mes` | Number of films released in a given month |
| `GET` | `/cantidad_filmaciones_dia` | Number of films released on a given weekday |
| `GET` | `/score_titulo` | Score/rating of a specific film |
| `GET` | `/votos_titulo` | Vote count & average (min 2000 votes required) |
| `GET` | `/get_actor` | Actor filmography, total & average revenue |
| `GET` | `/get_director` | Director filmography, total & average revenue |
| `GET` | `/recomendacion` | **5 similar movies** based on score similarity |

### Example — Movie Recommendation

**Request:**
```
GET /recomendacion?titulo=Toy Story
```

**Response:**
```json
{
  "recomendaciones": ["A Bug's Life", "Monsters, Inc.", "Finding Nemo", "Up", "WALL·E"]
}
```

---

## ⚒️ Tech Stack

| Layer | Tools |
|---|---|
| **Processing** | Python, Pandas, NumPy |
| **ML Model** | Scikit-learn (cosine similarity) |
| **API** | FastAPI, Uvicorn |
| **Analysis** | Matplotlib, Seaborn, Jupyter |
| **Deploy** | Render |

---

## ▶️ Run Locally

**1. Clone & install**
```bash
git clone https://github.com/TomasFeiertag/Proyecto-MLOps-1.git
cd Proyecto-MLOps-1
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**2. Start the API**
```bash
uvicorn src.main:app --reload
```

**3. Open the interactive docs**
```
http://localhost:8000/docs
```

---

## 📁 Project Structure

```
├── data/           # Raw and transformed CSV datasets
├── notebooks/      # EDA and transformation notebooks
├── src/            # FastAPI app + ML model
├── reports/        # Visualizations and analysis outputs
└── README.md
```

---

## 👤 Author

**Tomás Feiertag** — Data Scientist · NLP & LLMs @ Movistar

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/tfeiertag/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/TomasFeiertag)

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,100:009688&height=100&section=footer" />
