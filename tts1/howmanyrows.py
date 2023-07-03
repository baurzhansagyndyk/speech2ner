import csv

filename = "test.csv"

with open(filename, "r") as file:
    csv_reader = csv.reader(file)
    rows = sum(1 for row in csv_reader)

print(f"The CSV file '{filename}' has {rows} rows.")
