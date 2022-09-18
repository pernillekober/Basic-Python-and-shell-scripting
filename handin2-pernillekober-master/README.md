# Handin 2

<table>
  <tr>
    <td>Due date</td>
    <td>Tuesday, Sept 15 </td>
  </tr>
  <tr>
    <td>Format</td>
    <td>Write your Python code in the handin1.py file. Since we are now using functions, you no longer have to separate your python code into blocks separated by whitespace. When you are ready to submit, commit and push your code back to github as described in the "Github, git and the weekly hand-ins" page on Absalon.</td>
  </tr>
  <tr>
    <td>Setup</td>
    <td><strong>Please make sure that your name and email address have been set up correctly</strong> for <code>git</code>. This is very important, since otherwise you will not receive emails about the correctness of your code (and we cannot see who is who). See the "Github, git and the weekly hand-ins" page for details.</td>
  </tr> 
  <tr>
    <td>Other comments</td>
    <td>As usual, the hand-in covers the topics covered in this week of the course. This means that there might be a few things that you won't be able to solve until after the Friday lecture. </td>
  </tr>
</table>


1. Create a function called <code>read_data</code>, that takes a filename as argument. The function should open the file, and read its contents into a list of list of floats, where the outer list corresponds to the lines of the file, and the inner lists correspond to the columns (that is, convert the strings of each line to a list of two numeric values, and append them to an outer list). The function should return this list. Test the function by calling it on the <code>experimental_results.txt</code> file like this:

<pre><code>list_of_rows = read_data('experimental_results.txt')
print(list_of_rows)
</code></pre>

2. Write a function called <code>calc_averages</code> that takes a list of list of floats as input, and calculates the average value for each column by iterating over the rows. The function should return these two values. Test the function by calling it like this: 

<pre><code>col1_avg, col2_avg = calc_averages(list_of_rows)
print(col1_avg, col2_avg)
</code></pre>

3. Write a function called <code>transpose_data</code> that turns the list of lists around so that it becomes a list of columns, rather than a list of rows. This means that the outer list now has two elements each containing a list of all the values in the corresponding column. In other words, if I want to access the 26th value in the 2nd column, I would now index with [1][25] instead of [25][1].
Hint: Note that these two nested lists are just two different ways of representing the same table of data. Here is a sketch of the two variants:

<p align="center">
   <img src="https://wouterboomsma.github.io/ppds2020/images/list_list_transpose.svg">
</p>

Test the function by calling it like this:

<pre><code>list_of_columns = transpose_data(list_of_rows)
print(list_of_columns)    
</code></pre>

**Remember to add doc-strings to all your functions! If you forget, the tests will not pass.**