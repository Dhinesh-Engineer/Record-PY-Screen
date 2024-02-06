import pyautogui
import keyboard
from datetime import datetime
import imageio
import os
import numpy as np  # Import numpy for array conversion

directory = os.path.dirname(os.path.abspath(__file__))
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
path = os.path.join(directory, 'recording', f'screen_recording_{timestamp}.mp4')

frame_rate = 10

is_recording = False

def start():
    global is_recording
    is_recording = True

def stop():
    global is_recording
    is_recording = False

keyboard.add_hotkey('ctrl+alt+s', start)
keyboard.add_hotkey('ctrl+alt+q', stop)

video_writer = imageio.get_writer(path, fps=frame_rate)

try:
    while True:
        if is_recording:
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)  # Convert the PIL Image to a numpy array
            video_writer.append_data(frame)
            pyautogui.sleep(1/frame_rate)
except KeyboardInterrupt:
    print("Recording Interrupted.")
finally:
    video_writer.close()
    print("Recording Completed.")