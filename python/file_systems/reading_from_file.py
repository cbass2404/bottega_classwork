"""
r lets the function read the content of the text file
filename.mode == 'r' lets you check to make sure you are in read mode for that file only
len(content.split()) lets you check the word length in the document
"""


def get_file_contents(filename):
    queried_file = open(filename, 'r')

    if queried_file.mode == 'r':
        return queried_file.read()


content = get_file_contents("text_content.txt")

print(content)

print("Number of words", len(content.split()))
