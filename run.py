from FileHarvestor import read_files

if __name__ == "__main__":

    file_list = ["SampleDirectory/FolderA/File1.txt",
                 "SampleDirectory/FolderB/File1.txt",
                 "SampleDirectory/FolderC/File1.txt",
                 "SampleDirectory/FolderA/File2.txt",
                 "SampleDirectory/FolderB/File2.txt",
                 "SampleDirectory/FolderC/File2.txt",
                 "SampleDirectory/FolderA/File3.txt",
                 "SampleDirectory/FolderB/File3.txt",
                 "SampleDirectory/FolderC/File3.txt",
                 ]

    read_files(file_list=file_list,
               output_text_file='./output/contents.txt',
               output_markdown_file='./output/contents.md')
