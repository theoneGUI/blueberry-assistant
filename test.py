from common_ground import *
from threading import Thread
def begin():
    os.system('aplay computerbeep_75.wav')
    say('''Hello and welcome to the blueberry assistant. I am starting
up now and before we begin, I would like to say that if you ever need me,
just say blueberry and I will start listening for any commands I may execute.''')
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
handle = pvporcupine.create(keywords=['blueberry', 'bumblebee'])
#library_path = ... # Path to Porcupine's C library available under lib/${SYSTEM}/${MACHINE}/
#model_file_path = . # It is available at lib/common/porcupine_params.pv
#keyword_file_paths = ['path/to/keyword/1', 'path/to/keyword/2', ...]
#sensitivities = [0.5, 0.4, ...]
#handle = Porcupine(library_path, model_file_path, keyword_file_paths=keyword_file_paths, sensitivities=sensitivities)
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=handle.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=handle.frame_length)
def naf():
    pcm = audio_stream.read(handle.frame_length)
    pcm = struct.unpack_from("h" * handle.frame_length, pcm)
    return pcm
try:
    while True:
        pcm=naf()
        keyword_index=handle.process(pcm)
        if keyword_index >= 0:
            understanding.listen()

finally:
    handle.delete()
