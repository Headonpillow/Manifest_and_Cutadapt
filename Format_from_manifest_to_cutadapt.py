import os
import glob
import format_functions

os.chdir('.')

for oligo in glob.glob('*.file'):

    file = open(oligo)
    string_list = file.readlines()

    content = format_functions.mothur_to_cutadapt_2(string_list)

    file = open(oligo+'_cutadapt_f.fasta', "w")
    new_content = ''.join(content[0])
    file.write(new_content)

    file = open(oligo+'_cutadapt_r.fasta', "w")
    new_content = ''.join(content[1])
    file.write(new_content)