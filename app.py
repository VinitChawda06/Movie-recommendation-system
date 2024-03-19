import streamlit as st 
import pickle

movie_list = pickle.load(open('movies.pkl','rb'))
movie_list = movie_list['title'].values

option = st.selectbox(
    ' ',movie_list)