# Ompy Programming Language

A simple, cross-platform automation programming language built in Python, designed for beginners who want to automate tasks without complex software installations.

## 🌟 Overview

Ompy is a custom programming language specifically designed to simulate HID (Human Interface Device) outputs and automate various system tasks. It provides an easy-to-learn syntax that allows users to control their computer through simple commands.

### Key Features

- **Cross-platform compatibility** - Works on Windows, macOS, and Linux
- **Simple syntax** - Easy to learn for beginners
- **No complex installations** - Just Python and a few dependencies
- **Automation focused** - Built specifically for task automation
- **Human Interface Device simulation** - Control keyboard, mouse, and system functions

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running Ompy Scripts

There are two ways to run Ompy scripts:

#### Method 1: Run a specific .om file
```bash
python main.py your_script.om
```

#### Method 2: Run all .om files in current directory
```bash
python main.py
```
*This will execute all .om files in the current directory alphabetically.*

## 📝 Language Syntax

Ompy uses a simple command-based syntax where each line contains a command followed by its arguments.

### Basic Commands

| Command | Arguments | Description |
|---------|-----------|-------------|
| `type` | text | Types the specified text |
| `press` | key | Presses and releases a key |
| `combo` | key+combination | Presses key combinations (e.g., ctrl+c) |
| `link` | url | Opens a link in the default browser |
| `open` | application_path | Opens an application |
| `wait` | seconds | Pauses execution for specified seconds |
| `speak` | text | Uses text-to-speech to speak the text |
| `popup` | message | Shows a popup message |
| `notify` | message&title | Shows a system notification |

### Advanced Commands

| Command | Arguments | Description |
|---------|-----------|-------------|
| `screenshot` | file_path | Takes a screenshot and saves it |
| `takephoto` | file_path | Takes a photo using the camera |
| `playaudio` | file_path | Plays an audio file |
| `brightness set` | level | Sets screen brightness (0-100) |
| `brightness up` | percentage | Increases brightness by percentage |
| `brightness down` | percentage | Decreases brightness by percentage |
| `window move` | x, y | Moves active window to coordinates |
| `window resize` | width, height | Resizes active window |
| `window maximize` | - | Maximizes active window |
| `window minimize` | - | Minimizes active window |
| `movemouseto` | x, y | Moves mouse to coordinates |
| `mouseclick` | button | Clicks mouse button (left/right/middle) |

## 💡 Examples

### Hello World Example
```ompy
type Hello, World!
```

### Open Notepad and Type
```ompy
open notepad
wait 2
type This is written by Ompy!
```

### Brightness Control
```ompy
brightness set 50
wait 2
brightness up 20
```

### Window Management
```ompy
window move 100, 100
window resize 800, 600
wait 1
window maximize
```

### System Notification
```ompy
notify Welcome to Ompy!&Getting Started
speak Welcome to the Ompy programming language
```

## 📁 Project Structure

```
Ompy/
├── main.py              # Main interpreter
├── commands.om          # Example commands
├── requirements.txt     # Python dependencies
├── DOCUMENTATION.md     # Detailed documentation
├── Examples/           # Example scripts
│   ├── hello world in notepad.om
│   ├── take screenshot.om
│   ├── rickroll.om
│   └── ...
└── README.md           # This file
```

## 🔧 Advanced Usage

For in-depth detail of the program, read the [DOCUMENTATION.md](DOCUMENTATION.md) file.
## 🔍 Available Keys

### Special Keys
- `ctrl` - Control key
- `shift` - Shift key
- `gui` - Windows/Cmd key
- `alt` - Alt key
- `esc` - Escape key
- `del` - Delete key
- `prtsc` - Print Screen

### Function Keys
- `f1`, `f2`, `f3`, ..., `f12`

### Other Keys
- Any alphanumeric character (a-z, 0-9)
- `space`, `enter`, `tab`, `backspace`

## ⚠️ Important Notes

- **Security**: Be cautious when running scripts from untrusted sources as they can control your system
- **Permissions**: Some features may require elevated permissions
- **Testing**: Currently tested primarily on Windows, but designed to be cross-platform
- **Camera Access**: `takephoto` command requires camera permissions

## 🤝 Contributing

This project is part of the "Abandoned Amazing" collection but contributions and improvements are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

See the `LICENCE` file for details.

## 🎯 Use Cases

- **Task Automation** - Automate repetitive computer tasks
- **Presentation Control** - Create automated presentations
- **System Administration** - Batch system operations
- **Educational** - Learn programming concepts through automation
- **Accessibility** - Create custom automation for accessibility needs
- **Testing** - Automated UI testing scenarios

## 🚨 Disclaimer

Use this tool responsibly. The authors are not responsible for any misuse or damage caused by this software. Always test scripts in a safe environment before using them on important systems.

---

**Made with ❤️ for the automation community**