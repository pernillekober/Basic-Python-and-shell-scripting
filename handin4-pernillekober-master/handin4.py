import sys
import re
# Ex 1: 
    
def read_fasta(fasta_file):
    ''' reads fasta file and returns dictionary with protei name and amino acid sequence. '''
    file = open(fasta_file, "r")
    file_content = file.readlines()
    keys_list = []
    sequences_list = []
    sequence = ""
    counter = 0
    
    for line in file_content:
        counter += 1
        line = line.rstrip()
        if line.startswith(">"):
            key = line[1:]
            keys_list.append(key)
            if counter > 1:
                sequences_list.append(sequence)
                sequence = ""
        else:
            sequence += line
            if counter == len(file_content):
                sequences_list.append(sequence)
    
    file_dictionary = dict(zip(keys_list, sequences_list))
    file.close()
    return file_dictionary


# Ex 3: create a search function for the dictionary
def find_prot(dictionary, search_variable):
    '''Search for a given key in a given input dictionary, return related value from dictionary or
    None + error message if it does not exists in dictionary'''
    input_dictionary = dictionary 
    search_argument = search_variable

    if search_argument in input_dictionary:
        return input_dictionary[search_argument]
    else:
        print("Error: protein name %s not found" % (search_argument))
        return None


def find_prot2(dictionary, re_search):
    '''Search for a given key in a given input dictionary, return related value from dictionary or
    None + error message if it does not exists in dictionary'''
    input_dictionary = dictionary 
    search_expression = re_search
    matching_keys = []
    keys = input_dictionary.keys()
    
    for key in keys:
        if re.match(search_expression, key) is not None:
            matching_keys.append(key)
    return matching_keys
        