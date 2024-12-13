# PROGRAMMER: MOHANAD ELEMARY
# DATE CREATED: 14/11/2024                                 
# REVISED DATE: 13/12/2024

 
def calculates_results_stats(results_dic):

        """
        Calculates statistics of the results of the program run using classifier's model 
        architecture to classifying pet images. Then puts the results statistics in a 
        dictionary (results_stats_dic) so that it's returned for printing as to help
        the user to determine the 'best' model for classifying images. Note that 
        the statistics calculated as the results are either percentages or counts.
        Parameters:
        results_dic - Dictionary with key as image filename and value as a List 
                (index)idx 0 = pet image label (string)
                        idx 1 = classifier label (string)
                        idx 2 = 1/0 (int)  where 1 = match between pet image and 
                                classifer labels and 0 = no match between labels
                        idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                                0 = pet Image 'is-NOT-a' dog. 
                        idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                                'as-a' dog and 0 = Classifier classifies image  
                                'as-NOT-a' dog.
        Returns:
        results_stats_dic - Dictionary that contains the results statistics (either
                        a percentage or a count) where the key is the statistic's 
                        name (starting with 'pct' for percentage or 'n' for count)
                        and the value is the statistic's value. See comments above
                        and the previous topic Calculating Results in the class for details
                        on how to calculate the counts and statistics.
        """        

        
        
        # run calculation to get the following
                # n_images - number of images
                        # len(results_dic)
        n_images = len(results_dic)  

                # n_dogs_img - number of dog images
                        # sum of results[key][3]
        n_dogs_img = sum(1 for key in results_dic if results_dic[key][3] == 1)  # Number of dog images

                # n_notdogs_img - number of NON-dog images
                        # n_images - n_dogs_img
        n_notdogs_img = n_images - n_dogs_img  # Number of non-dog images

                # n_match - number of matches between pet & classifier labels
                        # sum of results[key][2]
        n_match = sum(1 for key in results_dic if results_dic[key][2] == 1)  # Number of matches between pet & classifier labels

                # n_correct_dogs - number of correctly classified dog images
                        # len(results[key][3]=1 AND results[key][4]=1)
        n_correct_dogs = sum(1 for key in results_dic if results_dic[key][3] == 1 and results_dic[key][4] == 1)

                # n_correct_notdogs - number of correctly classified NON-dog images
                        # n_images - n_correct_dogs
        n_correct_notdogs = n_images - n_correct_dogs  # n_notdogs_img - n_correct_dogs

                # n_correct_breed - number of correctly classified dog breeds
                        # len(results[key][2]=1 AND results[key][3]=1)

        n_correct_breed = sum(1 for key in results_dic if results_dic[key][2] == 1 and results_dic[key][3] == 1)

                # pct_match - percentage of correct matches
                        # (n_match/n_images)*100
        pct_match = (n_match / n_images) * 100 if n_images > 0 else 0  # Percentage of correct matches


                # pct_correct_dogs - percentage of correctly classified dogs
                        # (n_correct_dogs/n_dogs_img)*100
        pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100 if n_dogs_img > 0 else 0  # Percentage of correctly classified dogs


                # pct_correct_breed - percentage of correctly classified dog breeds
                        # (n_correct_breed/n_dogs_img)*100
        pct_correct_breed = (n_correct_breed / n_dogs_img) * 100 if n_dogs_img > 0 else 0  # Percentage of correctly classified dog breeds


                # pct_correct_notdogs - percentage of correctly classified NON-dogs
                        # (n_correct_notdogs/n_notdogs_img)*100
        pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100 if n_notdogs_img > 0 else 0  # Percentage of correctly classified non-dogs

        # Put it all in a dictionary

        results_stats_dic = {
        'n_images': n_images,
        'n_dogs_img': n_dogs_img,
        'n_notdogs_img': n_notdogs_img,
        'n_match': n_match,
        'n_correct_dogs': n_correct_dogs,
        'n_correct_notdogs': n_correct_notdogs,
        'n_correct_breed': n_correct_breed,
        'pct_match': pct_match,
        'pct_correct_dogs': pct_correct_dogs,
        'pct_correct_breed': pct_correct_breed,
        'pct_correct_notdogs': pct_correct_notdogs
        }       

        # OUTPUT: results_stats_dic
    
    
    
        return results_stats_dic
