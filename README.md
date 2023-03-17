[![Documentation Status](https://readthedocs.org/projects/metaconv/badge/?version=latest)](https://metaconv.readthedocs.io/en/latest/?badge=latest)

# metaconv

This python package has been developed to allow the conversion of the input files required from some of the most 
common programs for 16S amplicon analysis.

This package works mostly by allowing the user to use a live intepreter to read the content of folders as inputs and
produce different outputs according to the use case.

It supports mainly:

* The conversion from "oligo" file format (Mothur) to ".fasta" files to be used for the demultiplexing of illumina
paired-end reads with Cutadapt.
* The generation of a "manifest.tsv" file that is needed to import raw data in Qiime2 for the analysis of 16s
amplicon data.

The documentation is available on [read the docs](https://metaconv.readthedocs.io/en/latest/).