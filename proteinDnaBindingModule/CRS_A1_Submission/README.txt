This python code does depend on hg19 fasta files for chromosome 3, 8, 12, 15 
to be present (in the same folder as the code) to run. 

Below are the assignment directions:

UPGEN 778 (Protein-DNA binding module)
Assignment 1
Due: Monday, Oct 15, 2pm

Please submit all your answers and Python scripts as a single zip file, through Sakai.


1. Finding E2F1 binding sites in the UHRF1 promoter (10pt)

Write a Python script to find E2F1 binding sites, defined as matches to the consensus sequence TTTSSCGC (where S=C or G), in the promoter of the UHRF1 gene (provided in the file UHRF1_promoter_region.txt). Use your Python script to answer the following questions:

* How many E2F1 binding sites are there in the UHRF1 promoter?

* What is the exact DNA sequence for each of these binding sites?

* Where does each binding site start within this promoter? (report this as a 1-based coordinate relative to the start of the genomic sequence in file UHRF1_promoter_region.txt, regardless of whether the site occurs on the forward or the reverse strand)


2. Finding the best E2F1 binding site in the UHRF1 promoter (15pt)

Write a Python script to identify the best E2F1 binding site in the promoter of the UHRF1 gene, defined as the site with the best probability score according to the E2F1 DNA binding motif (or PWM). Print and report the optimal site, its score, and its location within the sequence (report this location as a 1-based coordinate relative to the start of the genomic sequence in file UHRF1_promoter_region.txt).

The PWM is provided in the file E2F1_motif.txt. Your Python script should store the PWM as a dictionary.


3. Finding E2F1 binding sites in ChIP-seq peaks (15 pt)

Write a Python script to find E2F1 binding sites in genomic regions bound in vivo by E2F1, defined as the ChIP-seq peaks reported for E2F1 in HeLa S3 cells (data from ENCODE). These genomic regions are provided in a FASTA file: E2F1_ChIPseq_peaks.fa. For each sequence in this FASTA file identify the E2F1 binding sites (defined as matches to the consensus sequence TTTSSCGC) and print, to an output file, how many sites you found in each sequence. Remember to look on both strands! Use your Python script to determine how many of the ChIP-seq peaks have at least one E2F1 binding site. Is this a small or a large fraction of the total peaks?

4. Getting the genomic sequences associated with ChIP-seq peaks (10 pt)

Write a Python script to extract, from the human genome, the sequences associated with the ChIP-seq peaks reported in the file:
wgEncodeSydhTfbsHelas3E2f1StdPk.narrowPeak
The coordinates correspond to version 19 of the human genome (hg19 or GRCh37), which you can download from:
http://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/

Report the sequences in an output file in the FASTA format. For simplicity, you can limit the analysis to the first 5 sequences in the narrowPeak file.



