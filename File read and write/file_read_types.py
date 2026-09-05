
# whole file as one string
def Normal_Read():
    with open("File read and write/files repository/notes.txt", "r") as file01:
        content = file01.read()
        print(content)

def Read_Line_By_Line():
    with open("File read and write/files repository/notes.txt", "r") as file02:
      content = file02.readlines()
      for line in content:
          print(line.strip()) # The strip() method removes any leading or trailing whitespace
          
def File_read_loopByLine():
    with open("File read and write/files repository/notes.txt", "r") as file:
        for line in file:  # most common pattern — loop line by line
            print(line.strip())


# Normal_Read()
# Read_Line_By_Line()
File_read_loopByLine()
