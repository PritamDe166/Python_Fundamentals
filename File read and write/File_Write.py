
def FileWrite():
  with open("File read and write/files repository/notes.txt", "a") as file:
    file.write("First Line\n")
    file.write("Second Line\n")

def FileRead():
  with open("File read and write/files repository/notes.txt", "r") as file:
    for line in file:
      print(line.strip())

FileWrite()
FileRead()