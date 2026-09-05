import json

# writing into a json file directly from dictionary
settings_write_path = "File read and write/files repository/users_example_write.json"

def WriteToJsonFile(path:str):
  settings = [
    {
      "name" : "James",
      "age" : 32,
      "location" : "Bangalore"
    },
    {
      "name" : "John",
      "age" : 31,
      "location" : "Pune"
    }
  ]

  with open(path, "w") as json_file:
    json.dump(settings, json_file, indent=4)


def ReadfromJson(path:str):
  with open(path, "r") as json_file:
    print(json.load(json_file))



WriteToJsonFile(settings_write_path)
ReadfromJson(settings_write_path)