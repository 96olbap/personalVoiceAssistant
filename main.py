import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import pyquark
import tkinter as tk

from time import strftime
from tkinter import *
from PIL import Image, ImageTk, ImageSequence

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def CommandsList():
    '''show the command to which voice assistant is registered with'''
    pyquark.filestart('')

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, phrase_time_limit= 6, timeout= 3600)
            command = 'waiting'
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mac' in command:
                command = command.replace('mac', '')
                print(command)
    except:
        pass
    return command


def run_mac():
    command = take_command()
    print(command)
    if 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            print("""
            Good Morning
            I am Mac, your personal voice assistant, kindly issue a command or say 'help' to view commands list.  
            """)
            talk("""
            Good Morning
            I am Mac, your personal voice assistant, kindly issue a command or say 'help' to view commands list.  
            """)
        elif 12 <= day_time < 18:
            print("""
            Good Morning
            I am Mac, your personal voice assistant, kindly issue a command or say 'help' to view commands list.  
            """)
            talk("""
            Good Afternoon
            I am Mac, your personal voice assistant, kindly issue a command or say 'help' to view commands list. 
            """)
        else:
            print("""
            Good Morning
            I am Mac, your personal voice assistant, kindly issue a command or say 'help' to view commands list.  
            """)
            talk("""
            Good evening
            I am Mac, your personal voice assistant, kindly issue a command or say 'help' to view commands list. 
            """)
    elif 'play' in command:
        song = command.replace('play', '')
        print('Playing' + song)
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'search' in command:
        ans = command.replace('search', '')
        info = wikipedia.summary(ans, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        print('Sorry, another time perhaps?')
        talk('Sorry, another time perhaps?')
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'help' in command:
        print("""
            This is your Commands list:
            1. To wake up the Assistant we use the word 'Mac'
            2. Play 'name of the song/ Artist':Plays a song on youtube  
            3. Time :  Tell the Current system time
            4. Tell a joke/another joke : Says a random dad joke.
            5. Search : Tells you a summary of who the person is on wikipedia 
            6. Open: Launches an system application
            7. Ask it anything eg: jokes
            """)
        talk("""
            This is your Commands list:
            1. To wake up the Assistant we use the word 'Weps'
            2. Play 'name of the song/ Artist':Plays a song on youtube  
            3. Time : Current system time
            4. Tell a joke/another joke : Says a random dad joke.
            5. Search : Tells you a summary of who the person is on wikipedia 
            6. Open: Launches an system application
            7. Ask it anything eg: jokes
            """)
    elif 'calendar' in command:
        print('Opening your Calendar, one moment please...')
        talk('Opening your Calendar, one moment please')
        pyquark.filestart('/System/Applications/Calendar.app')
    elif 'chrome' in command:
        print("Opening chrome, one moment please...")
        talk("Opening chrome, one moment please")
        pyquark.filestart('/Applications/Google Chrome.app')
    elif 'notes' in command:
        print("Opening notes, one moment please...")
        talk('Opening notes, one moment please')
        pyquark.filestart('/System/Applications/Notes.app')
    elif 'photos' in command:
        print("Opening photos, one moment please...")
        talk("Opening Photos, one moment please")
        pyquark.filestart('/System/Applications/Photos.app')
    elif 'messages' in command:
        print("Opening messages, one moment please...")
        talk("Opening Messages, one moment please")
        pyquark.filestart('/System/Applications/Messages.app')
    elif 'stop' in command:
        sys.exit()
    else:
        print('Please say the command again')
        talk('Please say the command again')


while True:
    run_mac()
    # tkinter code
    root = Tk()

   # Create the menubar
    menubar = Menu(root)
    root.config(menu=menubar)

    # Create Submenu

    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Help', menu=subMenu)
    subMenu.add_command(label='Commands List', command=CommandsList)

    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Settings', menu=subMenu)
    subMenu.add_command(label='Volume', command=CommandsList)

    root.geometry("{}x{}+{}+{}".format(745, 460, int(root.winfo_screenwidth() / 2 - 745 / 2),
                                       int(root.winfo_screenheight() / 2 - 460 / 2)))
    root.resizable(0, 0)
    root.title("Mac")
    root.iconbitmap(r'icon.ico')
    root.configure(bg='#000033')

    Speak_label = Label(root, text="SPEAK:", fg="#90dec1", font='"Arial" 12 ', borderwidth=0, bg='#100017')
    Speak_label.place(x=250, y=410)

    Photo = PhotoImage(file='Mic.png')

    btn = Button(root, image=Photo, borderwidth=0, activebackground='#3a0054', bg='#3a0054', command=run_mac)
    btn.place(x=330, y=390)

    global img
    img = Image.open('app-icon.gif')
    lbl = Label(root)
    lbl.place(x=0, y=0)
    for img in ImageSequence.Iterator(img):
        img = img.resize((740, 375))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()

    root.mainloop()
    
    