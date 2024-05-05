import speech_recognition
import pyttsx3

def SpeakNow(command):
    voice = pyttsx3.init()
    voice.say(command)
    voice.runAndWait()

sr = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source2:
    print("Silence Please")
    sr.adjust_for_ambient_noise(source2, duration=2)
    print("Speak Now Please")
    audio2 = sr.listen(source2)
    text = sr.recognize_google(audio2)
    text=text.lower()
    
    print("Did you say : --"+text)
    
    SpeakNow(text)