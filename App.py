import streamlit as st

st.write("Movie Streaming App🎥🍿")
movie_path = st.text_input('Movie Path', 'C:/examle.mp4')
video_file = open(movie_path, 'rb')
video_bytes = video_file.read()
if video_bytes:
    st.video(video_bytes)