import os

# Define the directory to search (update this to your desired folder path)
repo_dir = "YouTube-Transcript"  # Replace this with your actual folder path

# Define the name of the output file
output_file = "combined.txt"

# List to store the paths of all .txt files
txt_files = []

# Traverse the directory and all subdirectories
for root, _, files in os.walk(repo_dir):
    for file in files:
        # Check if the file has a .txt extension
        if file.endswith(".txt"):
            # Store the full path to the .txt file
            txt_files.append(os.path.join(root, file))

# Write the combined contents into the output file
with open(output_file, "w", encoding="utf-8") as outfile:
    for txt_file in txt_files:
        # Add a header for each file's contents
        outfile.write(f"Contents of {txt_file}:\n")
        try:
            # Read and write the content of the .txt file
            with open(txt_file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
        except Exception as e:
            # Handle errors (e.g., unreadable files)
            outfile.write(f"Error reading file: {e}\n")
        # Add a separator between files
        outfile.write("\n" + "-" * 40 + "\n")

# Confirmation message
print(f"Combined file '{output_file}' created successfully!")
