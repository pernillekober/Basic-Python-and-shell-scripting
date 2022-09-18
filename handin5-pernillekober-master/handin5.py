# Ex 1: 
def wordfile_to_list(filename):
    '''given a file with a single word at each line, return a list of words in the file'''
    file = open(filename, "r")
    word_list = file.readlines()
       
    
    word_list_stripped = []
    for word in word_list:
        word_list_stripped.append(word.strip('\n'))
        
    file.close() 
    return word_list_stripped


def wordfile_differences_linear_search(filename1, filename2):
    '''Given two word files returns list of words that are in filename1 but not in filename2.'''
    file1_list = wordfile_to_list(filename1)
    file2_list = wordfile_to_list(filename2)
    diff_file1_file2 = []
    
    for word in file1_list:
        if word not in file2_list:
            diff_file1_file2.append(word)
            
    return diff_file1_file2


def binary_search(sorted_list, element):
    """Search for element in list using binary search.
       Assumes sorted list"""
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end - index_start) // 2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current + 1
    return False


def wordfile_differences_binary_search(filename1, filename2):
    '''Uses binary_search function to ompare elements in two lists and return a list of words in 
    the first list and not in the second '''
    file1_list_sorted = wordfile_to_list(filename1)
    file2_list_sorted = sorted(wordfile_to_list(filename2))
    diff_file1_file2 = []   
    for word in file1_list_sorted:
        is_found = binary_search(file2_list_sorted, word)
        if not is_found: 
            diff_file1_file2.append(word)
        
    return diff_file1_file2


def wordfile_to_dict(filename):
    '''given a file with a single word at each line, return a list of words in the file'''
    file = open(filename, "r")
    word_dictionary = {}
    for word in file:
        (key, val) = (word.strip('\n'), None)
        word_dictionary[key] = val
    file.close() 
    
    return word_dictionary

    
#Ex 7:    
def wordfile_differences_dict_search(filename1, filename2):
    ''' Takes two files and creates a list and dictionary. For every word in list 
    searches through the dictionary and returns a list of words in the first file 
    that is not found in the second file '''
    file1_list = wordfile_to_list(filename1)
    file2_dict = wordfile_to_dict(filename2)
    diff_file1_file2 = []
    
    for word in file1_list:
        if word not in file2_dict: 
            diff_file1_file2.append(word)
    
    return diff_file1_file2
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    