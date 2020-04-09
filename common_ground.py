import os
def say(text):
    print(text)
    os.system('espeak "{}" -v english-us -a 80 -s 125 --stdout > file.wav'.format(text))
    os.system('aplay file.wav')
