# Ompy programming language

Hello Everyone! This is a custom programming language, specifically designed to simulate HID outputs on the device running it.
It is designed mainly for newbies, who don't want to install any kind of software on their device, but still emulate things.

It is cross-platform compatible with linux, Mac OS and Windows all are supported _(It has currently only been tested on Windows, but since it runs on Python and no OS specific libraries are used, it should technically work on all OSes.)_
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