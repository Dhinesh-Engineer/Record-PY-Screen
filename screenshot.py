import keyboard
import pygetwindow as gw
import pyautogui
from datetime import datetime

def screenshot():
    active_window = gw.getActiveWindow()
    
    if(active_window):
        x, y, width, height = active_window.left, active_window.top,active_window.width,active_window.height
        
        screenshot =pyautogui.screenshot(region=(x,y,width,height))
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        path = f"screenshot_{timestamp}.png"
        screenshot.save(path)
        
        print("File Saved");
        
    else:
        print("No Active Window")
    
keyboard.add_hotkey('ctrl+k',screenshot)

keyboard.wait('esc')
        