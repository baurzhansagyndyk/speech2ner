import csv

input_file = "textsproaudio.csv"
output_file = "train.csv"

# Open the input CSV file for reading
with open(input_file, "r") as file:
    reader = csv.reader(file)
    data = list(reader)  # Read the entire CSV data into a list

# Keep only the first column of each row
new_data = [[row[0]] for row in data]

# Write the new data to the output CSV file
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_data)
