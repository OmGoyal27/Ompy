import pyautogui as pg
import webbrowser
import subprocess
from pathlib import Path
import time
import pyttsx3
from plyer import notification
from keyboard import wait as waitforkeypressed, add_hotkey
import requests
from threading import Thread
from sys import exit as stopscript, argv
from pathlib import Path
import screen_brightness_control as sbc
import pygetwindow
import cv2

TEXT_TO_SPEECH_SPEED = 130
POPUP_TITLE = "Popup message"
NOTIFICATION_TIMEOUT_SECONDS = 3


def set_brightness(brightness_level: int):
    # get current brightness value
    previous_brightness_level = sbc.get_brightness()[0]
    print(f"Previously brightness level was {previous_brightness_level}% and now it is {brightness_level}%")
    # Set the brightness of the primary display
    sbc.set_brightness(brightness_level, display=0)

def brightness_up(brightness_increase_by: int):
    # get current brightness value
    brightness_level = sbc.get_brightness()[0]
    print(f"Current brightness level: {brightness_level}%")
    brightness_level = brightness_level + brightness_increase_by

    # Set the brightness of the primary display
    set_brightness(brightness_level)

def brightness_down(brightness_decrease_by: int):
    # get current brightness value
    brightness_level = sbc.get_brightness()[0]
    print(f"Current brightness level: {brightness_level}%")
    brightness_level = brightness_level - brightness_decrease_by
    
    # Set the brightness of the primary display
    set_brightness(brightness_level)

def move_window_coordinates_from_topleft(x: int, y: int):
    # Get the currently active window
    active_window = pygetwindow.getActiveWindow()
    if active_window:
        active_window.restore()     # This is required just in case the window is maximized.

        # Move the window
        active_window.topleft = x, y  # Move to (100, 100)
    else:
        print("No active window found!")

def set_window_size(width: int, height: int):
    active_window = pygetwindow.getActiveWindow()
    if active_window:
        active_window.restore()     # This is required just in case the window is maximized.

        # Resize the window
        active_window.width = width
        active_window.height = height
    else:
        print("No active window found!")

def text_to_speech(text):
    global TEXT_TO_SPEECH_SPEED
    speed = TEXT_TO_SPEECH_SPEED
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the speed (words per minute)
    engine.setProperty('rate', speed)

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

def combo(argument: str):
    arguments = argument.split('+')
    
    pg.hotkey(arguments)

def take_picture(save_path: str):
    '''Takes a picture for the camera and saves it to the desired location.'''
    # Initialize the camera (0 is typically the default camera)
    camera = cv2.VideoCapture(0)        # Change the camera number according to you.

    # Check if the camera opened successfully
    if not camera.isOpened():
        print("Error: Could not access the camera.")
    else:
        # Capture a single frame
        ret, frame = camera.read()

        if ret:
            # Save the captured frame to the specified path
            cv2.imwrite(save_path, frame)
            print(f"Screenshot saved at {save_path}")
        else:
            print("Error: Could not capture a frame.")

    # Release the camera
    camera.release()


def custom_funcs(function_names: str):
    '''Performs a series of functions given based on the function names.'''
    function_names = function_names.split(";|")       # Get the list of all the functions
    
    for function in function_names:
        function_name, argument = function.split(' ', 1)        # Gets the function name and argument separated
        doFunc(function_name, argument)


