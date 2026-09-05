## File read using open() function

def File_ReadWrite_Using_Open():
    file_read = open("File read and write/files repository/notes.txt", "r")
    content = file_read.read()
    print(content)
    file_read.close() ## make sure to close the file after reading if you are using the Open() function to read the file. This is important to free up system resources and avoid potential issues with file access.

    ## File write using open() function
    file_write = open("File read and write/files repository/notes.txt", "w")
    file_write.write("This is a new line of text.")
    file_write.close()
 
def File_Read_Using_With_Statement():
    with open("File read and write/files repository/notes.txt", "r") as file:
        content = file.read()
        print(content)


def File_Append_Using_With_Statement():
    with open("File read and write/files repository/notes.txt", "a") as file_append:
        file_append.write("\nThis line is appended to the file.")


##File_Append_Using_With_Statement()
File_Read_Using_With_Statement()