## Machine Condition Prediction

### Objective
Create a notebook/program that can pre-process machine sounds, then classify the sounds as either being normal, or from one of the anomalous categories.

### Dataset

MIMII Machine Sound Dataset
https://zenodo.org/record/3384388

### TODO:

1. Write pre-processing code using basic signal processsing techniques
- determine if better spectrograms can be created, these ones seem to be
overly sparse
- melceptrum coefficient plots? check video series and presentation

2. Apply basic resnet to classify each spectral image
- get more pretraining data, from healthy machines?
- 
- possibly move to resnet 80 or densnet 
