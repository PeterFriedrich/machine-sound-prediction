""" This is a script to take each MIMII dataset
file, make a spectrogram of it, and save it as a png """

# imports
from scipy.io import wavfile
import scipy.io as sio

from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt

import sys
import os

# test names
#wav_fname = "./data/file_example_WAV_1MG.wav"
#image_fname = "test_spectrogram"


def main():
    if len(sys.argv) < 2:
        print("use: python script.py <start file name> <end file name> <wav_folder> <destination folder>")
        return 0

    # extract the cli args
    end_name = sys.argv[1]
    wav_folder = sys.argv[2]
    dest_folder = sys.argv[3] + '/'
     
    # get file count
    _, _, files = next(os.walk('./data/' + wav_folder))
    file_count = len(files)

    # make the file to save stuff in
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
        print("Directory", dest_folder, "was created")
    else:
        print("Directory", dest_folder, "already exists")

    # go through the folder and apply transform/save func
    for wav_file in files:
            image_fname = "./" + dest_folder + wav_file
            make_save_spectro(wav_file, image_fname)
            if i % 50 == 0: # progress
                print(f"finished {wav_file}, last is {files[-1]}.", end='\r', flush=True)

    print("Finished spectrogram conversion.")

def make_save_spectro(wav_fname, image_fname): 
    """ inputs:
    wav_fname: string, wav filename
    image_fname: string, png filename
    Makes a spectrogram from an incoming wav file, and 
    saves it as a png named image_fname
    """
    # extract info
    samplerate, data = sio.wavfile.read(wav_fname) # problem here?
    length = data.shape[0] / samplerate # sample/sample_rate = time

    # make spectrogram
    freqs, time_segs, spectro_array = signal.spectrogram(data[:, 0], samplerate)
    plt.figure()
    # need to remove tick marks and border
    #plt.pcolormesh(time_segs, freqs, spectro_array)
    plt.imsave(image_fname + ".png", spectro_array, format="png", cmap=None)

if __name__ == "__main__":
    main()

