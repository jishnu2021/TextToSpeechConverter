import speech_recognition
import pyttsx3
import webbrowser

if __name__ =="__main__":
    path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    
    sr = speech_recognition.Recognizer()
    
    with speech_recognition.Microphone() as m:
        print("Speak Anything :")
        sr.adjust_for_ambient_noise(m)
        print("Please say something to open......")
        audio=sr.listen(m)
        
        print("Hearing....")
        try:
            dest = sr.recognize_google(audio)
            print("You asked to open :"+dest)
            
            webbrowser.get(path).open(dest)
            
        except Exception as e:
            print("error",str(e))    