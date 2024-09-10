"""Downloads all videos for a PyCon event from YouTube and extracts the audio.
The transcription by Whisper is a separate step after this script."""

import json, yt_dlp, os, re, sys
from pathlib import Path

PYCON_EVENTS = sys.argv[1:]


def sanitize_filename(filename: str) -> str:
    filename = filename.replace(' ', '-')
    sanitized_filename = re.sub(r'[<>:"/\\|?*\']', '_', filename)
    return sanitized_filename.strip()
    
def download_files_for_event(pycon_event):
    event_path = Path(__file__).parent / f'data/{pycon_event}/videos'
    for json_filename in os.listdir(event_path):
        if not json_filename.endswith('.json'): continue  # skip non-json files

        # Get video URLs from pyvideo data folder:
        with open(event_path / json_filename) as event_file:
            event_data = json.loads(event_file.read())

        event_url = event_data['videos'][0]['url']
        event_title = sanitize_filename(event_data['title'])

        ytdlp_options = {
            'quiet': True,
            'no_warnings': True,
            'no_progress': False,
            #'format': 'm4a/bestaudio/best',
            'outtmpl': event_title + '.%(ext)s',
            #'postprocessors': [{  # Extract audio using ffmpeg
            #    'key': 'FFmpegExtractAudio',
            #    'preferredcodec': 'm4a',
            #}]
        }

        # Make the folders for this event:
        os.chdir(Path(__file__).parent / 'events')
        os.makedirs(pycon_event, exist_ok=True)
        os.chdir(pycon_event)
        os.makedirs('originals', exist_ok=True)
        os.makedirs('human-reviewer-notes', exist_ok=True)
        os.chdir('originals')  # Videos will go in the "originals" folder.

        # Download the video and extract the audio to a .m4a file:
        print(f'Downloading {event_title}...')
        try:
            with yt_dlp.YoutubeDL(ytdlp_options) as ydl:
                error_code = ydl.download([event_url])
        except Exception as e:
            print(f'ERROR: {e}')

    print('Creating blank human review notes...')
    for filename in os.listdir(Path(__file__).parent / f'events/{pycon_event}/originals'):
        if not filename.endswith('.srt'): continue

        # Create a blank file for the human review notes if it doesn't already exist:
        notes_filename = Path(__file__).parent / f'events/{pycon_event}/human-reviewer-notes/{filename[:-4]}.txt'
        if notes_filename.exists(): continue
        with open(notes_filename, 'w') as fp:
            pass  # Just create a blank file.
        print(notes_filename, 'created.')




for event in PYCON_EVENTS:
    download_files_for_event(event)
    