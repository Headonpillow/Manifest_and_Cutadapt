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
            rc_reverse = ''
            for base in reversed_r:
                if base == 'A':
                    rc_reverse += 'T'
                if base == 'T':
                    rc_reverse += 'A'
                if base == 'C':
                    rc_reverse += 'G'
                if base == 'G':
                    rc_reverse += 'C'
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
            new_line.append(rc_reverse)
            new_line.append('\n')

            new_string = ''.join(new_line)
            new_string_list.append(new_string)

    return new_string_list


def mothur_to_cutadapt_f_2(string_list):
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


def mothur_to_cutadapt_r_2(string_list):
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


def mothur_to_cutadapt_2(string_list):

    # This function is the correct and currently implemented one, anyhow the commented lines in here are the
    # ones to specify the kind of adapter we are dealing with.

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
            # new_line_forward.append('^')
            new_line_forward.append(forward)
            new_line_forward.append('\n')

            new_line_reverse.append('>')
            new_line_reverse.append(sample)
            # new_line_reverse.append('^')
            new_line_reverse.append(reverse)
            new_line_reverse.append('\n')

            new_string_forward = ''.join(new_line_forward)
            new_string_list_forward.append(new_string_forward)
            new_string_reverse = ''.join(new_line_reverse)
            new_string_list_reverse.append(new_string_reverse)

    return [new_string_list_forward, new_string_list_reverse]
