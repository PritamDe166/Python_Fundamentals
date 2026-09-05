import csv

# Reading as row by row, as plain lists
def ReadCsvHeaders():
  with open("File read and write/files repository/grades.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)
    for row in header:
      print(row)


# Reading as Dictionaries (usually nicer to work with — uses the header row as keys automatically)
def ReadCsvAsDictionaries():
  with open("File read and write/files repository/grades.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    print(reader.fieldnames) # Prints the row headers

    for row in reader:
      print(row["name"], row["subject"], row["score"])

# method calls

# ReadCsvHeaders()
ReadCsvAsDictionaries()