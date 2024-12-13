# Dog Breed Classifier

## Introduction
This project implements a deep learning-based solution for classifying dog breeds. Using pre-trained models like ResNet, AlexNet, and VGG, the classifier is trained to identify the breed of a dog from input images. The goal is to provide an accurate and efficient way of recognizing dog breeds in images.

## Requirements
- Python 3.6+
- Libraries:
  - torch
  - torchvision
  - PIL
  - numpy

To install dependencies, run:

`pip install -r requirements.txt`


## Architecture
- Python Files:
    - check_images.py:
        - This the main script file to run the program.
        - Handles loading pet images from a specified directory.
        - Takes command-line arguments to specify which model to use and which file to load breed names from.

    - get_input_args.py:
        - Parses and processes the command input arguments to run the program.

    - get_pet_labels.py:
        - Processes the image directory and reads the image filenames as labels for the models evaluation later.  

    - classifier.py:
        - Contains the logic for classifying images using pre-trained models (ResNet, AlexNet, VGG).
        - It applies image transformations and uses the model to predict dog breeds.

    - classify_images.py:
        - Calls the model functions from classifier.py
        - Appends the model predictions to the results dictionary, and appends the match results in binary format.
    
    - adjust_results4_isadog.py:
        - Determines if predictions correctly classify an image as a dog species or not and appends this in binary 
          format to the results dictionary.

    - calculates_results_stats.py:
        - Calculates various statistics on the model predictions to express how well it performs in predicting the 
          the image label and if it's a dog.
    
    - print_results.py:
        - Prints final statistics and summary for the program.

    - get_pet_labels.py:
        - Extracts breed labels from the file names of the pet images.
        - It generates a dictionary mapping images to their respective breed names.

    - calculates_results_stats.py:
        - Computes performance metrics for the model.
        - Evaluates the classification results and outputs statistics like accuracy.

## Input Files and Directories:
  - pet_images/: Contains the input images to be classified. These should be placed in this directory.
  - dognames.txt: A file containing the list of dog breed names.
  - imagenet1000_clsid_to_human.txt: A file that maps ImageNet class IDs to breed names.

### Shell Script:
  - run_models_batch.sh: A shell script to run classification on all images using multiple model architectures in batch.

### Output Files:
  - The classification results are saved to text files (e.g., alexnet_pet-images.txt), each containing the predicted breed for each image.


# How to Run:

  - Clone repository and install dependencies:

`pip install -r requirements.txt`

  - Run the image classification: Use the following command to classify pet images using a specific model (e.g., alexnet):

`python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt`

  - You can also run batch classification: Run the batch script to classify images with multiple models:

`sh run_models_batch.sh`

  - You can upload your own images of dogs and other objects to the directory and test the program.
  - Note: This program will only work with the following model architecture inputs: resnet, alexnet, vgg.

## Conclusion
This repository provides a practical solution for classifying dog breeds in images using deep learning models. It’s designed to be easy to use with flexibility for choosing different model architectures.
