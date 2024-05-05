# import tkinter as tk
# from tkinter import *
# from tkinter import filedialog
# from tkinter.ttk import Combobox
# import pyttsx3
# import os
# from gtts import gTTS
# from playsound import playsound


# root = tk.Tk()  # Create an instance of the Tk class
# root.title("Text to Speech Converter")  # Note the correct spelling of 'title'
# root.geometry("1000x580+200+80")
# # root.resizable(True,True) to resize it
# root.resizable(False,False)
# root.configure(bg="#F7AC40")
# # root.mainloop()

# # simpli_logo = PhotoImage(file="C:/Users/jishn/Desktop/MachineL/TexttoSpeech/img2.jpg")
# # Label(root,image=simpli_logo,bg="#F7AC40").place(x=880,y=539)
# # root.mainloop()

# logo_image = PhotoImage(file= "C:/Users/jishn/Desktop/MachineL/TexttoSpeech/pic1.png")
# root.iconphoto(False,logo_image)
# # root.mainloop()

# upper_frame =Frame(root,bg="#14A7DD",width=1200,height=130)
# upper_frame.place(x=0,y=0)

# picture = PhotoImage(file="C:/Users/jishn/Desktop/MachineL/TexttoSpeech/pic2.png",width=90,height=90)
# Label(upper_frame,image=picture,bg="#14A7DD").place(x=150,y=20)
# # root.mainloop()

# Label(upper_frame,text="Text to Speech Converter", font="TimesNewroman 40 bold" ,bg="#14A7DD", fg='white').place(x=250, y=35)
# # root.mainloop()

# text_box = Text(root,font="callbri 20", bg="white",relief=GROOVE,wrap=WORD, bd=0)
# text_box.place(x=30,y=150, width=950,height=180)
# # root.mainloop()

# genderbox=Combobox(root,values=["Male","Female"],font="calibri 14",state="r",width=10)
# genderbox.place(x=30,y=350)
# genderbox.set("Select Gender")
# # root.mainloop()

# Speedbox=Combobox(root,values=["Fast","Medium","Slow"],font="calibri 14",state="r",width=10)
# Speedbox.place(x=30,y=440)
# Speedbox.set("Speed")
# # root.mainloop()

# tts =pyttsx3.init()
# def speaknow():
#     text=text_box.get(1.0,END)
#     gender=genderbox.get()
#     speed=Speedbox.get()
#     voices=tts.getProperty('voices')
    
#     def setvoice():
#         if(gender == 'Male'):
#             tts.setProperty('voice',voices[0].id)
#             tts.say(text)
#             tts.runAndWait()
#         else:
#             tts.setProperty('voice',voices[1].id)
#             tts.say(text)
#             tts.runAndWait()
#     if(text):
#         if(speed=='Fast'):
#             tts.setProperty('rate',250)
#             setvoice()
#         elif(speed == 'Medium'):
#             tts.setProperty('rate',150)
#             setvoice()
#         else:
#             tts.setProperty('rate',60)
#             setvoice()                    

# play_button=PhotoImage(file="C:/Users/jishn/Desktop/MachineL/TexttoSpeech/play2.png")
# play_btn=Button(root,text="Play",compound=LEFT,image=play_button,bg='white',height=100,width=130,font="arial 14 bold",borderwidth='0.1c',command=speaknow)
# play_btn.place(x=435,y=400)
# root.mainloop()


import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3

def speak_now():
    text = text_box.get(1.0, END)
    gender = gender_box.get()
    speed = speed_box.get()
    voices = tts.getProperty('voices')

    def set_voice():
        if gender == 'Male':
            tts.setProperty('voice', voices[0].id)
            tts.say(text)
            tts.runAndWait()
        else:
            tts.setProperty('voice', voices[1].id)
            tts.say(text)
            tts.runAndWait()

    if text:
        if speed == 'Fast':
            tts.setProperty('rate', 250)
            set_voice()
        elif speed == 'Medium':
            tts.setProperty('rate', 150)
            set_voice()
        else:
            tts.setProperty('rate', 60)
            set_voice()

root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("1000x580+200+80")
root.resizable(False, False)
root.configure(bg="#F7AC40")

# Upper frame
upper_frame = Frame(root, bg="#14A7DD", width=1000, height=130)
upper_frame.pack(side=TOP, fill=X)

logo_image = PhotoImage(file="pic1.png")
root.iconphoto(False, logo_image)

picture = PhotoImage(file="pic2.png").subsample(2)
Label(upper_frame, image=picture, bg="#14A7DD").place(x=50, y=20)

Label(upper_frame, text="Text to Speech Converter", font="Arial 32 bold", bg="#14A7DD", fg='white').place(x=200, y=35)

# Text box
text_box = Text(root, font="Arial 16", bg="white", relief=GROOVE, wrap=WORD, bd=0)
text_box.place(x=30, y=150, width=940, height=200)

# Gender combobox
gender_box = Combobox(root, values=["Male", "Female"], font="Arial 14", state="readonly")
gender_box.place(x=30, y=370)
gender_box.set("Select Gender")

# Speed combobox
speed_box = Combobox(root, values=["Fast", "Medium", "Slow"], font="Arial 14", state="readonly")
speed_box.place(x=30, y=440)
speed_box.set("Speed")

# Initialize Text-to-Speech engine
tts = pyttsx3.init()

# Play button
play_button = PhotoImage(file="play2.png").subsample(2)
play_btn = Button(root, text="Play", compound=LEFT, image=play_button, bg='#FFFFFF', height=80, width=100,
                  font="Arial 14 bold", borderwidth='0.1c', command=speak_now)
play_btn.place(x=450, y=400)

root.mainloop()

