# blueberry-assistant-satellite
Multi-platform virtual assistant written entirely in python!
Please create a virtual environment before installing any of these because dependencies can get messed up.
Especially on Windows, please execute all commands inside the root directory of the project.
There are several dependencies for this project:
```python
virtualenv, pyaudio==0.2.11, pvporcupine, pyautogui, SpeechRecognition, geopy, wolframalpha, darksky, urllib3, tflearn, tensorflow, nltk
```

Please install them in the order listed above. Otherwise, ```pvporcupine``` will try to install ```pyaudio``` in a different version than ```SpeechRecognition``` wants.

# Setup
Inside your dedicated virtual environment, run ```python3 Learn.py``` to setup the tensorflow files and
```python
python -c "import nltk ; nltk.download('punkt')"
``` 
to set up nltk.
The AI part must be set up before the scripts can run successfully, so in the virtual environment or root directory of the scripts, run ```python Learn.py```. The satellite can be augmented to fit (almost) any need. With proper modifications, it can be run on any platform.
