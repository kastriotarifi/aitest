import streamlit as st
from utils.gpt2_script_gen import generate_youtube_script
from utils.text_analysis import extract_keywords, text_to_speech
from utils.video_processing import download_pixabay_video, combine_videos
from moviepy.editor import AudioFileClip

st.title("YouTube Video Generator")

prompt = st.text_input("Enter a video topic:")
if st.button("Generate Script"):
    script = generate_youtube_script(prompt)
    st.write("Generated Script:", script)

    keywords = extract_keywords(script)
    st.write("Extracted Keywords:", keywords)

    voice_file = text_to_speech(script)
    audio_clip = AudioFileClip(voice_file)
    video_clips = []
    for keyword in keywords:
        videos = download_pixabay_video(st.secrets["PIXABAY_API_KEY"], keyword)
        video_clips.extend(videos)

    combine_videos(video_clips, audio_clip, script, 'final_output_video.mp4')
    st.video('final_output_video.mp4')
