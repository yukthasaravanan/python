import os
def create(content):
    with open("myFile.txt", 'w') as file:
        file.write(content)
create("hello haiiiiii")

# read data
def read():
    with open("myFile.txt", 'r') as readData:
        print(readData.read())
read()  

def append_to_file(content):
    with open("myFile.txt", "a") as openFile:
        openFile.write(content)

def read_file():
    with open("myFile.txt", "r") as readData:
        print(readData.read())

# Function calls
append_to_file("Now the file has more content\n")
read_file()

# os.rename("newFile.txt","mynewfile.txt")
# os.remove("mynewfile.txt")                         