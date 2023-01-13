import os
import streamlit as st
import pytube


def download_audio(url):
    """
    This function takes in a url and attempts to download the audio from the video located at that url. It uses the pytube library to stream the audio, filter it to only include the audio stream and download it. In case of an exception such as an invalid url, video unavailability or a connection error, the function will display an error message and return None.
    Otherwise, the function returns the file name of the downloaded audio.
    """
    try:
        yt = pytube.YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()
        file_name = audio.default_filename
        
    except (pytube.exceptions.RegexMatchError, pytube.exceptions.VideoUnavailable, pytube.exceptions.LiveStreamError, ConnectionError):
        st.error("An error occurred while trying to download the audio. Please check the URL and try again.")
        return None
    
    return file_name