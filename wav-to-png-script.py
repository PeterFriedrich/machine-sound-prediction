""" This is a script to take each MIMII dataset
file from specified folder, make a spectrogram of it, and save it as a png
in a destination folder.

note: The chunk error simply means unsupported metadata at the end of the 
wav files(possibly not present after librosa update?)"""

# imports
from scipy.io import wavfile
import scipy.io as sio

from scipy import signal
from scipy.fft import fftshift
from PIL import Image

import librosa
import librosa.display
import matplotlib.pyplot as plt

import sys
import os


def main():
    if len(sys.argv) < 2: # test cli args
        print("use: python script.py <wav_folder> <destination folder> <id_num>")
        return 0

    # extract the cli args
    wav_folder = sys.argv[1]
    dest_folder = sys.argv[2] 
     
    # get file count
    _, _, files = next(os.walk(wav_folder))
    file_count = len(files)

    # check or make the destination folder
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
        print("Directory", dest_folder, "was created")
    else:
        print("Directory", dest_folder, "already exists")
    
    counter = 0
    # go through the folder and apply transform/save func
    for wav_file in files:
            image_fname = dest_folder + "/" + 'spectro_' + wav_file[:-4] + wav_folder[12:17]
            make_save_spectro(wav_folder + '/' + wav_file, image_fname)
            counter += 1
            print(f"finished {counter}, file_count is {file_count}.", end='\r', flush=True)

    print("Finished spectrogram conversion.")

def make_save_spectro(wav_fname, image_fname):
    """ inputs:
    wav_fname: string, wav filename
    image_fname: string, png filename
    spectro_func(TODO): string, options: normal, log, mfcc 

    Makes a spectrogram from an incoming wav file, and 
    saves it as a png named image_fname
    """
    # extract info
    y, sr = librosa.load(wav_fname)

    # create spectro figure (currently mfcc)
    fig = plt.figure(figsize=(4,4))
    plt.axis('off')
    spectro_data = librosa.feature.mfcc(y=y, sr=sr)
    librosa.display.specshow(data=spectro_data, sr=sr, x_axis="time",
            cmap="plasma")

    # save
    fig.savefig(image_fname)
    plt.close()

def make_save_spectro_old(wav_fname, image_fname): 
    """ 
    DEPRECATED
    inputs:
    wav_fname: string, wav filename
    image_fname: string, png filename
    Makes a spectrogram from an incoming wav file, and 
    saves it as a png named image_fname
    """
    # extract info
    samplerate, data = sio.wavfile.read(wav_fname) # problem here?
    length = data.shape[0] / samplerate # sample/sample_rate = time

    # make spectrogram, needs to be square
    freqs, time_segs, spectro_array = signal.spectrogram(data[:, 0], samplerate)
    # save plot no whitespace 
    plt.figure(figsize=(6,6))
    fig = plt.pcolormesh(time_segs, freqs, spectro_array)
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig(image_fname, bbox_inches='tight', pad_inches = 0)
    plt.close()

    # reopen and crop with PIL
    im = Image.open(image_fname + '.png')
    width, height = im.size
    # left, top, right, bottom, from top left
    im1 = im.crop((0, 0, width - 3, height))
    im1.save(image_fname + '.png')
    im.close()
    im1.close()



if __name__ == "__main__":
    main()

