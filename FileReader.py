import os


def read_files_in_directory(directory='.', file_list=None, output_file='fileContents.txt'):
    """Reads all files in a directory and writes the contents to a file.

    Args:
        - directory (str, optional): The directory to read files from. Defaults to '.'.
        - file_list (list, optional): A list of files to read. Defaults to None.
        - output_file (str, optional): The file to write the contents to. Defaults to 'fileContents.txt'.
    """

    if file_list is None:
        return

    # Open the output file
    with open(output_file, 'w') as f:

        # Loop through the files in the list
        for file_name in file_list:

            # Construct the absolute file path
            file_path = os.path.join(directory, file_name)

            # Make sure the file exists
            if os.path.exists(file_path):

                # Open the file
                with open(file_path, 'r') as f2:

                    # Write the contents to the output file
                    # Title
                    f.write(f"{file_name}:\n")
                    # Contents
                    f.write(f2.read())
                    # New line
                    f.write("\n\n")

            else:
                print(f"File '{file_path}' does not exist.")

        # Close the output file
        f.close()


if __name__ == "__main__":

    file_list = ["Hello/hello.txt", "random_name.txt"]

    read_files_in_directory(".", file_list)
