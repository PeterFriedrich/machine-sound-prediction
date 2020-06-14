""" This is a script to take each MIMII dataset
file, make a spectrogram of it, and save it as a png

note: The chunk error simply means unsupported metadata at the end of the 
wav files"""

# imports
from scipy.io import wavfile
import scipy.io as sio

from scipy import signal
from scipy.fft import fftshift
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

    # go through the folder and apply transform/save func
    for wav_file in files:
            image_fname = dest_folder + "/" + 'spectro_' + wav_file[:-4] + wav_folder[12:17]
            make_save_spectro(wav_folder + '/' + wav_file, image_fname)
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

    # make spectrogram, needs to be square
    freqs, time_segs, spectro_array = signal.spectrogram(data[:, 0], samplerate)
    plt.figure()
    # save image only
    plt.imsave(image_fname + ".png", spectro_array, format="png", cmap=None)
    plt.close()

if __name__ == "__main__":
    main()

