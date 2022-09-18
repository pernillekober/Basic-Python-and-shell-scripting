import numpy as np
import matplotlib.pyplot as plt

def read_mnist_csv(filename):
    '''Ex1: read content of csv file (hence delimiter ',') into numpy array, exclude first line (header)'''
    no_coumn_data = (np.genfromtxt(filename, delimiter=','))[1::]
    
    return no_coumn_data


def group_by_label(nparray):
    '''Ex2: based on the first index in each numpy array, adds array to 
    corresponding index in list, returning a list of numpy arrays'''
    index_grouped_list = []
    sliced_nparray = nparray[:,0:1]    
    
    for i in range(10):
        objects = np.where(sliced_nparray == i)
        index_grouped_list.append(nparray[objects[0]])
        
    return index_grouped_list


def convert_to_images(numpy_list):
    '''Given a list of numpy arrays returns list of numpy arrays of size (???, 28, 28) '''
    new_numpy_list = []
    
    #iterate through list and create a new list element (numpy array with desired shape)
    for list_idx in range(len(numpy_list)):
        shape = list(numpy_list[list_idx].shape)
        new_shape = (shape[0], 28, 28)
        new_list_element = np.full(new_shape, None)
        
        #iterate through list element (numpy array of numpy arrays, reshape to 28x28 and insert)
        for array_idx in range(numpy_list[list_idx].shape[0]):
            reshaped_array = np.reshape(numpy_list[list_idx][array_idx][1:], (28,28))
            new_list_element[array_idx] = reshaped_array
    
        new_numpy_list.append(new_list_element)
    
    
    return new_numpy_list


def draw_image(numpy_array):
    ''' Note: Due to dtype problem, to make imshow work I had to first place the elements into a list of list with object type '''
    new_list = []
    
    for i in range(numpy_array.shape[0]):
        new_container = []
        for j in range(numpy_array.shape[1]):
            x = np.float64(numpy_array[i][j])  
            new_container.append(x)
        new_list.append(new_container)
    
    new_list = np.array(new_list)
    
    #print(len(new_list))
    #print(len(new_list[0]))
    #print(type(new_list))
    #print(new_list.shape)
    
    a = plt.imshow(new_list, cmap="gray")

    return a


def draw_image_row(list_of_numpy):
    '''Note, for-loops due to wrong data type 'float' that were not compatible with imshow.'''
    data = list_of_numpy
    length = len(data)
    idx = -1
    
    fig, axs = plt.subplots(1, length)
    
    for x in data:
        idx += 1
        y = x[0]
        new_list = []
            
        for i in range(y.shape[0]):
            new_container = []    

            for j in range(y.shape[1]):
                float_converted = np.float64(y[i][j])  
                new_container.append(float_converted)
            
            new_list.append(new_container)
        
        new_list = np.array(new_list)
        #print(type(new_list))
        #print(new_list.shape)
        #print(type(new_list[0][0]))
        
        print(idx)
        axs[idx].imshow(new_list, cmap = 'gray')
            
    
    return fig, axs
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    