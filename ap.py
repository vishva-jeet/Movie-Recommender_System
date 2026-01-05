import streamlit as st
import pickle
import pandas as pd
import requests

import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pickle.load(open("movies.pkl", "rb"))
@st.cache_data
def compute_similarity(movies_df):
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(movies_df["combined_features"]).toarray()
    similarity = cosine_similarity(vectors)
    return similarity

similarity = compute_similarity(movies)



#data load
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


st.title('Movie Recommendation System')

#poster
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=17ca36a3e45b2e160c822f0a467c90f2&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

#recommended movie function:
def recommend_movie(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    list_of_movies = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    #adding poster of movies from API
    recommended_movies_posters = []

    for i in list_of_movies:
        movie_id = i[0]
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters


#select box
selected_movies = st.selectbox(
    'Select Movies:',
    movies['title'].values
)

# Recommendation Button:
if st.button('Recommend Movies'):
    names,posters = recommend_movie(selected_movies)


    col1, col2, col3 ,col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
         st.text(names[2])
         st.image(posters[2])


    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
         st.text(names[4])
         st.image(posters[4])
