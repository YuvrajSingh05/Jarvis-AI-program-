
import subprocess
import wikipedia
from voice import speak, listen
from utils import *
from system_control import *
import webbrowser
import pywhatkit
import pyautogui

# decision making

def execute(command):

    # TIME
    if "time" in command:
        speak(f"The time is {get_time()}")
        print(f"The time is {get_time()}")

    # DATE
    elif "date" in command:
        speak(f"Today's date is {get_date()}")
        print(f"Today's date is {get_date()}")

    # BATTERY
    elif "battery" in command:
        speak(f"Your battery is at {get_battery()}")
        print(f"Your battery is at {get_battery()}")

    # OPEN GOOGLE
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    # OPEN CHROME
    elif "open chrome" in command:
        speak("Opening Chrome")
        webbrowser.open("https://chrome.com")

    # OPEN YOUTUBE
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # OPEN GMAIL
    elif "open gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    # CLOSE GOOGLE CHROME 
    elif "close chrome" in command:
        speak("Closing Chrome completely")
        os.system("taskkill /F /IM chrome.exe /T")

    # CLOSE GOOGLE
    elif "close google" in command:
        speak("Closing Google")
        os.system("taskkill /f /im chrome.exe")

    # CLOSE YOUTUBE 
    elif "close youtube" in command:
        speak("Closing YouTube")
        os.system("taskkill /f /im chrome.exe")

    # CLOSE GMAIL 
    elif "close gmail" in command:
        speak("Closing Gmail")
        os.system("taskkill /f /im chrome.exe")

    # CLOSE NOTEPAD
    elif "close notepad" in command:
        speak("Closing Notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "open desktop folder" in command or "can you open it" in command:
        speak("Opening Desktop folder")
        path = os.path.join(os.environ["USERPROFILE"], "OneDrive", "Desktop")
        os.startfile(path)

    # CREATE FOLDER
    elif "create folder" in command:
        speak("What should I name the folder?")
        name = listen()

        try:
            desktop = os.path.join(os.environ["USERPROFILE"],"OneDrive", "Desktop")
            path = os.path.join(desktop, name)

            os.makedirs(path, exist_ok=True)

            speak(f"Folder {name} created on desktop")

        except:
            speak("Sorry, I could not create folder")


    # WEATHER / TEMPERATURE
    elif "temperature" in command or "weather" in command:
        speak("Tell me city name")
        city = listen()

        if not city:
            city = "Delhi"
        else:
            city = city.replace("in", "").replace("at", "").strip()

        weather = get_temperature(city)

        speak(weather)
        print(weather)

    # SEARCH
    elif "search" in command:
        speak("What should I search?")
        query = listen()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://google.com/search?q={query}")

    elif "wikipedia" in command:
        try:
            speak("What should I search on Wikipedia?")
            query = listen()

            result = wikipedia.summary(query, sentences=2)

            speak(result)

        except:
            speak("No results found")

    # PLAY SONG
    elif "play song" in command:
        speak("Which song?")
        song = listen()
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    
    # PLAY MUSIC

    elif "play music" in command:
        speak("Playing system music")

        music_dir = os.path.join(os.environ["USERPROFILE"], "Music")

        songs = os.listdir(music_dir)

        music_files = [song for song in songs if song.endswith(".mp3")]

        if not music_files:
            speak("No mp3 music found in your system")
        else:
            import random

            song = random.choice(music_files)

            speak(f"Playing {song}")
            os.startfile(os.path.join(music_dir, song))
            
    elif "close media" in command or "close music" in command:
      speak("Closing media player")
      close()
      speak("Media is closed")

    # SCREENSHOT
    elif "screenshot" in command:
        speak("Taking screenshot")
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        speak("Screenshot taken")

    # CALCULATOR

    elif "calculate" in command:
        if "can you calculate" in command or "calculate" in command:
            try:
                speak("Calculating")

                expression = command
                expression = expression.replace("calculate", "")
                expression = expression.replace("plus", "+")
                expression = expression.replace("minus", "-")
                expression = expression.replace("into", "*")
                expression = expression.replace("multiply", "*")
                expression = expression.replace("x", "*")
                expression = expression.replace("divided by", "/")

                result = eval(expression)
                speak(f"The answer is {result}")

            except:
                speak("Sorry, I could not calculate that")

# SHUTDOWN
    elif "shutdown" in command:
        speak("Shutting down system")
        shutdown()
# RESTART
    elif "restart" in command:
        speak("Restarting system")
        restart()

# VOLUME UP
    elif "volume up" in command:
        speak("Increasing volume")
        volume_up()

# VOLUME DOWN
    elif "volume down" in command:
        speak("Decreasing volume")
        volume_down()

# PLAY/PAUSE MUSIC
    elif "stop song" in command or "stop music" in command  or "pause music" in command:
        speak("Stopping music")
        stop_music()
# OPEN CAMERA
    elif "open camera" in command:
        speak("Opening camera")
        open_camera()
# CLOSE CAMERA
    elif "close camera" in command:
        speak("Closing camera")
        os.system("taskkill /f /im WindowsCamera.exe") 
 # TAKE PHOTO
    elif "take photo" in command or "click photo" in command:
        speak("Taking photo")
        take_photo()
        speak("Photo clicked")

# OPEN NOTEPAD

    elif "open notepad" in command:
      speak("Opening Notepad")
      subprocess.Popen("notepad.exe")

# CLOSE NOTEPAD
    elif "close notepad" in command:
     speak("Closing Notepad")
     subprocess.call("taskkill /f /im notepad.exe")


    # OPEN DESKTOP
    elif "open desktop" in command:
        speak("Opening Desktop")
        desktop = os.path.join(os.environ["USERPROFILE"], "OneDrive", "Desktop")
        os.startfile(desktop)

    elif "close desktop" in command:
      speak("Closing Desktop")
      os.system("taskkill /f /im explorer.exe & start explorer.exe")

    # OPEN DOWNLOADS
    elif "open downloads" in command  or "open download" in command:
        speak("Opening Downloads")
        downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
        os.startfile(downloads)

    elif "close downloads" in command or "close download" in command:
      speak("Closing Downloads")
      os.system("taskkill /f /im explorer.exe & start explorer.exe")

   # OPEN SETTINGS
    elif "open settings" in command:
        speak("Opening Windows Settings")
        os.system("start ms-settings:")

    elif "close settings" in command:
     speak("Closing Settings")
     os.system("taskkill /f /im SystemSettings.exe")

  # LOCK PC
    elif "lock pc" in command:
        speak("Locking your PC")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif "unlock pc" in command:
      speak("I cannot unlock the PC automatically due to security restrictions. Please unlock it manually.")

    # OPEN THIS PC
    elif "open this pc" in command or "open my computer" in command:
        speak("Opening This PC")
        os.system("explorer shell:MyComputerFolder")

    # CHAT RESPONSES
    elif "hi" in command or "hello" in command:
        speak("Hello! How can I help you?")

    elif "what are you doing" in command:
      speak("I am listening to your commands and ready to assist you.")

    elif "how are you" in command or "how r u" in command:
        speak("I am fine, thank you for asking. How can I assist you?")

    elif "what you can do" in command or "your features" in command or "help" in command:
        speak("I can help you with system control, web browsing, media control, and knowledge answers. Here are my features:")
        features = """
    System Info: tell you time, date, battery status.
    Web: open google, youtube, chrome, gmail, search anything.
    Files: open desktop, downloads, this pc, and create folder.
    System Control: open notepad, settings, lock system, shutdown, restart.
    Volume: increase, decrease, stop music.
    Camera: open camera, take photo,  take screenshot.
    Media: play system music, play songs on youtube.
    Knowledge: wikipedia, what is, who is, do you know.
    Chat: hello, hi, how are you, who are you.
    Exit: goodbye, exit program."""
        speak(features)

    elif "what are your features" in command or "your features" in command:
        speak("I can open apps, websites, folders, and answer basic questions like a simple assistant.")

    elif "tell me about yourself" in command or "describe yourself" in command:
     speak("I am your personal AI assistant built using Python. I can help you open applications, browse websites, manage files, control system tasks, and answer your questions like a smart assistant.")

    elif "who are you" in command or "hu r u" in command or "how r u" in command:
        speak("I am your personal assistant created in Python.")

    elif "trending ai" in command or "open trending ai" in command:
        speak("Opening trending AI news")
        webbrowser.open("https://www.google.com/search?q=latest+AI+news+today")
        
    elif "close trending AI" in command or "close trending" in command:
        speak("Closing trending ai")
        close()

    elif "today news" in command or "news" in command:
        speak("Opening today's news for you")
        webbrowser.open("https://news.google.com/")

    elif "terminate news" in command or "close it" in command:
        speak("Closing")
        close()

    elif ("latest" in command or
      "any latest news" in command or
      "any latest new" in command):
       speak("Yes, I am always ready for your updates.")
       speak("You can ask me today's news or trending AI updates.")

    # EXIT
    elif "exit" in command or "goodbye" in command:
        speak("Goodbye have a nice day")
        return False

    elif "what is" in command or "who is" in command or "tell me about" in command or"do you know" in command or "where is" in command:
        speak("Let me think")
        query = command.replace("what is", "")
        query = query.replace("who is", "")
        query = query.replace("where is", "")
        query = query.replace("tell me about", "")
        query = query.replace("do you know", "")
        query = query.strip()
        answer_question(query)

    else:
       speak("Sorry, I couldn't process that command. Please try again.")

    return True 