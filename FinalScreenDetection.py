import keyboard
import pyautogui
import pygetwindow as gw
import cv2
import numpy as np
import time as time
import math
import random
import os
import json
import shutil

shorcuts = []
start_time = 0
end_time = 0
prev_state = "Stay in the Test"
flag = False
# Set the video dimensions and frame rate
SCREEN_SIZE = (1920, 1080)  # Change to your screen resolution
FRAME_RATE = 30
# Define the codec and create VideoWriter object
video = str(random.randint(1, 50000)) + "SDViolation.avi"
writer = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*"XVID"), FRAME_RATE * 0.5, SCREEN_SIZE)


def SD_record_duration(text, img):
    global start_time, end_time, prev_state, flag, writer, video
    if text != "Stay in the Test" and prev_state == "Stay in the Test":
        start_time = time.time()
        for _ in range(2):
            writer.write(img)
    elif text != "Stay in the Test" and str(text) == prev_state and (time.time() - start_time) > 2:
        flag = True
        for _ in range(2):
            writer.write(img)
    elif text != "Stay in the Test" and str(text) == prev_state and (time.time() - start_time) <= 2:
        flag = False
        for _ in range(2):
            writer.write(img)
    else:
        if prev_state != "Stay in the Test":
            writer.release()
            end_time = time.time()
            duration = math.ceil(end_time - start_time)
            HeadViolation = {
                "Name": prev_state,
                "Time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)),
                "Duration": str(duration) + " seconds",
                "Mark": (2 * (duration - 2)),
                "Link": video
            }
            if flag:
                write_json(HeadViolation)
                move_file_to_output_videos(video)
            else:
                os.remove(video)
            video = str(random.randint(1, 50000)) + "STViolation.avi"
            writer = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*"XVID"), FRAME_RATE * 0.5, SCREEN_SIZE)
            flag = False
    prev_state = text


# Function to capture the screen using PyAutoGUI and return the frame as a NumPy array
def capture_screen():
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame

# function to add to JSON
def write_json(new_data, filename='violation.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def move_file_to_output_videos(file_name):
    # Get the current working directory (project folder)
    current_directory = os.getcwd()
    # Define the paths for the source file and destination folder
    source_path = os.path.join(current_directory, file_name)
    destination_path = os.path.join(current_directory, 'OutputVideos', file_name)
    try:
        # Use 'shutil.move' to move the file to the destination folder
        shutil.move(source_path, destination_path)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found in the project folder.")
    except shutil.Error as e:
        print(f"Error: Failed to move the file. {e}")
def shortcut_handler(event):
    if event.event_type == keyboard.KEY_DOWN:
        shortcut = ''
        # Check for Ctrl+C
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
            shortcut += 'Ctrl+C'
            print("Ctrl+C shortcut detected!")
        # Check for Ctrl+V
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('v'):
            shortcut += 'Ctrl+V'
            print("Ctrl+V shortcut detected!")
        # Check for Ctrl+A
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('a'):
            shortcut += 'Ctrl+A'
            print("Ctrl+A shortcut detected!")
        # Check for Ctrl+X
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('x'):
            shortcut += 'Ctrl+X'
            print("Ctrl+X shortcut detected!")
        # Check for Alt+Shift+Tab
        elif keyboard.is_pressed('alt') and keyboard.is_pressed('shift') and keyboard.is_pressed('tab'):
            shortcut += 'Alt+Shift+Tab'
            print("Alt+Shift+Tab shortcut detected!")
        # Check for Win+Tab
        elif keyboard.is_pressed('win') and keyboard.is_pressed('tab'):
            shortcut += 'Win+Tab'
            print("Win+Tab shortcut detected!")
        # Check for Alt+Esc
        elif keyboard.is_pressed('alt') and keyboard.is_pressed('esc'):
            shortcut += 'Alt+Esc'
            print("Alt+Esc shortcut detected!")
        # Check for Alt+Tab
        elif keyboard.is_pressed('alt') and keyboard.is_pressed('tab'):
            shortcut += 'Alt+Tab'
            print("Alt+Tab shortcut detected!")
        # Check for Ctrl+Esc
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('esc'):
            shortcut += 'Ctrl+Esc'
            print("Ctrl+Esc shortcut detected!")
        # Check for Function Keys F1
        elif keyboard.is_pressed('f1'):
            shortcut += 'F1'
            print("F1 shortcut detected")
        # Check for Function Keys F2
        elif keyboard.is_pressed('f2'):
            shortcut += 'F2'
            print("F2 shortcut detected!")
        # Check for Function Keys F3
        elif keyboard.is_pressed('f3'):
            shortcut += 'F3'
            print("F3 shortcut detected!")
        # Check for Window Key
        elif keyboard.is_pressed('win'):
            shortcut += 'Window'
            print("Window shortcut detected!")
        # Check for Ctrl+Alt+Del
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('del'):
            shortcut += 'Ctrl+Alt+Del'
            print("Ctrl+Alt+Del shortcut detected!")
        # Check for Prt Scn
        elif keyboard.is_pressed('print_screen'):
            shortcut += 'Prt Scn'
            print("Prt Scn shortcut detected!")
        # Check for Ctrl+T
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('t'):
            shortcut += 'Ctrl+T'
            print("Ctrl+T shortcut detected!")
        # Check for Ctrl+W
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('w'):
            shortcut += 'Ctrl+W'
            print("Ctrl+W shortcut detected!")
        # Check for Ctrl+Z
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('z'):
            shortcut += 'Ctrl+Z'
            print("Ctrl+Z shortcut detected!")
        shorcuts.append(shortcut) if shortcut != "" else None
keyboard.hook(shortcut_handler)
# Store the initial browser window and its title
browser_window = None
browser_window_title = None

# Store the initial active window and its title
active_window = gw.getActiveWindow()
active_window_title = active_window.title if active_window is not None else None

exam_window_title = active_window_title

while True:

    # Get the current active window
    new_active_window = gw.getActiveWindow()
    frame = capture_screen()

    # Check if the active window has changed
    if new_active_window is not None and new_active_window.title != exam_window_title:
        # Check if the active window is a browser or a tab
        if new_active_window.title != active_window_title:
            print("Moved to Another Window: ", new_active_window.title)
            # Update the active window and its title
            active_window = new_active_window
            active_window_title = active_window.title
        text = "Move away from the Test"
    else:
        if new_active_window is not None:
            text = "Stay in the Test"

    SD_record_duration(text, frame)
    # Check if 'finish' key is pressed
    if keyboard.is_pressed('q'):
        break

# Close the OpenCV windowq
cv2.destroyAllWindows()
write_json({
    "Name": ('Prohibited Shorcuts (' + ','.join(list(dict.fromkeys(shorcuts))) + ') are detected.'),
    "Time": 0,
    "Duration": (str(len(shorcuts))+" Counts"),
    "Mark": (2 * len(shorcuts)),
    "Link": ''
})
