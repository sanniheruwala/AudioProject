from pydub import AudioSegment
from pydub.playback import play

def audioConvert(src_path, dest_path, dest_type):
    audio = readAudio(src_path)
    audio.export(dest_path + "/output." + dest_type, format=dest_type)

def readAudio(path):
    type = piano_path[-3:]
    print("Audio type : " + type)
    audio = AudioSegment.from_file(path, type)
    return audio

def fadeEffect(audio):
    length = len(audio)
    fade_time = int(length * 0.1)
    faded = audio.fade_in(fade_time).fade_out(fade_time)
    return faded

def increaseBitRate(audio, rate):
    return audio.low_pass_filter(rate)

def overlayAudio(audio1, audio2):
    return audio1.overlay(audio2)

def saveFile(audio, dest_path):
    audio.export(dest_path)

def trimAudio(audio,start,end):
    return audio[start:end]

#Give your mp3 file input path and output path for audio to merge.
piano_path = 'Resources/piano.mp3'
guitar_path = 'Resources/guitar.mp3'
output_path = '/Users/sheruwala/Desktop/out.mp3'

#Read file and add effects to it.
audio_guitar = readAudio(guitar_path)
audio_piano = readAudio(piano_path)
faded_guitar = fadeEffect(audio_guitar)

#Mix two audio
mixed = increaseBitRate(overlayAudio(faded_guitar, audio_piano), 2000)

#Save output
saveFile(mixed, output_path)

#Play it in IDE
play(mixed[-10000:])
