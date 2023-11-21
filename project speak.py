import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes





def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print (data) 
        except sr.UnknownValueError:
            print("Not Understanding")    


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait


if __name__ == '_main_':


    if sptext().lower() == "Hay peter" :
        data1 = sptext().lower()

        if " your name " in data1:
            name = " my name is peter"
            speechtx(name)

        elif " How are you old " in data1:
            age = " i am two years old"
            speechtx(age)

        elif ' now time ' in data1:
            time = datetime.datetime.now()  .strftime("%I%M%p")
            speechtx(time)

        elif    ' youtube' in data1:
            webbrowser.open("https://www.youtube.com/")

        elif    'google' in data1:
            webbrowser.open("https://www.google.com/")

        elif    ' jock' in data1:
            jokes_1 = pyjokes.get_joke(language="eng",category="neutral")
            speechtx(jokes_1)



            

#    else:
#        print("thanks")