def doFunc(function_name: str, argument: str):
    global POPUP_TITLE
    global NOTIFICATION_TIMEOUT_SECONDS
    '''
    Performs the required function.
    Args:
    function_name: The name of the actual function.
    arguments: The value to pass with it.'''
    function_name = function_name.lower()
    
    match function_name:
        case "type":
            print(f"Typing {argument}")
        
            pg.typewrite(argument)
        
        case "press":
            print(f"Pressing {argument}")
        
            pg.press(argument)
        
        case "combo":
            print(f"Pressing keys {argument}")
        
            combo(argument)
        
        case "link":
            print(f"Opening {argument}")
        
            webbrowser.open(argument)
        
        case "open":
            print(f"Opening the app {argument}")
        
            subprocess.Popen(argument, creationflags=subprocess.CREATE_NEW_CONSOLE)
        
        case "wait":
            print(f"Waiting for {argument} seconds.")
        
            time.sleep(int(argument))
        
        case "speak":
            print(f"Speaking {argument}")
        
            text_to_speech(argument)
        
            print(f"Spoke {argument}")
        
        case "popup":
            print(f"Displaying message {argument}")
        
            pg.alert(argument, POPUP_TITLE)
        
        case "notify":
            message, title = argument.split("&")
            print(f"Sending notificataion '{message}' with title '{title}'")
        
            notification.notify(        # Send a notification to the system.
            title=title,
            message=message,
            timeout=NOTIFICATION_TIMEOUT_SECONDS
            )
        
        case "pausekey":
            print(f"Waiting for key {argument}")
        
            waitforkeypressed(argument)
        
            print(f"Resuming script as key {argument} was pressed.")
        
        case "runpyfile":
            print(f"Running Python file located at location {argument}")
            
            with open(argument) as rawcustomcode:
                exec(rawcustomcode.read())      # Run the code
            
            print("Successfully ran the Python file.")

        case "sendhttpreq":
            print(f"Sending an HTTP request to {argument}")
            
            requests.get(argument)
            
            print(f"Sent an HTTP request to {argument}")
        
        case "movemouseto":
            print(f"Moving mouse to {argument}")
            
            x, y = argument.split(", ")
            x = int(x.removeprefix('('))
            y = int(y.removesuffix(')'))
            pg.moveTo((x, y))
            
        case "mousekey":
            if argument.lower() == 'l':
                print("Clicking the left button.")
                
                pg.leftClick()
            
            if argument.lower() == 'r':
                print("Clicking the right button.")
                
                pg.rightClick()

        case "onkeypressed":
            key, functions = argument.split(' ', 1)
            print(f"Will wait for key {key} from now on.")
            
            add_hotkey(key, custom_funcs, args=(functions,))
            time.sleep(1)

        case "brightness":
            function_to_perform_for_brightness, percentage = argument.split()
            percentage = int(percentage)        # Convert it into an integer
            match function_to_perform_for_brightness:
                case "set":
                    print(f"Setting brightness to {percentage}%.")
                    set_brightness(percentage)

                case "up":
                    print(f"Increasing brightness by {percentage}%.")
                    brightness_up(percentage)

                case "down":
                    print(f"Decreasing brightness by {percentage}%.")
                    brightness_down(percentage)
                case _:
                    print(f"Unknown command {function_name} for brightness.")

        case "window":
            function_to_perform_for_window = argument.split(' ', 1)
            match function_to_perform_for_window[0]:
                case "move":
                    passed_args = function_to_perform_for_window[1]
                    x, y = passed_args.split(', ')
                    x = int(x)
                    y = int(y)
                    print(f"Moving the current active window to {x}, {y}.")
                    move_window_coordinates_from_topleft(x, y)
                case "resize":
                    passed_args = function_to_perform_for_window[1]
                    width, height = passed_args.split(', ')
                    width = int(width)
                    height = int(height)
                    print(f"Resizing the currently active window to {width}, {height}.")
                    set_window_size(width, height)
                case "maximize":
                    print("Maximizing the cuurently active window.")
                    active_window = pygetwindow.getActiveWindow()
                    if active_window:
                        active_window.maximize()
                    else:
                        print("No active window found!")
                case "minimize":
                    print("Minimizing the cuurently active window.")
                    active_window = pygetwindow.getActiveWindow()
                    if active_window:
                        active_window.minimize()
                    else:
                        print("No active window found!")
                case "restore":
                    print("Restoring the cuurently active window.")
                    active_window = pygetwindow.getActiveWindow()
                    if active_window:
                        active_window.restore()
                    else:
                        print("No active window found!")
        
        case "screenshot":
            print("Taking a screenshot...")

            # Take a screenshot
            screenshot = pg.screenshot()

            # Save the screenshot to the desired location
            save_path = argument                            # Just to make everything clear
            screenshot.save(save_path)

            print(f"Screenshot saved at {save_path}")
        
        case "takephoto":
            print(f"Taking photo and saving it to {argument}")
            take_picture(argument)

        case _:
            print(f"Unknown command: {function_name}")        # Unknown command


def main():
    global eachLineCode
    
    for eachCode in eachLineCode:
        function_name, argument = eachCode.split(' ', 1)        # Gets the function name and argument separated
        
        if function_name.lower() == 'end':
            stopscript('The script ended successfully.')
        elif function_name.lower() == 'nextfile':
            print("Skipping this file...")
        else:
        
            doFunc(function_name.lower(), argument)

    # Uncomment the below lines if you want the script to end only when specified.
    # while True:
    #     pass

if __name__ == '__main__':
    # Check if a file was passed as an argument
    if len(argv) > 1:
        om_file = argv[1]
        if om_file.endswith('.om'):
            path = Path(om_file)
            
            code = path.read_text(encoding='utf-8')

            try:
                eachLineCode = code.splitlines()            # Gets each line of the code.

                eachLineCode[:] = [code for code in eachLineCode if code != '']     # Filters for empty lines.
            except Exception as e:
                print("It is a single line argument.")

            main()
        else:
            print(f"{om_file} is not a valid .om file.")
            stopscript(f"{om_file} is not a valid .om file.")
    else:

        # Get the current working directory
        working_dir = Path.cwd()

        # List and read all .om files
        om_files = sorted(list(working_dir.glob("*.om")))           # Returns them alphabetically.

        if not om_files:
            print("No .om files found in the working directory.")
        else:
            for file in om_files:
                with file.open('r') as content:
                    code = content.read()

                    try:
                        eachLineCode = code.splitlines()            # Gets each line of the code.

                        eachLineCode[:] = [code for code in eachLineCode if code != '']     # Filters for empty lines.
                    except Exception as e:
                        print("It is a single line argument.")

                    main()