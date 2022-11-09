def mothur_to_cutadapt_f(string_list):
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
            RC_forward = ''
            for base in reversed_f:
                if base == 'A':
                    RC_forward += 'T'
                if base == 'T':
                    RC_forward += 'A'
                if base == 'C':
                    RC_forward += 'G'
                if base == 'G':
                    RC_forward += 'C'
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
            new_line.append(RC_forward)
            new_line.append('\n')

            new_string = ''.join(new_line)
            new_string_list.append(new_string)

    return new_string_list


def mothur_to_cutadapt_r(string_list):
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
            reversed_r = reverse[::-1]
            RC_reverse = ''
            for base in reversed_r:
                if base == 'A':
                    RC_reverse += 'T'
                if base == 'T':
                    RC_reverse += 'A'
                if base == 'C':
                    RC_reverse += 'G'
                if base == 'G':
                    RC_reverse += 'C'
            new_line.append('>')
            new_line.append(sample)
            new_line.append('X')
            new_line.append(reverse)
            new_line.append('\n')
            new_line.append('>')
            new_line.append(sample)
            new_line.append('X')
            new_line.append(forward)
            new_line.append('\n')
            new_line.append('>')
            new_line.append(sample)
            new_line.append('X')
            new_line.append(RC_reverse)
            new_line.append('\n')

            new_string = ''.join(new_line)
            new_string_list.append(new_string)

    return new_string_list


def mothur_to_cutadapt_F(string_list):
    new_string_list = []

    for string in string_list:
        if 'BARCODE' not in string:
            continue
        else:
            new_line = []
            forward = string[8:15]
            sample = string[24:]
            sample = sample.replace("/", "-")
            new_line.append('>')
            new_line.append(sample)
            new_line.append('X')
            new_line.append(forward)
            new_line.append('\n')

            new_string = ''.join(new_line)
            new_string_list.append(new_string)

    return new_string_list


def mothur_to_cutadapt_R(string_list):
    new_string_list = []

    for string in string_list:
        if 'BARCODE' not in string:
            continue
        else:
            new_line = []
            reverse = string[16:23]
            sample = string[24:]
            sample = sample.replace("/", "-")
            new_line.append('>')
            new_line.append(sample)
            new_line.append('X')
            new_line.append(reverse)
            new_line.append('\n')

            new_string = ''.join(new_line)
            new_string_list.append(new_string)

    return new_string_list


def mothur_to_cutadapt_2(string_list, oligo):
    new_string_list_forward = []
    new_string_list_reverse = []

    for string in string_list:
        if 'BARCODE' not in string:
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
            new_line_forward.append('^')
            new_line_forward.append(forward)
            new_line_forward.append('\n')

            new_line_reverse.append('>')
            new_line_reverse.append(sample)
            new_line_reverse.append('^')
            new_line_reverse.append(reverse)
            new_line_reverse.append('\n')

            new_string_forward = ''.join(new_line_forward)
            new_string_list_forward.append(new_string_forward)
            new_string_reverse = ''.join(new_line_reverse)
            new_string_list_reverse.append(new_string_reverse)

    file = open(oligo[:4]+'_cutadapt_f.fasta', "w")
    new_content = ''.join(new_string_list_forward)
    file.write(new_content)

    file = open(oligo[:4]+'_cutadapt_r.fasta', "w")
    new_content = ''.join(new_string_list_reverse)
    file.write(new_content)