import os


def read_folder_content(raw_files_path='.'):
    os.chdir(raw_files_path)
    file_list = []
    content = os.listdir()
    for file in content:
        if '.fastq.gz' in file:
            file_list.append(os.path.abspath(file))
    return file_list


def write_manifest(raw_files_path='.'):
    root = os.getcwd()
    # Use the function 'ReadFolderContent' to
    file_list = read_folder_content(raw_files_path)
    new_string_list = []
    header = 'sample-id\tforward-absolute-filepath\treverse-absolute-filepath\n'
    new_string_list.append(header)
    for string in file_list:
        if 'R1' in string:
            # Create an empty new line variable to append the parts to.
            new_line = []

            # Get the path directory from the system and determine how long it is.
            path = os.getcwd() + '/'
            path_length = len(path)

            # The length is needed to index the subsequent string and retrieve just the sample name.
            # The subset of the string starts when the path ends and stops at -12 (that removes the
            # last characters '.R1.fastq.gz').
            sample = string[path_length:-12]
            new_line.append(sample)
            new_line.append('\t')
            new_line.append(string)
            new_line.append('\t')
            string2 = string.replace('R1', 'R2')
            new_line.append(string2)
            new_line.append('\n')

            new_string = ''.join(new_line)
            new_string_list.append(new_string)

    file = open('manifest.tsv', "w")
    new_content = ''.join(new_string_list)
    file.write(new_content)
    os.chdir(root)
