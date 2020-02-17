# blueberry-assistant
Multi-platform virtual assistant written entirely in python!
Please create a virtual environment before installing any of these because dependencies can get messed up.

There are several dependencies for this project:
```python
virtualenv, pyaudio==0.2.11, pvporcupine, pyautogui, SpeechRecognition, geopy, wolframalpha, darksky, urllib3, tflearn, tensorflow, nltk
```

Please install them in the order listed above. Otherwise, ```pvporcupine``` will try to install ```pyaudio``` in a different version than ```SpeechRecognition``` wants.

# Setup
Inside your dedicated virtual environment, run ```python3 Learn.py``` to setup the tensorflow files and
```python
python3 -c "import nltk ; nltk.download('punkt')"
``` 
to set up nltk.
