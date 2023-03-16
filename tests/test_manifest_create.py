import os
import metaconv


def test_manifest_create():
    metaconv.write_manifest(raw_files_path='./resources')
    file = open('./resources/manifest.tsv')
    lines = file.readlines()
    assert(lines[0] == 'sample-id\tforward-absolute-filepath\treverse-absolute-filepath\n')
    assert(lines[1] == 'SML_A1\t/home/headonpillow/Desktop/PhD/Projects/metaconv/resources/SML_A1.R1.fastq.gz\t/home/headonpillow/Desktop/PhD/Projects/metaconv/resources/SML_A1.R2.fastq.gz\n')
    os.remove('./resources/manifest.tsv')
