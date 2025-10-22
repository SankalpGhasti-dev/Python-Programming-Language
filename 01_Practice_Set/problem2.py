import os 

# Specify the directory you want to list
directory_path = '/linux' 

# List all files and diretories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)

# Note: Make sure the specified directory exists to avoid errors.

