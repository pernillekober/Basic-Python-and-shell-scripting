from statistics import mean
import numpy as np

#Opgave 1
def read_data(filename):
    '''Takes txt input (two columns á 8 char) and creates a list of lists 
    containing row input and converts content to floats'''
    data = open(filename, "r")
    content_rows = data.readlines()
    for i in range(len(content_rows)):
        x, y = float(content_rows[i][:8]), float(content_rows[i][9:17])
        content_rows[i] = [x,y]
    return content_rows

list_of_rows = read_data('experimental_results.txt')
#print(list_of_rows)    


#Opgave 2
def calc_averages(list_of_lists):
    ''' takes list of list of tuple of floats, and takes the average of values within each column'''
    col1_list = []
    col2_list = []
    for i in range(len(list_of_lists)):
         col1_list.append(list_of_rows[i][0])
         col2_list.append(list_of_rows[i][1]) 
    return mean(col1_list), mean(col2_list)
    
    
col1_avg, col2_avg = calc_averages(list_of_rows)
#print(col1_avg, col2_avg)

#Opgave 3
def transpose_data(list_input):
    '''uses numpy library to transpose given list of lists input andback to nested list'''
    list_to_np = np.array(list_input)
    np_transposed = list_to_np.T
    np_transposed_to_list = np_transposed.tolist()
    return np_transposed_to_list  

list_of_columns = transpose_data(list_of_rows)
#print(list_of_columns) 