# import os
# def create(content):
#     with open("myFile.txt", 'w') as file:
#         file.write(content)
# create("hello haiiiiii")

# # read data
# def read():
#     with open("myFile.txt", 'r') as readData:
#         print(readData.read())
# read()  

# def append_to_file(content):
#     with open("myFile.txt", "a") as openFile:
#         openFile.write(content)

# def read_file():
#     with open("myFile.txt", "r") as readData:
#         print(readData.read())

# # Function calls
# append_to_file("Now the file has more content\n")
# read_file()

# os.rename("newFile.txt","mynewfile.txt")
# os.remove("mynewfile.txt")


#create a new file ,get three input from user save each line in a new line in a file name called names.txt and read alll the name and 
# print the uppercase
def three_input():
    with open("names.txt", "w") as file:
        for i in range(3):
            name = input("enter the any statement:" )
            file.write(name + "\n")

def uppercase():
    with open("names.txt", "r") as file:
        for line in file:
            print(line.strip( ).upper( ))
three_input()
uppercase()








