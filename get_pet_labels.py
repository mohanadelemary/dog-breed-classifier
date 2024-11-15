#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Mohanad Elemary
# DATE CREATED: 14/11/2024                              
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import re

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    results_dic = {}
    image_labels = []
    #read image_dir and create a list of all the file Names
    image_list = listdir(image_dir)

    print("\nPrints 10 filenames from folder")
    for i in range(min(10, len(image_list))):
        print("{:2d} file: {:>25}".format(i + 1, image_list[i]) )


    for image_name in image_list:
        image_label = image_name.split('.')[0]
        image_label = re.sub(r'[^a-zA-Z]+', ' ', image_label).strip().lower()
        image_labels.append(image_label)

    print("\nPrints 10 image labels from folder")
    for i in range(min(10, len(image_labels))):
        print("{:2d} file: {:>25}".format(i + 1, image_labels[i]) )

    for i, image_label in enumerate(image_labels):
      if image_labels[i] not in results_dic:
          results_dic[image_list[i]] = [image_label]
      else:
          print(f"{image_list[i]} already exists in results dictionary")

    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
      print("Filename=", key, "   Pet Label=", results_dic[key][0])

    return results_dic
