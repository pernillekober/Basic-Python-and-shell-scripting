# Create a directory called "handin3" in your current directory.
mkdir handin3

# Inside this directory, create a directory called "test1".
mkdir handin3/test1/

# Use a Unix command to download the following file: https://wouterboomsma.github.io/ppds2020/data/m_scrambled.txt into a file called "m_scrambled.txt" within the "test1" directory.
curl https://wouterboomsma.github.io/ppds2020/data/m_scrambled.txt -o handin3/test1/m_scrambled.txt


# Make a copy of the "test1" directory, called "test2".
cp -R handin3/test1 handin3/test2

# Go to the "handin3" directory, and use the "find" command to output all files and directories under this directory.
cd handin3
find .
cd ..

# Remove the "test2" directory.
rm -rf handin3/test2

# Use the "cat" command to take a look at the "m_scrambled.txt" you just downloaded.
cat handin3/test1/m_scrambled.txt

# Find a way to "unscramble" (i.e. make sense of) the image into a new file called "m.txt" (in the "test1" directory).
sort -n handin3/test1/m_scrambled.txt > handin3/test1/m.txt

# Find a way to download, unscramble and save (into "m.txt") in a single (one-line) command (i.e. combine point 3. and 8.). Again, save it to a file called "m.txt" in the "test1" directory.
curl https://wouterboomsma.github.io/ppds2020/data/m_scrambled.txt -o handin3/test1/m_.txt && sort -n handin3/test1/m_.txt > handin3/test1/m.txt

# Delete the "handin3" directory and all directories below it
rm -rf handin3