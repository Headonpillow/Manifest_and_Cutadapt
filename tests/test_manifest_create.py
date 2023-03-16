import os
import metaconv


def test_manifest_create():
    metaconv.write_manifest(raw_files_path='./resources')
    file = open('./resources/manifest.tsv')
    lines = file.readlines()
    assert(lines[0] == 'sample-id\tforward-absolute-filepath\treverse-absolute-filepath\n')
    os.remove('./resources/manifest.tsv')
