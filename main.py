import streamlit as st
from pytube import YouTube
import time

# Title of the App
st.markdown("# <div align=center> Extract Audio from YouTube Video </div> <br> ", unsafe_allow_html=True)

# Subtitle
st.markdown("##### <div align=center> Paste the link of the youtube video below to download the audio <hr></div>", unsafe_allow_html=True)

# Get the link of the video
st.markdown(" ### <div align=center> The URL link </div> ", unsafe_allow_html=True)
link = st.text_input('', placeholder = "Enter the Video Link Here!")
st.markdown("<div></div>", unsafe_allow_html=True)


# Check if the link is not empty
if link:
    
    # Create a progress bar
    my_bar = st.progress(0)

    # Loop to simulate the progress
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
        
    my_bar.empty()
    
    # Get the audio of the video
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio = True).get_audio_only()
    stream = yt.streams.get_by_itag(140)
  
    # Create a column for the button    
    col1, col2, col3 = st.columns([1,0.5,1])
    
    # Add the download button
    with col2:
        button = st.button("Download Now")
        if button:
            stream.download()
            
    # Show success message after download
    if button:   
        st.success("Download Completed! 😊")
        st.balloons()
                   
