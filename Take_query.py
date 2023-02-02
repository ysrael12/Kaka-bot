from Speech_eng import speak
import pyttsx3
import webbrowser
import speech_recognition
from Take_comand import take_comand
from times import tell_time, tell_day
from Hello import Hello
import os

def Take_query():
    #TODO Hello function
    Hello()

    while(True):
        #TODO take comand function
        query = take_comand().lower()

        if "abrir o google" in query:
            speak("Abrindo o google")

            webbrowser.open("www.google.com.br/")
            continue
        
        elif "abrir o site da escola" in query:
            speak("Abrindo o Site Cesd")

            webbrowser.open("www.cesd.xyz")
            continue

        elif "desligar" in query:
            speak("desligadon")
            os.system('shutdown /s /t 1')
            continue
       
        elif "adeus" in query:
            exit()
            continue

        elif "sobre o assistente" in query:
            speak("Eu sou KAKA bot seu assistente")
