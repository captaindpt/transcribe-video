# transcribe-video

This project provides a script to download and transcribe audio from YouTube videos. It uses the `pytube` library to download audio and the `whisper` library to transcribe the audio to text.

## Features

- **Download YouTube Audio**: Download audio from YouTube videos as MP3 files.
- **Transcription**: Transcribe the downloaded audio files to text using the `whisper` library.
- **Support for Different YouTube URL Formats**: Handles both standard and short YouTube URLs.

## Requirements

- Python 3.8+
- `virtualenv` (for creating isolated Python environments)
- `pytube` (for downloading YouTube videos)
- `whisper` (for audio transcription)
- `ffmpeg` (for processing audio files)

## Setup

### Step 1: Install `virtualenv`

If you don't have `virtualenv` installed, you can install it using `brew` or `apt`:
```bash
brew install virtualenv
```

### Step 2: Create a Virtual Environment

Navigate to your project directory and create a virtual environment:
```bash
cd ~/ccode
virtualenv venv
```

### Step 3: Activate the Virtual Environment

Activate the virtual environment:
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

With the virtual environment activated, install the required Python packages:
```bash
pip install pytube
pip install whisper
```

Make sure you have `ffmpeg` installed. You can install it using `brew`:
```bash
brew install ffmpeg
```

## Usage

### Download and Transcribe YouTube Video

To download and transcribe a YouTube video, run the following command:
```bash
python transcribe.py <YouTube URL or file path>
```

### Example

```bash
python transcribe.py https://youtu.be/A8uQqfu69GU?si=hLlP_g5l23URZj_d
```

### Script Details

The script performs the following steps:
1. Parses the YouTube URL to extract the video ID.
2. Downloads the audio from the YouTube video as an MP3 file.
3. Uses the `whisper` library to transcribe the audio file to text.
4. Saves the transcribed text to a file named `<video_id>.txt`.

### Output

The final transcribed text is saved to a file and printed to the console.
