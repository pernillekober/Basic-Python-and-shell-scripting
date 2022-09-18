# Handin 6

<table>
  <tr>
    <td>Due date</td>
    <td>Tuesday, Oct 20</td>
  </tr>
  <tr>
    <td>Format</td>
    <td>Write your Python code in the handin6.py and handin6_test.py files. Since we are now using functions, you no longer have to separate your python code into blocks separated by whitespace.

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

In this handin, we will experiment with a classic Machine Learning data set, the MNIST dataset of handwritten digits (see https://en.wikipedia.org/wiki/MNIST_database for details). The full dataset has 70,000 images - but for convenience I have reduced it to only 200 images, and included it as a CSV file in the repository (the original full size csv file can be found here: https://pjreddie.com/projects/mnist-in-csv/)

1. In the module file called <code>handin6.py</code>, create a function called <code>read_mnist_csv</code>, which takes a single argument called <code>filename</code>. This function should read the file, and return a numpy array. Note that the first line in the .csv file is a header with column names, which you should exclude when reading in the data. Hint: you can use <code>genfromtxt</code> for this task.<br><br>Verify that your function works by calling it from the <code>handin6_test.py</code> file, on the filename <code>mnist_test_200.csv</code>.

2. The database contains examples of all 10 digits. The first column in the dataset specifies which of the digits the row corresponds to. Write a function called <code>group_by_label</code> that takes a numpy array as argument, and returns a list of numpy arrays, grouped by which digit it corresponds to. The output should thus be a list with 10 elements, where the first element is a numpy array corresponding to all the rows in the original array where the first column is 0. Hint: The <code>np.where</code> function can give you all the indices where a numpy array has a particular value. So, for instance, the following will return all elements in an array x where the values are zero: <pre><code>indices = np.where(x == 0)
print(x[indices])</code></pre>Again, verify that it works by calling the <code>group_by_label</code> function from your <code>handin6_test.py</code> file, using the numpy array from the previous exercise as argument.

3. You might have noticed that the numpy arrays we have been working with have 785 columns. If we remove the first column, we have 784 columns left, which corresponds to 28x28 pixel values. In your <code>handin6.py</code> file, write a function called <code>convert_to_images</code> that takes a list of numpy arrays as input (the one created by the previous exerise), and returns a list with numpy arrays with shape (???, 28, 28), where ??? is the size of the group. Hint: you can use the <code>reshape</code> method in any numpy array to change the shape of an array (while keeping the total number of elements fixed).<br><br>Verify that your function works by calling it from <code>handin6_test.py</code> using the list of grouped numpy arrays from the previous exercise as input.

4. Now let's visualize a digit. In your <code>handin6.py</code> file, write a function called <code>draw_image</code> that takes a 28x28 pixel numpy array group as input, and shows it on screen. You can use matplotlib's <code>imshow</code> function for this purpose. Set the color map (cmap) to gray and remove the axis on the plot.<br><br>Again, check that it is working by calling the <code>draw_image</code> function from the <code>handin6_test.py</code> file, using the first image in the zero-digit group as an example. To visualize it, add a <code>plt.show()</code> to your <code>handin6_test.py</code> (don't put it in the main module, since it will distrupt the testing procedure).

5. Now let's create a visualization containing one of each digit. In your <code>handin6.py</code> file, write a function called <code>draw_image_row</code>, which takes a list of numpy arrays as its input (i.e. the groups from before). Within this function, you can use <code>fig, axs = plt.subplots(<em>rows</em>, <em>columns</em>)</code> function to create a grid of small plots. Since we only want a single row, you can set the first argument to 1, while the second argument of <code>subplots</code> should be the number of groups. The <code>subplots</code> call will create a number of miniplots, which you can access through the <code>axs</code> variable. For instance, to visualize something in the first miniplot, you would write <code>axs[0].imshow(...)</code>. For simplicity, just choose the first image in each group to visualize.<br><br>Call the <code>draw_image_row</code> from your <code>handin6_test.py</code> using the groups list from the exercises above. Verify that you indeed get a row of all 10 digits.

6. Finally, let's calculate the average image for each group. In your <code>handin6.py</code> file, write a function called <code>calc_group_averages</code>, that takes a list of numpy arrays as input, and returns a new list of numpy arrays, where each numpy array is now just a single image, which is an average of all the images in the group. Hint: you will need to use the <code>axis</code> option of <code>np.average</code> like we saw in class. Please make sure that your output images have the shape (1,28,28) rather than just (28,28) - which you can do using the <code>reshape</code> method. This ensures that you can reuse the <code>draw_image_row</code> function to visualize these averaged images.<br><br>From your <code>handin6_test.py</code> file, call the <code>calc_group_averages</code> function using the group list from the previous exercises. Now take the resulting list, and use it to call <code>draw_image_row</code> again - this time to get a row of average images for each digit.

