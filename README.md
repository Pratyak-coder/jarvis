# Voice Assistant: Mango

Overview

Mango is a simple voice-activated assistant built in Python. It listens for a wake word ("mango") and executes commands like opening Google in a web browser. It uses speech recognition and text-to-speech for interaction.

## Requirements

- Python 3.x
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `webbrowser`

## Installation

1. Install Python 3.x.
2. Install required libraries:

   ```
   pip install speechrecognition pyttsx3
   ```
3. Ensure a working microphone is connected.

## Usage

1. Run the script:

   ```
   python mango.py
   ```
2. Say "mango" to activate the assistant.
3. Speak a command (e.g., "open google").
4. Say "exit" to stop the program.

## Features

- Wake Word: Activates on "mango".
- Commands:
  - "open google": Opens Google in the default web browser.
- Text-to-Speech: Provides voice feedback.
- Error Handling: Handles speech recognition errors gracefully.

## Notes

- Uses Google's Speech Recognition API (default key).
- Microphone timeout: 2 seconds for wake word, 5 seconds for commands.
- Add more commands by modifying the `Command_Process` function.

## Limitations

- Requires internet for speech recognition.
- Limited command set (extendable in `Command_Process`).
- Basic error handling for unrecognized speech or microphone issues.
