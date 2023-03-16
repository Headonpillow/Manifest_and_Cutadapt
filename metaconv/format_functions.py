import glob
import os


def mothur_to_cutadapt(string_list, adapter_type='^', barcode_length=7):
    new_string_list_forward = []
    new_string_list_reverse = []

    for string in string_list:
        if 'BARCODE' not in string.upper():
            continue
        else:
            new_line_forward = []
            new_line_reverse = []

            if barcode_length > 7:
                offset = barcode_length - 7
                corrected_fwd_end = 15 + offset
                corrected_rv_start = corrected_fwd_end + offset
                corrected_rv_end = corrected_rv_start + barcode_length
                corrected_sample_start = corrected_rv_end + offset

                forward = string[8:corrected_fwd_end]
                reverse = string[corrected_rv_start:corrected_rv_end]
                sample = string[corrected_sample_start:]

            else:
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


def convert_oligos(path='.', adapter_type='^', barcode_length=7):
    os.chdir(path)

    for oligo in glob.glob('*.file'):
        file = open(oligo)
        string_list = file.readlines()

        content = mothur_to_cutadapt(string_list, adapter_type, barcode_length)

        file = open(oligo + '_cutadapt_f.fasta', "w")
        new_content = ''.join(content[0])
        file.write(new_content)

        file = open(oligo + '_cutadapt_r.fasta', "w")
        new_content = ''.join(content[1])
        file.write(new_content)
