import pyautogui as pg
import webbrowser
import subprocess
from pathlib import Path
import time
import pyttsx3


def text_to_speech(text):
    speed = 130
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

def doFunc(function_name: str, argument: str):
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
        case "popup":
            print(f"Displaying message {argument}")
            pg.alert(argument, "Popup message")
        case _:
            print("Unknown command.")        # Unknown command


def main():
    for eachCode in eachLineCode:
        function_name, argument = eachCode.split(' ', 1)        # Gets the function name and argument separated
        doFunc(function_name.lower(), argument)


if __name__ == '__main__':
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