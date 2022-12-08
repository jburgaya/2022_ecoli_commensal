# Snakemake workflow for wg-GWAS on _E. coli_ commensal and BSI

Snakemake pipeline to reproduce the wg-GWAS analysis on the genetic determinants of *E. coli* bloodstream infections (BSI) and commensal isolates. Users wishing to replicate this study should place the data containig the phenotype and covariates within the `data/` directory.

## Input genomes
The input assemblies can be found under the following bioproject accessions:

| Phenotype | Bioproject accession |
| ------------- | ------------- |
| BSI | [PRJEB39260](https://www.ebi.ac.uk/ena/browser/view/PRJEB39260), [PRJEB35745](https://www.ebi.ac.uk/ena/browser/view/PRJEB39260) |
| Commensal | [PRJEB38489](https://www.ebi.ac.uk/ena/browser/view/PRJEB38489), [PRJEB44819](https://www.ebi.ac.uk/ena/browser/view/PRJEB44819), [PRJEB44872](https://www.ebi.ac.uk/ena/browser/view/PRJEB44872), [PRJEB39252](https://www.ebi.ac.uk/ena/browser/view/PRJEB39252), [PRJEB55584] |

The fasta files should be placed inside the `data/fastas` directory, and the annotated gff files in the `data/gffs` directory.

## Usage
To make a dry run of the analyis:
```
snakemake --use-conda --cores 36 -n -p
```
Snakemake will install the appropriate packages for each step as conda environments when running it without the `-n` flag.

A symbolic link to a directory containing the eggnog-mapper database should be placed in `data/eggnog-mapper`, as well as one to the unzipped fasta file from uniref50 (`data/uniref50.fasta`).

## Author
Judit Burgaya (BurgayaVentura.Judit@mh-hannover.de)
