import pyttsx3
import webbrowser
import speech_recognition as sr

def take_comand():
     r = sr.Recognizer()

     with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Reconhecendo")
             
            
            Query = r.recognize_google(audio, language='pt-br')
            print("Comando=", Query)
             
        except Exception as e:
            print(e)
            print("Repita")
            return "None"
         
        return Query