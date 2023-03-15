import os
import glob

os.chdir('.')

# So whatever it does, it just converts basically a tsv file that contains for each string:
# from 0:-13 the sample (so the last 13 positions are the rest of the filename like ".R1 etc.")
# the whole string is the filename, that ends with "/"? that gets removed from the "-1".
# Apparently the thing happens for many .tsv files idk why.
# I don't understand from what types of .tsvs this is supposed to create a manifest file.

content = os.listdir()

new_string_list = []

for file in content:

    f = open(file)
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
