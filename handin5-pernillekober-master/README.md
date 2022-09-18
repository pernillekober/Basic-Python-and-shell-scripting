# Handin 5

<table>
  <tr>
    <td>Due date</td>
    <td>Tuesday, Oct 6</td>
  </tr>
  <tr>
    <td>Format</td>
    <td>Unix part: Put the relevant commands into the handin5.sh file. The individual exercises should be separated by empty lines (see the "Github, git and the weekly hand-ins" page on Absalon for an example).

Python part: Write your Python code in the handin5.py, handin5_test1.py, handin5_test2.py, and handin5_test3.py  files. Since we are now using functions, you no longer have to separate your python code into blocks separated by whitespace.

When you are ready to submit, commit and push your code back to github as described in the "Github, git and the weekly hand-ins" page on Absalon.</td>
  </tr>
  <tr>
    <td>Setup</td>
    <td><strong>Please make sure that your name and email address have been set up correctly</strong> for <code>git</code>. This is very important, since otherwise you will not receive emails about the correctness of your code (and we cannot see who is who). See the <a href="https://absalon.ku.dk/courses/35880/pages/github-git-and-the-weekly-hand-ins?module_item_id=801269">Github, git and the weekly hand-ins</a> page for details.
  </tr> 
  <tr>
    <td>Other comments</td>
    <td>As usual, the hand-in covers the topics covered in this week of the course. This means that there might be a few things that you won't be able to solve until after the Friday lecture. </td>
  </tr>
</table>

This handin is meant to illustrate that it is important to think carefully about how to represent your data. The speed by which a task is solved is very dependent on the way the data is organised. The exercise looks very long, but most of the code that you need to write are minor modifications of earlier hand-ins.

We are going to create a program that compares the <code>british-english</code> and <code>american-english</code> files (or files like it) and calculates how many entries are different between the two files. The files are included in this repository.

One way of comparing the files is to put the words from the two files into two seperate lists, and then run through a loop where you check if each word in one file is present in the other. We will see that there are more and less efficient ways to do this, and that it can matter a lot which choice you make. In this exercise we will try three different representations of  the data in the second file, and thereby three different ways of looking up the names: linear search, binary search, and using dictionaries.

We have provided two small test files so you can test whether your methods work before actually running on the huge files. These files are called <code>british-english-test</code> and <code>american-english-test</code>, and are also included in this repository.

## Python part

1. In the module file called <code>handin5.py</code>, create a function called <code>wordfile_to_list</code>, which takes a single argument called <code>filename</code>. This function should read the file, and return a list with words. You can assume that each line in the file only contains a single word. Please remember to the remove newlines at the end of each line. 

2. Add a function to the <code>handin5</code> module called <code>wordfile_differences_linear_search</code>, which takes two filenames as arguments, and calls <code>wordfile_to_list</code> to create a list for each of these files. The function should contain a loop that for each word in the first list looks through the second list to see if there is a match. It should return a list of words that are in the first file but not in the second file.

3. In the file called <code>handin5_test1.py</code>, call the <code>wordfile_differences_linear_search</code> on the input files, using <code>british-english</code> as file1 and <code>american-english</code> as file2 (it is ok to test it on the test files first, but please switch to the full files before submitting), and saves the result in a variable called <code>differences</code>. Python has built-in functionality for measuring execution times within a programme, using the <code>timeit</code> module, which can be used like this: 

<pre><code>
import timeit
start_time = timeit.default_timer()
# write code you want to measure execution time for here
time_spent = timeit.default_timer() - start_time</code></pre>

Use this technique to measure how long it takes to call the <code>wordfile_differences_linear_search</code> function, and save the result in a variable called <code>time_spent</code>, as in the example. Hint: you are of course very welcome to print the <code>time_spent</code> and <code>differences</code> out to screen so you can check your results, although this output will not be used by the code-checker (we check the variables directly).

4. It is much more efficient to find elements in a sorted list. One way of doing this is by using a method called binary search.  Basically, binary search excludes half of the remaining list at every step of the search and will therefore only look at much fewer elements than the linear search above. To help you out, here is an implementation of a binary search function in Python:

<pre><code>
def binary_search(sorted_list, element):
    """Search for element in list using binary search.
       Assumes sorted list"""
    # Current active list runs from index_start up to
    # but not including index_end
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end-index_start)//2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current+1
    return False</code></pre>

Add this function to the <code>handin5</code> module, and add another function called <code>wordfile_differences_binary_search</code>. Again, this function should take two filename arguments, and return a list of the words that appear in the first file, but not in the second. This difference is that this time, you should call the <code>binary_search</code> function for each element in the outer loop.

5. The <code>handin5_test2.py</code> file should be similar to <code>handin5_test1.py</code>, but now instead call the <code>wordfile_differences_binary_search</code> on the input files, and saves the result in a variable called differences. Again, use the <code>timeit</code> module to measure the time it takes to calculate the differences, and save this result in a variable called <code>time_spent</code>.

6. Finally, we will test the speed of lookups in a Python dictionary. Create a function called <code>wordfile_to_dict</code> in the <code>handin5</code> module. This function should be identical to <code>wordfile_to_list</code>, but save the results as keys in a dictionary rather than in a list (you can choose whatever you like for the values - for instance None).

7. Add a function to the <code>handin5</code> module called <code>wordfile_differences_dict_search</code>, which takes two filenames as arguments, and calls <code>wordfile_to_list</code> on the first file and <code>wordfile_to_dict</code> on the second file. The function should contain a loop that for each word in the list looks in the dictionary to see if there is a match. It should return a list of words that are in the first file but not in the second file.

8. The test code in <code>handin5_test3.py</code> should be similar to the two others, but now call the <code>wordfile_differences_dict_search</code> on the input files. Again you should save the result in a variable called <code>differences</code> and the <code>timeit</code> module to measure the time it takes to do the calculation, and save this result in a variable called <code>time_spent</code>.

## Unix part

In the Unix part, we will now simulate the scenario that I talked about in class: that we wish to login to a remote server to run our (heavy) Python scripts. The strategy is: a) make sure you have a working version of the Python part above, and that you have pushed it to the server, b) log into the ppds-diku server, c) on the the server, use git clone https://github.com/UCPH-PPDS2020/handin5-??? to get a copy of your Python code (replacing ??? with your Github username). Then complete the following assignments from within the new handin5-??? directory that you have created (note that the only thing you should put in the <code>handin5.sh</code> file are the commands you need to solve the questions below, not the ssh, git clone etc.): 

1. The unix command time can measure the execution time of a process. Use it to measure the execution time of <code>handin5_test1.py</code>.

2. Use the <code>time</code> command to measure the execution time of <code>handin5_test2.py</code>.

3. Use the <code>time</code> command to measure the execution time of <code>handin5_test3.py</code>.

4. The <code>diff</code> command can be used to solve the same task as our Python script above. Write a command that does this. The command should just print out the number of differences (i.e. the number of words in file1 that do not occur in file2). 

5. Repeat the previous question, but now use the <code>time</code> command to measure how fast it is.


