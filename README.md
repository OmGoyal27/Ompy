# Ompy programming language

Hello Everyone! This is a custom programming language, specifically designed to simulate HID outputs on the device running it.
It is designed mainly for newbies, who don't want to install any kind of software on their device, but still emulate things.

It is cross-platform compatible with linux, Mac OS and Windows all are supported _(It has currently only been tested on Windows, but since it runs on Python and no OS specific libraries are used, it should technically work on all OSes.)_

Note(Date- 25/11/24): Please uncomment the lines in the mainloop of the Python script if you want to use the _onkeypressed_ function. _It is not necessary to uncomment it to use it, but it is recommended._
# Documentation

This is a language just like Python, built in Python. It is kind of based on the indentation too!

If multiple files are there, it will execute them one by one, alphabetically.
Syntaxes:

Each argument is separated with a space.

|Command|Arguments|
|-------|---------|
|type|text|
|press|key|
|combo|key_combination|
|link|Link|
|open|app|
|wait|Delay time|
|speak|text|
|popup|message|
|notify|message&title|
|pausekey|key|
|runpyfile|path|
|sendhttpreq|url|
|movemouseto|(x, y)|
|mouseclick|key|
|onkeypressed|key function1;|function2;|someotherfunction|
|end|None|
|nextfile|None|
|brightness set|brightness_level|
|brightness up|by_percent|
|brightness down|by_percent|
|window move|x, y|
|window resize|width, height|
|window maximize|None|
|window minimize|None|
|window restore|None|
|screenshot|path|
|takephoto|path|
|runcmd|command|
|execfunc|function|
|playaudio|path|

## Detailed documentation on each key

- Type

    - The type command types the given text.
    - For example; 'type Hello World!'


- Press

    - The press command presses and releases the given key.
    - Capitalisation of the key matters.
    - Could be any key.
    - Available keys:

        * 'ctrl' for the control key.
        * 'shift' for the shift key.
        * 'gui' for the Windows key.
        * 'alt' for the alt key.
        * Function keys are same; e.g. 'f13', 'f12' etc.
        * Any other keys like esc are in their original name; like esc is for the escape key, del is for the delete key, prtsc is for print screen key etc.
        * Any other alphanumeric character will be accepted.

    - For example; 'press a'


- Combo

    - The combo command presses and releases a combination of keys when called.
    - The keys to press are separated by the plus '+' symbol.
    - Available keys:

        * 'ctrl' for the control key.
        * 'shift' for the shift key.
        * 'gui' for the Windows key.
        * 'alt' for the alt key.
        * Function keys are same; e.g. 'f13', 'f12' etc.
        * Any other keys like esc are in their original name; like esc is for the escape key, del is for the delete key, prtsc is for print screen key etc.
        * Any other alphanumeric character will be accepted.

    - For example; 'combo ctrl+shift+del'


- Link

    - The link command accepts an input, that is a link and opens that link.
    - For eg; 'link omgoyal.in'


- Open

    - The open command open an app.
    - The argument to pass with it is the app name.
    - How it works: It is kind of a run dialog.
    - Note: It is optional to include extention, but it is _recommended_.
    - For eg; open notepad


- Wait

    - The wait command waits for the given period of seconds.
    - For eg; wait 3


- Speak

    - The speak command lets you make the machine speak words or sentences.
    - You could enter full sentences too, as log as Python and your machine could handle it.
    - For eg; speak Hello World!


- Popup

    - The popup command displays a popup screen with a specific tezt message.
    - Any message is accepted.
    - Other code execution is blocked until the popup is closed.
    - For eg; popup Hello World!


- Notify

    - The notify command sends a notification message to the system.
    - It accepts 2 arguments: The message and title.
    - The arguments have to be given like message&title.
    - Note- The '&' sign cannot be used for either the message or the title.
    - For eg; notify Hello World!&From Om:


- Pausekey

    - The pausekey commands blocks the script until a specific key is pressed.
    - A combination of keys is accepted.
    - The keys to press are separated by the plus '+' symbol.
    - Available keys:

        * 'ctrl' for the control key.
        * 'shift' for the shift key.
        * 'gui' for the Windows key.
        * 'alt' for the alt key.
        * Function keys are same; e.g. 'f13', 'f12' etc.
        * Any other keys like esc are in their original name; like esc is for the escape key, del is for the delete key, prtsc is for print screen key etc.
        * Any other alphanumeric character will be accepted.
    - For eg; pausekey esc


