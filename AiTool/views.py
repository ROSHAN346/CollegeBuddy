import os
from gtts import gTTS
import speech_recognition as sr
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        tts = gTTS(text)
        tts.save('media/output.mp3')
        return render(request, 'tts.html', {'audio': 'output.mp3'})
    return render(request, 'tts.html')

def speech_to_text(request):
    text_result = ""
    if request.method == 'POST' and request.FILES.get('audio'):
        audio = request.FILES['audio']
        fs = FileSystemStorage()
        filename = fs.save(audio.name, audio)
        audio_path = fs.path(filename)

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            try:
                text_result = recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                text_result = "Could not understand audio."

    return render(request, 'stt.html', {'result': text_result})
