from pathlib import Path

def file_system_tree(directory: Path, indent: str = ""):
    # Print the directory name
    print(indent + str(directory.name) + "/")
    # Iterate over the contents of the directory
    for item in directory.iterdir():
        if item.is_dir():
            # If the item is a directory, call the function recursively
            file_system_tree(item, indent + "    ")
        else:
            # If the item is a file, print its name
            print(indent + "    " + item.name)

# Specify the directory you want to start from
starting_directory = Path.cwd()

# Call the function
file_system_tree(starting_directory)

