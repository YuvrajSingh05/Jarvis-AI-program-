import pyttsx3
import speech_recognition as sr


#SPEAK
def speak(text):
    try:
        print("Jarvis:", text)

        engine = pyttsx3.init()

        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)

        engine.say("Sir, " + text)
        engine.runAndWait()

        engine.stop()

    except Exception as e:
        print("Voice Error:", e)


#LISTEN
def listen(awake=True):
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            if awake:
                print("Listening...")

            r.adjust_for_ambient_noise(source, duration=0.5)
            r.pause_threshold = 1

            audio = r.listen(source)

        command = r.recognize_google(audio, language='en-in')

        if awake:
            print("You said:", command)

        return command.lower()

    except Exception as e:
        print("Speech Error:", e)
        return ""