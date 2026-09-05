import json

# Reading a json into a dict directly
def ReadFromJson():
  with open("File read and write/files repository/settings_example.json", "r") as jsonFile:
    config = json.load(jsonFile)
    print(config)

ReadFromJson()