import pyttsx3
import speech_recognition as sr
# web browser search
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    # microphone used
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        # function audio create
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not Understand")


# sptext()
def speechtx():
    engine = pyttsx3.init()
    # voice modules usedd karsakti hai install kar k
    voices = engine.getProperty("voices")
    # girl speek chahuye to voices[1] kati
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    # user ki voise kam jada karsakti h clear speek then hihg speek
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
# sppeechtx("hello weldone dipika baror, you are so cute")
    
if __name__ == '__main__':

    if "hey peter" in sptext().lower():        
            while True:

                # if sptext().lower() == "hey peter" :
                    data1=sptext().lower()

                    if "your name" in data1:
                         name = "my name is peter"
                         speechtx(name)
                    # data2= sptext().lower()

                    elif "your age" in data1:
                         age = "i am twenty two years old"
                         speechtx(age)

                    elif "Now a time" in data1:
                        # time ko search karne k liye strftime ka used hota hai
                        time = datetime.datetime.now().strftime("%I%M%P")
                        speechtx(time)
                        # print(time)

                    elif 'youtube' in data1:
                         webbrowser.open("https://www.youtube.com/")

                    elif 'web' in data1:
                         webbrowser.open("https://www.wscubetech.com/")


                    elif "joke" in data1:
                         joke_1 = pyjokes.get_joke(language="en",category="neutral")
                         print(joke_1)
                         speechtx(joke_1)


                    # python song create
                    elif 'play song' in data1:
                         add = "D:\bhajan\song"
                         listsong = OSError.listdir(add)
                         print(listsong)
                         OSError.startfile(OSError.path.join(add,listsong[1]))

                    elif "exit" in data1:
                        speechtx("thank you")
                        break

                    time.sleep(10)


                # else:
                #     print("thanks")

