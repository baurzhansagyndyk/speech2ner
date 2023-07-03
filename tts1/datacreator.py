import os
import csv

def create_csv_with_path(input_filename, output_filename, folder_name):
    # Get the current working directory
    current_directory = os.getcwd()

    # Construct the folder path based on the provided folder name
    folder_path = os.path.join(current_directory, folder_name)

    with open(input_filename, "r") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    # Add the 'path' header to the first row
    rows[0].append("path")

    # Fill the 'path' column with the desired values using the folder path
    for i in range(1, len(rows)):
        rows[i].append(f"{folder_path}/{i}.wav")

    # Write the modified data to a new CSV file
    with open(output_filename, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)

    print(f"A new CSV file '{output_filename}' has been created with the 'path' column.")

# Specify the folder name where the audio files are located
folder_name = "audios2"

# Specify the input CSV file name
input_filename = "test.csv"

# Specify the output CSV file name
output_filename = "test_with_path.csv"

# Call the function to create the new CSV file with the given folder path
create_csv_with_path(input_filename, output_filename, folder_name)

