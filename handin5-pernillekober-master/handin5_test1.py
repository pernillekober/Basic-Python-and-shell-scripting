import handin5 as h5
import timeit

#Ex 3:
start_time = timeit.default_timer()
differences = h5.wordfile_differences_linear_search("british-english", "american-english")
time_spent = timeit.default_timer() - start_time
#print("Length of difference list: {}".format(len(differences)))
#print("Time spent on linear search: {}".format(time_spent))

