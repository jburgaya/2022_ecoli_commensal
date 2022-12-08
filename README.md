# Snakemake workflow for wg-GWAS on _E. coli_ commensal and BSI

Bacterial wg-GWAS for the detection of E. coli BSI and commensal genetic determinants

Snakemake workflow to reproduce the whole-genome (wg) GWAS analysis on the genetic determinants of *E. coli* bloodstream infections (BSI) and commensal isolates.

## Input genomes
The input assemblies can be found under the following bioproject accessions:

| Phenotype | Bioproject accession |
| ------------- | ------------- |
| BSI | [PRJEB39260](https://www.ebi.ac.uk/ena/browser/view/PRJEB39260), [PRJEB35745](https://www.ebi.ac.uk/ena/browser/view/PRJEB39260) |
| Commensal | [PRJEB38489](https://www.ebi.ac.uk/ena/browser/view/PRJEB38489), [PRJEB44819](https://www.ebi.ac.uk/ena/browser/view/PRJEB44819), [PRJEB44872](https://www.ebi.ac.uk/ena/browser/view/PRJEB44872), [PRJEB39252](https://www.ebi.ac.uk/ena/browser/view/PRJEB39252), [PRJEB55584] |

## Usage
To make a dry run of the analyis:
```
snakemake --use-conda --cores 36 -n -p
```
Snakemake will install the appropriate packages for each step as conda environments. symbolic link to a directory containing the eggnog-mapper database should be placed in data/eggnog-mapper, as well as a symbolic link to the unzipped fasta file from uniref50 (data/uniref50.fasta).

## Author
Judit Burgaya (BurgayaVentura.Judit@mh-hannover.de)
