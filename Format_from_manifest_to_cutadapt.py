import os
import glob
import format_functions

os.chdir('/home/headonpillow/Desktop/PhD/UPPMAX_jobs/oligos')

for oligo in glob.glob('*.file'):

    f = open(oligo)
    string_list = f.readlines()

    format_functions.mothur_to_cutadapt_2(string_list, oligo)
