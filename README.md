## Machine Condition Prediction

### Objective
Create a notebook/program that can pre-process machine sounds, then classify the sounds as either being normal, or from one of the anomalous categories.

### Dataset

MIMII Machine Sound Dataset
https://zenodo.org/record/3384388

Original Paper: https://arxiv.org/pdf/1909.09347.pdf

Original baseline repo: https://github.com/MIMII-hitachi/mimii_baseline/

16khz sampling rate, 16 bits per sample, 8 channels.

Switching over to valve for first 
First dataset is 0dB

### TODO:

- *Apparently* this paper says detailed spectrograms work better than MFCC
on this method (basic visual comparisons seem to agree), and combining them doesn't yield improvements.
- Apply basic resnet to classify each spectral image
- Grab more pre-training data, find other datasets, or places to scrape from. 
- Move to mobilnet etc.
- testing keys
