# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python and Streamlit. It recommends similar movies based on movie features and displays movie posters using The Movie Database (TMDB) API.

## 🚀 Live Demo

**Live Application:** https://movie-recommender-system-qabw.onrender.com

> Replace `YOUR_RENDER_URL_HERE` with your actual Render URL.

## 📌 Project Overview

Finding movies based on personal interests can be challenging. This project helps users discover similar movies by selecting a movie from a dropdown menu and generating five recommendations.

The application uses text feature extraction and cosine similarity to identify movies with similar characteristics.

## ✨ Features

- Select a movie from a dropdown menu.
- Generate five similar movie recommendations.
- Content-based filtering using CountVectorizer.
- Cosine similarity for measuring movie similarity.
- Movie poster retrieval using the TMDB API.
- Interactive web interface built with Streamlit.
- Deployment on Render.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend / UI:** Streamlit
- **Data Processing:** Pandas
- **Feature Extraction:** Scikit-learn CountVectorizer
- **Similarity Measurement:** Cosine Similarity
- **API Integration:** TMDB API
- **Deployment:** Render
- **Model/Data Storage:** Pickle

## 📂 Project Structure

```text
Movie-Recommender_System/
│
├── ap.py                 # Streamlit application
├── movies.pkl            # Movie data used for similarity calculation
├── movies_dict.pkl       # Movie dataset for the application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
```

The repository may also contain a Jupyter notebook used for data exploration and model preparation.

## ⚙️ How It Works

1. **Load movie data:** The application loads the movie datasets stored in pickle files.
2. **Feature extraction:** CountVectorizer converts combined movie features into numerical vectors.
3. **Similarity calculation:** Cosine similarity measures how closely movies match.
4. **Movie selection:** The user selects a movie from the Streamlit dropdown.
5. **Recommendation generation:** The application ranks movies by similarity and selects the top five recommendations, excluding the selected movie.
6. **Poster display:** The TMDB API provides poster information for the recommended movies.

## 💻 Installation and Setup

### Prerequisites

- Python 3.11
- Git
- pip

### 1. Clone the repository

```bash
git clone https://github.com/vishva-jeet/Movie-Recommender_System.git
```

### 2. Navigate to the project folder

```bash
cd Movie-Recommender_System
```

### 3. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run ap.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 🔑 TMDB API

The application uses the TMDB API to retrieve movie poster information.

For more information, visit the [TMDB API documentation](https://developer.themoviedb.org/docs).

For security, API credentials should be stored in environment variables rather than committed to a public repository.

## ☁️ Deployment

This application is deployed using Render.

To deploy your own instance:

1. Open [Render](https://render.com/).
2. Create a new Web Service using your repository.
3. Set the build command:

   ```bash
   pip install -r requirements.txt
   ```

4. Set the start command:

   ```bash
   streamlit run ap.py --server.address 0.0.0.0 --server.port $PORT
   ```

5. Configure any required environment variables and deploy the service.

## 🎯 Learning Outcomes

- Implementing content-based recommendation systems.
- Using text vectorization and cosine similarity.
- Integrating external APIs into a Python application.
- Building interactive applications with Streamlit.
- Managing project dependencies and deploying applications.

## 👨‍💻 Author

**Vishvajeet Kumar**

- GitHub: [vishva-jeet](https://github.com/vishva-jeet)

## 📄 License

This project is available for educational and portfolio purposes. Add a license file if you intend to distribute it under a specific open-source license.
