from pytube import YouTube, Search
from moviepy.editor import AudioFileClip
import os

# Read the song names from the file
with open('output.txt', 'r', encoding='utf-8') as f:
    song_names = [line.strip() for line in f]

# Directory to save the songs
output_dir = 'C:\\Users\\jb781\\Downloads\\SONGS'

# Search for each song on YouTube and download the first result as an MP3
for song_name in song_names:
    results = Search(song_name).results
    if results:
        print(f"Downloading first result for '{song_name}'...")
        video = results[0]
        stream = video.streams.filter(only_audio=True).first()
        output_file = stream.download(output_dir)
        mp3_file = output_file.replace(".mp4", ".mp3")
        audio = AudioFileClip(output_file)
        audio.write_audiofile(mp3_file)
        os.remove(output_file)
        print(f"Downloaded and converted to MP3: {mp3_file}")
