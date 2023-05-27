import os


def read_files_in_directory(directory='.', output_file='fileContents.txt', ignored_directories=[]):

    default_ignored = ['.git', '.gitignore', '.vscode',
                       '__pycache__', 'node_modules', '.venv']

    # Add the default ignored directories to the ignored directories list
    ignored_directories.extend(default_ignored)

    # Open the output file
    with open(output_file, 'w') as f:
        # Walk through the directory
        for root, dirs, files in os.walk(directory):
            # For each file
            for file_name in files:

                # Skip the output file
                if file_name == output_file:
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