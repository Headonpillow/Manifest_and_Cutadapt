import os


def read_folder_content(raw_files_path='.'):
    '''
    It reads the content of a folder to retrieve a list of `.fastq.gz` files.

    Parameters
    ----------
    raw_files_path :
        The path where the raw `.fastq.gz` files are stored.
    '''

    # Change directory to match the "raw_files_path" specified.
    os.chdir(raw_files_path)
    # Create an empty list to which append the names of the files in the folder.
    file_list = []
    # Actually reads the content of the folder.
    content = os.listdir()
    for file in content:
        # Appends to the "file_list" just the ".fastq.gz" files
        if '.fastq.gz' in file:
            file_list.append(os.path.abspath(file))
    return file_list


def write_manifest(raw_files_path='.'):
    '''
    It writes a manifest file to use as import with Qiime2 from a folder of ´.fastq.gz'files.
    The content of the folder is read and all the ´.gz´ files included in the manifest.
    The manifest file can then be used normally with Qiime2 to start the analysis pipeline.

    Parameters
    ----------
    raw_files_path :
        The path where the raw `.fastq.gz` files are stored.
    '''

    # Sets the root from which the script is running from.
    root = os.getcwd()
    # Use the function "read_folder_content" to get a list of the filenames in the folder.
    file_list = read_folder_content(raw_files_path)
    # Creates a new list to which append the lines that will be created
    new_string_list = []
    # The header is gonna be the same for all the created manifest files.
    header = 'sample-id\tforward-absolute-filepath\treverse-absolute-filepath\n'
    new_string_list.append(header)
    for string in file_list:
        # This select just one string of the filenames, just the forward one.
        # This happens because we just need one occurrence that will be adapted
        # to write also the reverse one, but in this way we keep only one string to work on.
        if 'R1' in string:
            # Create an empty new line variable to append the different part of the line.
            new_line = []

            # Get the path directory from the system and determine how long it is.
            # This is needed to actually correctly index the subsequent string and retrieve
            # just the sample name .
            path = os.getcwd() + '/'
            path_length = len(path)

            # The subset of the string starts when the path ends and stops at -12 (that removes the
            # last characters '.R1.fastq.gz').
            sample = string[path_length:-12]

            # Here we start appending things to the "new_line".
            new_line.append(sample)
            new_line.append('\t')
            new_line.append(string)
            new_line.append('\t')
            # And here the string is modified to consider the reverse file "R2".
            string2 = string.replace('R1', 'R2')
            new_line.append(string2)
            new_line.append('\n')

            # A whole string is created with "join" and appended to the new list of strings
            # that will be the content of the file at the end.
            new_string = ''.join(new_line)
            new_string_list.append(new_string)

    # A file is open in writing mode and the new content is joined and written to it.
    file = open('manifest.tsv', "w")
    new_content = ''.join(new_string_list)
    file.write(new_content)
    # The directory is changed back to root.
    os.chdir(root)
