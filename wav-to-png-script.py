""" This is a script to take each MIMII dataset
file, make a spectrogram of it, and save it as a png """

# imports
from scipy.io import wavfile
import scipy.io as sio

from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt

wav_fname = "./data/file_example_WAV_1MG.wav"
image_fname = "test_spectrogram"

def make_save_spectro(wav_fname, image_fname): 
    """ inputs:
    wav_fname: string, wav filename
    image_fname: string, png filename
    Makes a spectrogram from an incoming wav file, and 
    saves it as a png named image_fname
    """
    # extract info
    samplerate, data = sio.wavfile.read(wav_fname)
    length = data.shape[0] / samplerate # sample/sample_rate = time

    # make spectrogram
    freqs, time_segs, spectro_array = signal.spectrogram(data[:, 0], samplerate)
    plt.figure()
    plt.pcolormesh(time_segs, freqs, spectro_array)
    plt.savefig(image_fname)

make_save_spectro(wav_fname, image_fname)
