import os
os.chdir("/home/pi/updateAssistant")
def say(text):
    print(text)
    with open("voiceNum.log") as file:
        v=file.readlines()
    if v[0] == "1":
        os.system('espeak "{}" -v english-us -p 50 -a 80 -s 125 --stdout > file.wav'.format(text))
        os.system('aplay file.wav')
    elif v[0] == '2':
        os.system("""echo "{}" | festival --tts""".format(text))
    elif v[0] == '3':
        os.system("""./speech.sh "{}" """.format(text)) 
