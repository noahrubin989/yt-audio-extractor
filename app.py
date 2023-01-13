# === YouTube video audio extractor ===
import streamlit as st
import utils
   
st.markdown("""
            # YouTube Video Audio Extractor
            
            ### Created By: Noah Rubin
            📊 [LinkedIn](https://www.linkedin.com/in/noah-rubin1/)  
            
            🧑🏽‍💻 [GitHub](https://github.com/noahrubin989)
            """)

url = st.text_input(label='Enter the URL of your favourite YouTube video')
if url: 
    file_name = utils.download_audio(url)
    if file_name:
        with open(file_name, 'rb') as f:
            st.download_button(label='Download Audio', data=f, file_name=file_name, mime='audio/mpeg')    