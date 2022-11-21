import pickle
import streamlit as st
import requests
import pandas as pd


def fetch_poster(video_code):
    url = "https://www.googleapis.com/youtube/v3/videos?id={}&key=AIzaSyB1bIXzkTxscjs1rnX_WScPm3njJKgla0w&part=snippet,contentDetails,statistics,status".format(video_code)
    data = requests.get(url)
    data = data.json()
    # poster_path = data['thumbnail']
    full_path = "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(video_code)
    return full_path


def recommend(video):
    video_index = videos_pkl[videos_pkl['title'] == video].index[0]
    distances = sorted(list(enumerate(similarity[video_index])), reverse=True, key=lambda x: x[1])
    recommended_video_names = []
    recommended_video_posters = []

    for i in distances[1:6]:
        video_code = videos_pkl.iloc[i[0]].Video_code
        recommended_video_posters.append(fetch_poster(video_code))
        recommended_video_names.append(videos_pkl.iloc[i[0]].title)
    return recommended_video_names, recommended_video_posters


videos_pkl = pickle.load(open(r'C:\Users\Soham\Dropbox\My PC (LAPTOP-AGG4JAFB)\Desktop\MyCode\College Projects\ML PROJECT\video_list.pkl', 'rb'))

similarity = pickle.load(open(r'C:\Users\Soham\Dropbox\My PC (LAPTOP-AGG4JAFB)\Desktop\MyCode\College Projects\ML PROJECT\similarity.pkl', 'rb'))

st.title('TED TALK RECOMMENDATION SYSTEM')
selected_video_name = st.selectbox(
    'Which type of videos would you like to watch',
    videos_pkl['title'].values
)

if st.button('Show me my Recommendations!'):
    recommended_video_names, recommended_video_posters = recommend(selected_video_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.caption(recommended_video_names[0])
        st.image(recommended_video_posters[0], width = 120)
    with col2:
        st.caption(recommended_video_names[1])
        st.image(recommended_video_posters[1], width = 120)

    with col3:
        st.caption(recommended_video_names[2])
        st.image(recommended_video_posters[2], width = 120)
    with col4:
        st.caption(recommended_video_names[3])
        st.image(recommended_video_posters[3], width = 120)
    with col5:
        st.caption(recommended_video_names[4])
        st.image(recommended_video_posters[4], width = 120)