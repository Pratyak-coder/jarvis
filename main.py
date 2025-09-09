import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def Speak(text):     
    engine.say(text)
    engine.runAndWait()

def Command_Process(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    print (c)

    pass

def exit():
    pass

if __name__=="__main__":
    Speak("initializing mango")
    

    while True:
        r = sr.Recognizer()
    


        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
           # obtain audio from the microphone 
            with sr.Microphone() as source:
                print("Recognizing")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            Wake_Word = r.recognize_google(audio)
        
            # listen the wake_word "mango"
            if Wake_Word.lower() == "mango":
                Speak("..yep..")
                with sr.Microphone() as source:
                    print("Mango Active")
                    audio = r.listen(source , timeout =5, phrase_time_limit = 5)
                command = r.recognize_google(audio)
                Command_Process(command)        
            
            elif Wake_Word.lower() == "exit":
                break


        except Exception as e:
            print("error ; {0}".format(e))

