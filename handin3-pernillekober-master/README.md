# Handin 3

<table>
  <tr>
    <td>Due date</td>
    <td>Tuesday, Sept 22</td>
  </tr>
  <tr>
    <td>Format</td>
    <td>Unix part: Put the relevant commands into the handin3.sh file. The individual exercises should be separated by empty lines (see the "Github, git and the weekly hand-ins" page on Absalon for an example).

Python part: Write your Python code in the handin3.py file. Since we are now using functions, you no longer have to separate your python code into blocks separated by whitespace.

When you are ready to submit, commit and push your code back to github as described in the "Github, git and the weekly hand-ins" page on Absalon.</td>
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

## Unix

Please write up the Unix commands for each of the questions below and put them in the handin3.sh file. We strongly recommend logging in to the <code>ppds-diku</code> server to try out the commands, where we know that everything should work as expected.

1. Create a directory called "handin3" in your current directory.
2. Inside this directory, create a directory called "test1".
3. Use a Unix command to download the following file: https://wouterboomsma.github.io/ppds2020/data/m_scrambled.txt into a file called "m_scrambled.txt" within the "test1" directory.
4. Make a copy of the "test1" directory, called "test2".
5. Go to the "handin3" directory, and use the "find" command to output all files and directories under this directory.
6. Remove the "test2" directory.
7. Use the "cat" command to take a look at the "m_scrambled.txt" you just downloaded.
8. Find a way to "unscramble" (i.e. make sense of) the image into a new file called "m.txt" (in the "test1" directory).
9. Find a way to download, unscramble and save (into "m.txt") in a single (one-line) command (i.e. combine point 3. and 8.). Again, save it to a file called "m.txt" in the "test1" directory.
10. Delete the "handin3" directory and all directories below it


## Python

Now, we are going to do the same "unscrambling" exercise in Python.

1. Write a function called <code>unscramble_attempt1</code> that takes a list of strings as input, and returns a new list of strings. In this first attempt, use the built-in <code>sorted()</code> function to simply return a sorted version of the list. You can call the function by writing <pre><code>scrambled_file = open("m_scrambled.txt")
unscrambled_lines = unscramble_attempt1(scrambled_file.readlines())
print("".join(unscrambled_lines))
scrambled_file.close()</code></pre>

2. As you can see from the previous output, the unscrambling is not quite working. Try to understand what is causing the problem. One way to fix this is to transform the list of strings into a list of tuples, where the first value in the tuple is the line number (an integer), and the second element is the rest of the line (a string). You can call <code>sorted()</code> or <code>sort()</code> on this new list, and then transform it back into a list of strings. Write a function called <code>unscramble_attempt2</code> that does this. The function should return a list of strings just like in the previous exercise - such that it can be called like this: <pre><code>scrambled_file = open("m_scrambled.txt")
unscrambled_lines = unscramble_attempt1(scrambled_file.readlines())
print("".join(unscrambled_lines))
scrambled_file.close()</code></pre>

**Remember to add doc-strings to all your functions! If you forget, the tests will not pass.**