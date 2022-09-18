import handin6 as h6
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

data = h6.read_mnist_csv("mnist_test_200.csv")
print("ex 1 works")
#print("mnist shape: {}".format(data.shape))

grouped_numpy_list = h6.group_by_label(data)
print("ex 2 works")
#print("grouped numpy list length: {}".format(len(grouped_numpy_list)))
#print("grouped numpy list index 9 length: {}".format(len(grouped_numpy_list[9])))
#print("grouped numpy list index 9 [0] length: {}".format(len(grouped_numpy_list[9][0])))
#print("grouped numpy list index 9 type: {}".format(type(grouped_numpy_list[9])))    


reshaped_list = h6.convert_to_images(grouped_numpy_list)
print("ex 3 works")



#exercise4 = h6.draw_image(reshaped_list[0][0])
#plt.show()
print("ex 4 works")


exercise5 = h6.draw_image_row(reshaped_list)

