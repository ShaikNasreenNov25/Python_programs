# Task 1: Read a File and Handle Errors
import os

filename = "sample.txt"

if os.path.exists(filename):
    with open(filename, "r")as fh:
        print("Reading file content:")
        lines = fh.readlines()
        for i in range(len(lines)):
            print(f"Line {i+1} : {lines[i].strip()}")
else:
    print(f"Error: the file '{filename}' was not found.")

print("\n==========================================\n")
# Task 2: Write and Append Data to a File

data = input("Enter text to write to the file: ")
file_name = "output.txt"
with open(file_name, "w") as file:
    file.write(data + "\n")
print(f"Data successfully written to {file_name}.\n")

add_data = input("Enter additional text to append: ")
with open(file_name, "a") as file:
    file.write(add_data + "\n")
print("Data successfully appended.\n")

print(f"Final content of {file_name}: ")

with open(file_name, "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"{line.strip()}")

