#!/usr/bin/env python

'''Get input files for mash'''

def get_options():
    import argparse

    description = 'Get the input file for mash'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('dataset',
                        help='File of the dataset')
    parser.add_argument('col',
                        help='Samples id column')

    return parser.parse_args()

if __name__ == "__main__":
    options = get_options()

    import sys
    import os.path
    import pandas as pd

    # read file
    f = pd.read_csv(options.dataset, sep='\t')
    f = f[options.col]

    # define common parts
    common = "data/fastas/"
    extension = ".fasta"

    # get path and input
    p = []
    for id in f:
        p.append(common+id+extension)
    
    m = '\n'.join([str(i) for i in p])

    # save
    with open("mash_input.txt", "w") as output:
        output.write(str(m))
