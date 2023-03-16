import os
import metaconv

ABS_PATH = os.path.dirname(os.path.abspath(__file__))


def test_format_functions():
    metaconv.convert_oligos(path='resources')
    os.chdir(ABS_PATH)
    file_f = open('resources/mos1.file_cutadapt_f.fasta')
    lines = file_f.readlines()
    for line in lines:
        assert (line.startswith('>') or line.startswith('^') == True)
        assert (line.endswith("\n") == True)
    file_r = open('resources/mos1.file_cutadapt_f.fasta')
    lines = file_r.readlines()
    for line in lines:
        assert (line.startswith('>') or line.startswith('^') == True)
        assert (line.endswith("\n") == True)

    os.remove('resources/mos1.file_cutadapt_f.fasta')
    os.remove('resources/mos1.file_cutadapt_r.fasta')

