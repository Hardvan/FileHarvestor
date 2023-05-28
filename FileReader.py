import os


def read_files_in_directory(directory='.', output_file='fileContents.txt'):
    """Reads all files in a directory and writes the contents to a file.

    Args:
        - directory (str, optional): The directory to read files from. Defaults to '.'.
        - output_file (str, optional): The file to write the contents to. Defaults to 'fileContents.txt'.
        - ignored_directories (list, optional): A list of directories to ignore. Defaults to None.
    """

    ignored_directories = ['.git', '.gitignore', '.vscode',
                           '__pycache__', 'node_modules', '.venv']

    ignored_extensions = []

    # Open the output file
    with open(output_file, 'w') as f:
        # Walk through the directory
        for root, dirs, files in os.walk(directory):

            # Remove ignored directories from the traversal
            dirs[:] = [d for d in dirs if d not in ignored_directories]

            # For each file
            for file_name in files:

                # Skip the output file
                if file_name == output_file or file_name.split('.')[-1] in ignored_extensions:
                    continue

                # Get the file path
                file_path = os.path.join(root, file_name)

                # Write the file path to the output file
                f.write(f"{file_path}:\n")

                # Open the file and write the contents to the output file
                with open(file_path, 'r') as file:
                    file_contents = file.read()
                    f.write(file_contents)

                f.write("\n\n")  # Write a new line to the output file


if __name__ == "__main__":
    read_files_in_directory()
