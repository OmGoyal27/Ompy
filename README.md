# Om programming language

Hello Everyone! This is a custom programming language, specifically designed to simulate HID outputs on the device running it.
It is designed mainly for newbies, who don't want to install any kind of software on their device, but still emulate things.

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
    - Note: Do not inclue the extention.
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