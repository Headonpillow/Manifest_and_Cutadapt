import glob
import os


def mothur_to_cutadapt(string_list, adapter_type='^', barcode_length=7):
    '''
    Used from the "Convert Oligo" function to actually operate the conversion.
    It reads line by line the previous file and reformats every line with a new string.

    Parameters
    ----------
    string_list :
        This parameter is created during the call of 'Convert_oligos'.

    adapter_type : string
        Specify the type of adapter for Cutadapt, according to the ones listed
        `here<https://cutadapt.readthedocs.io/en/stable/guide.html#adapter-types>`_.
        Default `adapter_type = ''` that corresponds to an anchored 5' adapter.

    barcode_length : integer
        Specify the length of the barcodes in the oligo files.
        Default `barcode_length = 7`
    '''

    # Create two empty lists of strings, they will in the end have the whole
    # content of the file, line by line.
    new_string_list_forward = []
    new_string_list_reverse = []

    for string in string_list:
        # This excludes the "PRIMERS" string and only selects the barcodes.
        if 'BARCODE' not in string.upper():
            continue
        else:
            # Two new line list are created, one forward and one reverse.
            # The whole function runs in parallel creating contents for the
            # two different files.
            new_line_forward = []
            new_line_reverse = []

            # This part of the function takes care of setting an offset to the
            # hard coded positions in the string below contained in the "else".
            # This behaviour is needed because the function has been thought
            # to deal with 7bp long barcodes, if the barcodes are longer, the index
            # just gets updated.
            # Still the function doesn't take into account the chance the barcode
            # length might be shorter than 7.
            if barcode_length > 7:
                # Calculates offset length
                offset = barcode_length - 7
                corrected_fwd_end = 15 + offset
                corrected_rv_start = corrected_fwd_end + offset
                corrected_rv_end = corrected_rv_start + barcode_length
                corrected_sample_start = corrected_rv_end + offset

                # Determines which string is forward and reverse and which one
                # indicates the sample.
                forward = string[8:corrected_fwd_end]
                reverse = string[corrected_rv_start:corrected_rv_end]
                sample = string[corrected_sample_start:]

            else:
                # Hardcoded case in which the barcode is 7bp long, this is also
                # the default behaviour of the function.
                forward = string[8:15]
                reverse = string[16:23]
                sample = string[24:]

            # Any occurrence of "/" is replaced with "-" for consistency.
            sample = sample.replace("/", "-")
            # The new line is now created, with the specified "adapter_type"
            # "new_line" is a list of strings.
            new_line_forward.append('>')
            new_line_forward.append(sample)
            new_line_forward.append(adapter_type)
            new_line_forward.append(forward)
            new_line_forward.append('\n')

            new_line_reverse.append('>')
            new_line_reverse.append(sample)
            new_line_reverse.append(adapter_type)
            new_line_reverse.append(reverse)
            new_line_reverse.append('\n')

            # A complete string is created from the "new_line" list and put it into a variable.
            new_string_forward = ''.join(new_line_forward)
            # This new string is appended to the empty "content" list created outside the loop.
            new_string_list_forward.append(new_string_forward)
            new_string_reverse = ''.join(new_line_reverse)
            new_string_list_reverse.append(new_string_reverse)

    # The function returns the content of forward and reverse files as a list of strings.
    return [new_string_list_forward, new_string_list_reverse]


def convert_oligos(path='.', adapter_type='^', barcode_length=7):
    """
    Converts the Mothur "oligo" format to .fasta files containing the barcodes, for use with Cutadapt.

    The function reads the barcode pairs present in the oligo files with the .file extension used in the Mothur
    software. Those barcode pairs are reformatted in two different .fasta files that can be used as inputs to
    operate the demultiplexing of NGS reads with Cutadapt.
    It outputs .fasta files in the directory where the oligo files are present.

    Parameters
    ----------
    path : string
        The path where the oligo files are stored, this directory will also be the output directory.
        Default `path = '.'`

    adapter_type : string
        Specify the type of adapter for Cutadapt, according to the ones listed
        `here<https://cutadapt.readthedocs.io/en/stable/guide.html#adapter-types>`_.
        Default `adapter_type = ''` that corresponds to an anchored 5' adapter.

    barcode_length : integer
        Specify the length of the barcodes in the oligo files.
        Default `barcode_length = 7`
    """

    # Retrieve the root from where the script is running from to change it back
    # at the end of the function.
    root = os.getcwd()
    # Change working directory to the path passed to the function where the files are.
    os.chdir(path)

    for oligo in glob.glob('*.file'):
        file = open(oligo)
        # Read the lines of the oligo file and creates a list, this will be
        # passed to the "mothur_to_cutadapt" function.
        string_list = file.readlines()

        # Use the mothur_to_cutadapt() function to do the conversion.
        # The content variable is a list, with one content forward and
        # one content reverse.
        content = mothur_to_cutadapt(string_list, adapter_type, barcode_length)

        # Write the contents in the new files
        file = open(oligo + '_cutadapt_f.fasta', "w")
        new_content = ''.join(content[0])
        file.write(new_content)

        file = open(oligo + '_cutadapt_r.fasta', "w")
        new_content = ''.join(content[1])
        file.write(new_content)

    os.chdir(root)
