#Task 1: Open alice.tt and read to variable named lines.
f = open("alice.txt")
lines = f.readlines() 

#Task 2: Calculate and print how many lines there are in the file
number_of_lines = len(lines)
print(number_of_lines)

#Task 3: print the 41st line
selected_line = print(lines[40])

#Task 4: Count the number of words in the 43rd line and print the result
n_words = len(lines[42].split())
print(n_words)

#Task 5: Open new file junk.txt to junk_file var. Write 9th and 11th line from alice file to junk_file. Close file when done
file = open("junk.txt", "w+")
file.writelines([lines[8], "\n", lines[10]])
file.close()