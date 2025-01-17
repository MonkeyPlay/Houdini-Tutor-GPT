import os

# Define the directory of the Git repository
repo_dir = "Houdini-Tutor-GPT"

# Define the output file
output_file = "combined.txt"

# List to store the paths of all .txt files
txt_files = []

# Traverse the repository directory
for root, _, files in os.walk(repo_dir):
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(os.path.join(root, file))

# Write the names of the txt files and their contents to the combined file
with open(output_file, "w") as outfile:
    for txt_file in txt_files:
        outfile.write(f"Contents of {txt_file}:\n")
        with open(txt_file, "r") as infile:
            outfile.write(infile.read())
        outfile.write("\n" + "-"*40 + "\n")

print(f"Combined file '{output_file}' created successfully!")
