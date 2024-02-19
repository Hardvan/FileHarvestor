import os
import time


def read_files_in_directory(directory='.', file_list=None, output_file='./output/contents.txt'):

    if file_list is None:
        print("❌ No files to read. Exiting.")
        return

    start = time.time()  # Start the timer

    # Create the output directory if it doesn't exist
    output_directory = os.path.dirname(output_file)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    not_found_files = []  # List to store files that were not found
    with open(output_file, 'w', encoding='utf-8') as f:  # Open the output file

        for file_name in file_list:  # Iterate through the list of files

            file_path = os.path.join(directory, file_name)  # absolute path

            # Make sure the file exists
            if os.path.exists(file_path):

                # Open the file with the appropriate encoding
                with open(file_path, 'r', encoding='utf-8') as f2:
                    # Write the contents to the output file
                    f.write(f"{file_name}:\n")  # Title
                    f.write(f2.read())  # Contents
                    f.write("\n\n")  # New line
                    print(f"✅ '{file_path}' read successfully")

            else:
                print(f"❌ File '{file_path}' does not exist.")
                not_found_files.append(file_path)

    if len(not_found_files) > 0:
        print(
            f"❌ The following files were not found ({len(not_found_files)} of {len(file_list)}):")
        for file in not_found_files:
            print(f"  - {file}")
    else:
        print("✅ All files read successfully")

    end = time.time()  # End the timer
    elapsed_time = round(end - start, 2)  # Calculate the elapsed time

    print(
        f"✅ Output written to '{output_file}' \033[90m({elapsed_time}s)\033[0m")


if __name__ == "__main__":

    app_py = "app.py"
    students_py = "Students.py"
    index_html = "templates/index.html"
    index_css = "static/css/index.css"
    index_js = "static/js/index.js"

    read_files_in_directory(directory=".",
                            file_list=[app_py, students_py,
                                       index_html, index_js],
                            output_file="./output/contents.txt")