- Runpyfile

    - The runpyfile command's argument accepts the path of a Python file.
    - It accepts the file's absolute path.
    - Any pip installation required for the custom file should be done in the environment or system running the initial Python file.
    - It runs the Python file as the host.
    - For eg; runpyfile C:/PathToPythonfile.py


- Sendhttpreq

    - The sendhttpreq command sends a get request to the url.
    - It does not return anything.
    - For eg; sendhttpreq https://example.com

- Movemouseto

    - Moves the mouse cursor to a specific part of the screen.
    - It is an absolute mouse.
    - The arguments accepted are in the form of (x, y).
    - It does not click the mouse after moving it there.
    - For eg; movemouseto (0, 0)

- Mousekey

    - The mousekey command presses and releases a mouse button.
    - The arguments accepted are either 'l' for left button or 'r' for right button.
    - For eg; mousekey l


- Onkeypressed

    - The onkeypressed function, activates a thread that activates the given function when the desired key is pressed.
    - It keeps executing the next line of code, and it is a loop that never stops, unless a function is called to stop the entire script, by force.
    - Many functions can be called; each function is separated by a semicolon and then a '|'.
    - Note- No function using the semicolon and the '|' symbol consecutively can be used.
    - It is not fully practical now; but it will probably be in the future.
    - For eg; onkeypressed esc open notepad;|wait 3;|type Hello World!


- End

    - The end command stops the script. It is not required to have this function.
    - It accepts no arguments.
    - For eg; end

- Nextfile

    - The nextfile command skips the current file or like ends the current file only, and starts for the other file. If no other file is detected and the script is in a loop, it will still run continuously.
    - It accepts no arguments.
    - For eg; nextfile

- Brightness

    - The brightness can be controlled via 3 commands:
    
    - Brightness_set
        - The brightness set command accepts the brightness as an argument and it sets the brightness of the display to an absolute percentage.
        - For eg; brightness set 100
    - Brightness up
        - The brightness up command increases the brightness by the given number.
        - For eg; brightness up 20
    - Brightness down
        - The brightness down command decreases the brightness by the given number.
        - For eg; brightness down 20

- Window

    - The window command is used for adjusting the currently active window.
    - It can be controlled via 5 commands:

    - Window move

        - The window move command moves the window depending on the top left corner.
        - The accepted arguments are the x and y coordinates to move to in the format (x, y).
        - For eg; window move 0, 0

    - Window resize

        - The window resize command resizes the currently active window.
        - It accepts 2 arguments: the width and the height to set it to in the format (width, height).
        - For eg; window resize 800, 600

    - Window maximize

        - The window maximize commad accepts no arguments and maximizes the currently active window.
        - For eg; window maximize

    - Window minimize

        - The window minimize commad accepts no arguments and minimizes the currently active window.
        - For eg; window minimize

    - Window restore

        - The window restore commad accepts no arguments and restores the currently active window.
        - For eg; window restore

- Screenshot

    - The screenshot command is used to silently take a full picture of the screen.
    - The argument to pass is the path where to store the file.
    - It is also required to add the filename and the extention too.
    - For eg; screenshot C:/screenshot.png

- Takephoto

    - The takephoto command takes a picture from the camera.
    - After calling the function, the camera usually takes about 2 seconds to open, the camera light will not be on during this period.
    - The camera light will be on only for a split second.
    - The argument to pass is the save location.
    - It is also required to add the filename and the extention too.
    - For eg; takephoto C:/photo.png

- Runcmd

    - The runcmd command runs a command in the terminal.
    - If you are on Windows then it is required to add "cmd /c " before your command.
    - The terminal window will be hidden.
    - For eg; echo Hello World!

- Execfunc

    - The execfunc command executes a function present in the Python script.
    - The argument to pass is the function name without parentheses.
    - For eg; execfunc example_execfunc

- Playaudio

    - The playaudio command plays an audio file present on your computer, in the background.
    - The argument to pass is either the absolute or relative path of the audio file.
    - For eg; playaudio Examples/output.mp3