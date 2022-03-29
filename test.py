#IMPORTS
import pickle
import streamlit as st
import pandas as pd

movies = pickle.load(open("movies.pkl",'rb'))
corrMatrix = pickle.load(open('corrmatrix.pkl','rb'))

st.image('movie.jpg',width=300)
st.title('Movie Recommender')

movie_list = movies['title']
selected_movie = st.selectbox("select a movie from the dropdown", options=movie_list)

rating = st.slider('Choose a rating', 1, 5)
col1, col2,= st.columns([1,2])
with col1:
    st.empty()
with col2:
    if rating==1:
        st.markdown("⭐")
    if rating==2:
        st.markdown("⭐⭐")
    if rating==3:
        st.markdown("⭐⭐⭐")
    if rating==4:
        st.markdown("⭐⭐⭐⭐")
    if rating==5:
        st.markdown("⭐⭐⭐⭐⭐⭐")

index = movie_list[movie_list == selected_movie].index[0]
movie_name = movies.iloc[index]['title']


def get_similar(movie_name, rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    return similar_ratings.index


movie_poster = pd.read_csv('movie_poster.csv',names=['id','url'])
movie_url = pd.read_csv('movie_url.csv')

if st.button('Show Recommendation'):
    similar_movies = get_similar(movie_name,rating)
    similar_movies = similar_movies[1:]
#################################################################
    idx = 0
    cols = st.columns(4)

    if idx < 4:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[0].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1

    if idx < 4:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[1].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1

    if idx < 4:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[2].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1

    if idx < 4:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[3].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1
#####################################################################
    idx = 5
    # for _ in range(4):
    cols = st.columns(4)

    if idx < 9:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[0].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1

    if idx < 9:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[1].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1

    if idx < 9:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[2].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1

    if idx < 9:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[3].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1
######################################################################
    idx = 9
    # for _ in range(4):
    cols = st.columns(4)

    if idx < 13:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[0].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1

    if idx < 13:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[1].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1

    if idx < 13:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[2].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1

    if idx < 13:
        id = movies[movies['title'] == similar_movies[idx]].index[0]
        pos_url = movies.iloc[id]['poster_url']
        cols[3].image(pos_url, width=150, caption=similar_movies[idx])
    idx+=1


st.subheader('by hrishikesh jadhav', anchor=None)