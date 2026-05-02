
import os
import time
import webbrowser
import pyautogui
import requests
import wikipedia

from voice import speak

def shutdown():
    os.system("shutdown /s /t 5")

def restart():
    os.system("shutdown /r /t 5")

def screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png")

def volume_up():
    pyautogui.press("volumeup")

def volume_down():
    pyautogui.press("volumedown")
    
def stop_music():
    pyautogui.press("playpause") 

def open_camera():
    os.system("start microsoft.windows.camera:")

def close():
    pyautogui.hotkey("alt", "f4")
    
def take_photo():
    open_camera()
    time.sleep(3)
    pyautogui.press("enter") 
    time.sleep(5)
    close() 
    
def get_temperature(city="Delhi"):
    try:
        city = city.lower().replace(" ", "%20")
        url = f"https://wttr.in/{city}?format=3"
        return requests.get(url).text
    except:
        return "Weather not available"
    
def answer_question(query):

    try:
        result = wikipedia.summary(query, sentences=2, auto_suggest=False)
        speak(result)
        print(result)

    except Exception as e:
        print("Wikipedia Error:", e)
        speak("I couldn't find a clear answer on Wikipedia. Opening Google search.")
        webbrowser.open(f"https://www.google.com/search?q={query}")

def execute(command):

    command = command.lower()

