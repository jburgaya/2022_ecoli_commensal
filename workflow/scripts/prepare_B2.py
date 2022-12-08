#!/usr/bin/env python

'''Get B2 input'''

def get_options():
    import argparse

    description = 'Get B2 input'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('data',
                        help='Full dataset')

    return parser.parse_args()
    args.method

if __name__ == "__main__":
    options = get_options()

    import sys
    import os.path
    import pandas as pd

    # read file
    m = pd.read_csv(options.data, sep='\t')

    # get B2 strains
    m = m[m.phylogroup == "B2"]
    m = m[['code_rangement', 'ST']]
    
    # save
    m.to_csv(sys.stdout, sep='\t', index=False)
