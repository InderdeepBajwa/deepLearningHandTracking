import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile("vid1.MP4")

with harvard as source:
    audio = r.record(source)

r.recognize_google(audio)

    