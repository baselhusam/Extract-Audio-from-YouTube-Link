from pytube import YouTube
import streamlit as st
from tube_dl import Youtube
from pytube import YouTube
import time


st.markdown("# <div align=center> Extract Audio from YouTube Video </div> <br> ", unsafe_allow_html=True)
st.markdown("##### <div align=center> Paste the link of the youtube video below to download the audio <hr></div>", unsafe_allow_html=True)


st.markdown(" ### <div align=center> The URL link </div> ", unsafe_allow_html=True)
link = st.text_input('', placeholder = "Enter the Video Link Here!")
st.markdown("<div></div>", unsafe_allow_html=True)
    
if link:
    

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
        
    my_bar.empty()

    yt = YouTube(link)
    audio = yt.streams.filter(only_audio = True).get_audio_only()
    stream = yt.streams.get_by_itag(140)
    
    col1, col2, col3 = st.columns([1,0.5,1])
    
    
    with col2:
        button = st.button("Download Now")
        if button:
            stream.download()
    if button:   
        st.success("Download Completed! 😊")
        st.balloons()
                   