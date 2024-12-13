# PROGRAMMER: Mohanad Elemary 
# DATE CREATED: 14/11/2024                                
# REVISED DATE: 13/12/2024

from classifier import classifier 
import os

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. 

    The format includes putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.

    Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    

    
    for key in results_dic:
    
        file_path = os.path.join(images_dir, key)
        classifier_label = classifier(file_path, model)
        results_dic[key].append(classifier_label)

        if results_dic[key][0] in results_dic[key][1]:
          results_dic[key].append(1)
          results_dic[key][1] = results_dic[key][0]
        else:
          results_dic[key].append(0)

    
    return None 