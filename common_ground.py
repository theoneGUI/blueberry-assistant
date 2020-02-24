import os
def say(text):
    print(text)
    os.system('espeak "{}" -a 300 -v english-us -s 125 2>/dev/null'.format(text))
