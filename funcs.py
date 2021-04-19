from mutagen.wave import WAVE
import pydub
from pydub.silence import split_on_silence
from pydub import AudioSegment
import os 

count=0
def inc():
    global count
    count = count + 1


#file_length 
def audio_length(aud_file):
    audio = WAVE(aud_file)
    length = int(audio.info.length)
    print(length)
#file_size
def audio_size(aud_file):
    file_stats = os.stat(aud_file)
    size = f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}'
    print (size)
    
#listfiles and rename
def rename_files(files):
    for f in files:
        f_name = os.path.splitext(f)
        f_name = "Slicing - "+str(count)
        inc()
        new_name = '{}'.format(f_name)
        os.rename(f,new_name)
        print(f)
        
#split audio files of each 20 minutes
#def split_parts_mins():