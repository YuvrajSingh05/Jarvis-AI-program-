import datetime

from voice import speak, listen
from commands import execute

awake = True


# GREETING
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour < 12:
        speak("Good morning")
    elif hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Jarvis. How can I help you?")


wish()


# MAIN LOOP

while True:

    # ALWAYS LISTEN
    command = listen(awake=awake)

    if not command:
        continue

    command = command.lower()

    # WAKE WORD 
    wake_words = [
        "jarvis", "hi jarvis", "hello jarvis",
        "hey jarvis", "wake up", "are you there", "arise"
    ]

    if any(word in command for word in wake_words):
        awake = True
        speak("I am back online")
        continue

    # SLEEP MODE
    sleep_words = [
        "sleep", "go to sleep", "take a break",
        "stop listening", "please wait"
    ]

    if any(word in command for word in sleep_words):
        awake = False
        speak("Going to sleep mode")
        continue

    # IGNORE COMMANDS IN SLEEP
    if not awake:
        continue

    # EXECUTE COMMANDS ONLY WHEN AWAKE
    response = execute(command)

    # EXIT SYSTEM
    if response == False:
        speak("Goodbye, shutting down assistant")
        break