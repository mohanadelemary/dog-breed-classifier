# PROGRAMMER: MOHANAD ELEMARY
# DATE CREATED: 14/11/2024
# REVISED DATE: 13/12/2024

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    
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
    results_stats_dic - Dictionary that contains the results statistics (either
                        a  percentage or a count) where the key is the statistic's 
                        name (starting with 'pct' for percentage or 'n' for count)
                        and the value is the statistic's value 
    model - Indicates which CNN model architecture will be used by the 
            classifier function to classify the pet images,
            values must be either: resnet, alexnet, vgg (string)
    print_incorrect_dogs - True prints incorrectly classified dog images and 
                            False doesn't print anything(default) (bool)  
    print_incorrect_breed - True prints incorrectly classified dog breeds and 
                            False doesn't print anything(default) (bool) 
    Returns:
            None - simply printing results.
    """    
    
    # Print the summary of results
    print(f"Summary of Results for {model} Model:")
    print("-" * 40)
    print(f"Total Images: {results_stats_dic['n_images']}")
    print(f"Total Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Total Non-Dog Images: {results_stats_dic['n_notdogs_img']}")
    print(f"Total Matches: {results_stats_dic['n_match']}")
    print(f"Correct Dogs: {results_stats_dic['n_correct_dogs']}")
    print(f"Correct Non-Dogs: {results_stats_dic['n_correct_notdogs']}")
    print(f"Correct Breeds: {results_stats_dic['n_correct_breed']}")
    print(f"Percentage of Matches: {results_stats_dic['pct_match']:.2f}%")
    print(f"Percentage of Correct Dogs: {results_stats_dic['pct_correct_dogs']:.2f}%")
    print(f"Percentage of Correct Breeds: {results_stats_dic['pct_correct_breed']:.2f}%")
    print(f"Percentage of Correct Non-Dogs: {results_stats_dic['pct_correct_notdogs']:.2f}%")
    print("-" * 40)

    # Print incorrectly classified dogs if requested
    if print_incorrect_dogs:
        print("Incorrectly Classified Dog Images:")
        print("-" * 40)
        for key in results_dic:
            if results_dic[key][3] == 1 and results_dic[key][4] == 0:
                print(f"Image: {key} - Pet Label: {results_dic[key][0]} - Classifier Label: {results_dic[key][1]}")
        print("-" * 40)

    # Print incorrectly classified breeds if requested
    if print_incorrect_breed:
        print("Incorrectly Classified Dog Breeds:")
        print("-" * 40)
        for key in results_dic:
            if results_dic[key][3] == 1 and results_dic[key][4] == 1:
                if results_dic[key][0] != results_dic[key][1]:
                    print(f"Image: {key} - Pet Label: {results_dic[key][0]} - Classifier Label: {results_dic[key][1]}")
        print("-" * 40)

    return None
