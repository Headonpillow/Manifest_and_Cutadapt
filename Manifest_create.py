import os
import glob

os.chdir('/home/headonpillow/Desktop/PhD/UPPMAX_jobs/cutadapt')

for manifest in glob.glob('*.tsv'):

    f = open(manifest)
    string_list = f.readlines()

    new_string_list = []
    header = 'sample-id\tforward-absolute-filepath\treverse-absolute-filepath\n'
    new_string_list.append(header)

    for string in string_list:

        if 'R1' in string:

            new_line = []

            sample = string[0:-13]
            new_line.append(sample)
            new_line.append('\t')
            new_line.append('$PWD/')
            new_line.append(string[0:-1])
            new_line.append('\t')
            string2 = string.replace('R1', 'R2')
            new_line.append('$PWD/')
            new_line.append(string2[0:-1])
            new_line.append('\n')

            new_string = ''.join(new_line)
            new_string_list.append(new_string)

    file = open('manifest.tsv', "w")
    new_content = ''.join(new_string_list)
    file.write(new_content)
