import os
import sys
from pytube import YouTube
import subprocess
from urllib.parse import urlparse, parse_qs

def download_youtube_video(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path='.')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file

def transcribe_file(file_path, file_name):
    print(f"Transcribing file: {file_path}")
    result = subprocess.run(['whisper', file_path, '--output_format', 'txt', '--output_dir', '.'])
    print(f"Transcription output: {result.stdout}")
    txt_file = f'{os.path.splitext(file_path)[0]}.txt'
    if os.path.exists(txt_file):
        os.rename(txt_file, f'{file_name}.txt')
    else:
        print(f"Expected transcription file not found: {txt_file}")

def get_youtube_id(url): 
    parsed_url = urlparse(url)
    if 'youtube.com' in parsed_url.netloc:
        query = parse_qs(parsed_url.query)
        return query['v'][0] if 'v' in query else None
    elif 'youtu.be' in parsed_url.netloc:
        return parsed_url.path[1:]
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <YouTube URL or file path>")
        sys.exit(1)

    input_path = sys.argv[1]

    if "youtube.com" in input_path or "youtu.be" in input_path:
        youtube_id = get_youtube_id(input_path)
        if youtube_id is None:
            print("Invalid YouTube URL")
            sys.exit(1)
        audio_file_path = download_youtube_video(input_path)
        if not audio_file_path:
            print("Failed to download the video.")
            sys.exit(1)
        file_name = youtube_id
    else:
        audio_file_path = input_path
        file_name = os.path.splitext(os.path.basename(input_path))[0]

    if not os.path.exists(audio_file_path):
        print(f"Audio file does not exist: {audio_file_path}")
        sys.exit(1)

    transcribe_file(audio_file_path, file_name)

    print(f"Transcription saved to {file_name}.txt")

if __name__ == "__main__":
    main()
