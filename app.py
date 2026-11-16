import streamlit as st
import pickle 
import joblib

st.title("Movie Recommendation System")

with open("movies.pickle", "rb") as m:
    movies = pickle.load(m)

similarity = joblib.load("simlarity.joblib")
movie_titles = movies["title"].values  

name_movies = st.selectbox("Enter The Movie Name", movie_titles)


def recommend(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]
    recommendations = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(recommendations)),
        reverse=True,
        key=lambda x: x[1]
    )[1:10]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies          
    
    
if st.button("Recommend"):
    st.write("The Recommended Movies are :")
    r = recommend(name_movies)
    for i in r:
        st.write(i)
