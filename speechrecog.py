import whisper

model = whisper.load_model('base')
result = model.transcribe('audio.wav')
result['text']

#pip install git+https://github.com/openai/whisper.git
