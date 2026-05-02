import datetime
import psutil

# helper functions (tools)
def get_time():
    return datetime.datetime.now().strftime("%H:%M")

def get_date():
    return datetime.datetime.now().strftime("%d %B %Y")

def get_battery():
    battery = psutil.sensors_battery()
    return f"{battery.percent}%"