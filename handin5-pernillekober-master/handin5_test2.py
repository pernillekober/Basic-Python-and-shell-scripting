import handin5 as h5
import time
import timeit

#Ex 5:
start_time = timeit.default_timer()
differences = h5.wordfile_differences_binary_search("british-english", "american-english")
time_spent = timeit.default_timer() - start_time
#print("Length of difference list: {}".format(len(differences)))
#print("Time spent on binary search: {}".format(time_spent))

