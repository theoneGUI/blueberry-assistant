import random
global voice
voice=random.randint(1,3)
from common_ground import *
from threading import Thread
def begin():
    os.system('aplay computerbeep_75.wav')
    say('''Blueberry is starting up''')
Thread(target=begin).start()
from pvporcupine import Porcupine
from datetime import datetime
import numpy as np
import soundfile, pyaudio, sys, struct, os, understanding
from datetime import datetime
import pvporcupine
def words(IN):
    res = re.findall(r'\w+', IN) 
    return res
handle = pvporcupine.create(keywords=['blueberry', 'hey google'])
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=handle.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=handle.frame_length)
def naf():
    pcm = audio_stream.read(handle.frame_length, exception_on_overflow=False)
    pcm = struct.unpack_from("h" * handle.frame_length, pcm)
    return pcm
say('ready')
x=[]
#try:
while True:
    pcm=naf()
    keyword_index=handle.process(pcm)
    if keyword_index >= 0:
        a=understanding.listen()
        if a == '.again}' or a == 'do that again':
            last=x[len(x)-int(1)]
            print(last)
            understanding.passthrough(last)
        else:
            x.append(a)
    if len(x) > 100:
        del x
        x=[]
#finally:
#    handle.delete()
