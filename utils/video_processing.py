import os
import requests
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, TextClip, CompositeVideoClip

def download_pixabay_video(api_key, search_query, max_videos=3):
    url = f"https://pixabay.com/api/videos/?key={api_key}&q={search_query}"
    response = requests.get(url)
    videos = []
    if response.status_code == 200:
        for video in response.json()['hits'][:max_videos]:
            video_url = video['videos']['large']['url']
            video_path = f"downloaded_videos/video_{video['id']}.mp4"
            if not os.path.exists(video_path):
                os.makedirs('downloaded_videos', exist_ok=True)
                with open(video_path, 'wb') as f:
                    f.write(requests.get(video_url).content)
                videos.append(video_path)
    return videos

def combine_videos(video_clips, voice_clip, script, output_filename='combined_video.mp4'):
    final_video = concatenate_videoclips([VideoFileClip(clip) for clip in video_clips])
    audio_clip = AudioFileClip(voice_clip)
    final_video = final_video.set_audio(audio_clip)
    final_video.write_videofile(output_filename, codec='libx264', fps=24)
