import glob
import os

def ReverseComplement(string_list):
    new_string_list = []

    for string in string_list:
        if 'BARCODE' not in string:
            continue
        else:
            new_line = []
            forward = string[8:15]
            reverse = string[16:23]
            sample = string[24:]
            sample = sample.replace("/", "-")
            reversed_f = forward[::-1]
            rc_forward = ''
            for base in reversed_f:
                if base == 'A':
                    rc_forward += 'T'
                if base == 'T':
                    rc_forward += 'A'
                if base == 'C':
                    rc_forward += 'G'
                if base == 'G':
                    rc_forward += 'C'
            new_line.append('>')
            new_line.append(sample)
            new_line.append('X')
            new_line.append(forward)
            new_line.append('\n')
            new_line.append('>')
            new_line.append(sample)
            new_line.append('X')
            new_line.append(reverse)
            new_line.append('\n')
            new_line.append('>')
            new_line.append(sample)
            new_line.append('X')
            new_line.append(rc_forward)
            new_line.append('\n')

            new_string = ''.join(new_line)
            new_string_list.append(new_string)

    return new_string_list

def MothurToCutadapt(string_list, adapter_type = '^'):

# It just works when barcodes are 7bp long tho, maybe I can implement another parameter.

    new_string_list_forward = []
    new_string_list_reverse = []

    for string in string_list:
        if 'BARCODE' not in string.upper():
            continue
        else:
            new_line_forward = []
            new_line_reverse = []

            forward = string[8:15]
            reverse = string[16:23]
            sample = string[24:]

            sample = sample.replace("/", "-")
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

            new_string_forward = ''.join(new_line_forward)
            new_string_list_forward.append(new_string_forward)
            new_string_reverse = ''.join(new_line_reverse)
            new_string_list_reverse.append(new_string_reverse)

    return [new_string_list_forward, new_string_list_reverse]

def ConvertOligos(path = '.'):

    os.chdir(path)

    for oligo in glob.glob('*.file'):
        file = open(oligo)
        string_list = file.readlines()

        content = MothurToCutadapt(string_list)

        file = open(oligo + '_cutadapt_f.fasta', "w")
        new_content = ''.join(content[0])
        file.write(new_content)

        file = open(oligo + '_cutadapt_r.fasta', "w")
        new_content = ''.join(content[1])
        file.write(new_content)