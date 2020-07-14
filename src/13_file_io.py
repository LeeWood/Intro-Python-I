"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open(r'C:\Users\Aleesha\LAMBDA_PROJECTS\cs\Intro-Python-I\src\foo.txt', 'r') 
print( f.read() )
f.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

newFile = open(r'C:\Users\Aleesha\LAMBDA_PROJECTS\cs\Intro-Python-I\src\bar.txt', 'w')
newFile.write("Hi friends...I'm the new file on the block.")
newFile.close()



# * What if this was a function that used inputs...?? 
"""
- takes in two arguments(name of new file and the text for the file)
- should be coming from inputs rather than parameters on the functions. Two inputs.
- open/create file...need to dynamically add file name to the path on `open()`...format string method?
- succuss message.
"""


def newTxtFile():
    name = input("File name: ")
    txt = input("File text: ")

    f = open(r'C:\Users\Aleesha\LAMBDA_PROJECTS\cs\Intro-Python-I\src\{0}.txt'.format(name), 'w')
    f.write(txt)
    f.close()
    
    print( "file created!" )
    
newTxtFile()

#!This works!! 