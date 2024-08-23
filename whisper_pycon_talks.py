import whisper, sys, os

model = whisper.load_model('medium')


for filename in os.listdir():
    if not filename.endswith('.m4a'): continue

    result = model.transcribe(filename)
    whisper.utils.get_writer('srt', '.')(result, 'filename')
    whisper.utils.get_writer('txt', '.')(result, 'filename')
