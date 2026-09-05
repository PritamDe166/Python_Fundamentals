import csv

# using writer to append data to an existing csv
def WriteCsvByRow():
  with open("File read and write/files repository/grades.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Alice", "Civics", "89"])


# using the dictionary writer to write the headers and rows into a non-exisiting csv
def WriteCsvByDictWriter():
  students = [{"name":"Alice", "subject":"History", "score":"97"}, {"name":"Bob", "subject":"Civics", "score":"90"}]

  with open("File read and write/files repository/grades01.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "subject", "score"])
    writer.writeheader()
    writer.writerows(students)


def ReadCsv(path:str):
  with open(path, "r") as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)

    for row in reader:
      print(row["name"], row["subject"], row["score"])



WriteCsvByRow()
WriteCsvByDictWriter()

grades = "File read and write/files repository/grades.csv"
grades01 = "File read and write/files repository/grades01.csv"

ReadCsv(grades)
ReadCsv(grades01)