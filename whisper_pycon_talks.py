import whisper, sys, os, shutil
from pathlib import Path

model = whisper.load_model('medium')

PYCON_EVENTS = sys.argv[1:]


def run_whisper_for_event(pycon_event):
    os.chdir(Path(__file__).parent / f'events/{pycon_event}/originals')

    for filename in os.listdir():
        if not filename.endswith('.m4a'): continue

        if os.path.exists(filename[:-4] + '.srt'):
            print(f'Skipping {filename} because it has already been transcribed.')

        print(f'Transcribing {filename}...')
        result = model.transcribe(filename)
        whisper.utils.get_writer('srt', '.')(result, filename[:-4] + '.srt')

    

for event in PYCON_EVENTS:
    run_whisper_for_event(event)
    