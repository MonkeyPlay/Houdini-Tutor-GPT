The text files are later compiled together and are one of the custom knogledge files supported for Houdini-Tutor-GPT

Currently extracting transcripts using :https://tactiq.io/tools/youtube-transcript



Steps to Make the python code work
Clone the Repository Use the git clone command to download the repository to your local system:

bash
Copy
Edit
git clone https://github.com/MonkeyPlay/Houdini-Tutor-GPT.git
This will create a local directory named Houdini-Tutor-GPT.

Update the Path in the Script Modify the repo_dir variable in the script to point to the local path of the cloned repository. For example:

python
Copy
Edit
repo_dir = "Houdini-Tutor-GPT"
Run the Script Execute the Python script from the same directory where it is saved. Make sure the script has access to the cloned repository's local path.

Output The script will scan the Houdini-Tutor-GPT directory, find all .txt files, and create the combined.txt file containing their contents.
