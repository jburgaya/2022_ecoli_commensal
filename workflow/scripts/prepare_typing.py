#!/usr/bin/env python

'''Get full dataset info'''

def get_options():
    import argparse

    description = 'Get full dataset info'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('metadata',
                        help='Dataset with phenotype and covariates info')
    parser.add_argument('phylogroup',
                        help='Dataset with phylogroupy info (output from ClermonTyping)')
    parser.add_argument('st',
                        help='Dataset with ST info (output from mlst)')
#    parser.add_argument('typing',
#                        help='Clinical dataset with ST and phylogroup')
    
    return parser.parse_args()
    args.method

if __name__ == "__main__":
    options = get_options()

    import sys
    import os.path
    import pandas as pd

    # read files
    m = pd.read_csv(options.metadata, sep='\t')
    p = pd.read_csv(options.phylogroup, header=None, sep='\t')
    s = pd.read_csv(options.st, header=None, sep='\t')
#    j = pd.read_csv(options.typing, sep=',')

    # rename columns in phylogroup and st files
    p = p.rename(columns={0:'code_rangement', 1:'phylogroup'})
    s = s.rename(columns={0:'code_rangement', 1:'st'})

    # prepare Julie data
#    j.drop(j.tail(7).index, inplace=True)
#    j.drop(j.head(2).index, inplace=True)
#    j.columns = j.iloc[0]
#    j.drop(j.head(1).index, inplace=True)

    # get columns of interest
#    ty = j[['Strain', 'Phylogroup', 'ST (Warwick)', 'ST (Pasteur)', 'Serotype (O:H)', 'FimH allele']]
    # reencode
#    ty = ty.rename(columns={'Strain':'code_rangement', 'Phylogroup':'j_phylogroup',
#                            'ST (Warwick)':'j_st_w', 'ST (Pasteur)':'j_st_p',
#                            'Serotype (O:H)':'j_OH', 'FimH allele':'j_fimh'})

    # merge datasets on column 'code_rangement'
    f1 = pd.merge(p, s, on='code_rangement', how='left')
    f2 = pd.merge(m, f1, on='code_rangement', how='left')
#    f3 = pd.merge(j, f2, on='code_rangement', how='left')

    # reorder columns
#    tp = f3[['code_rangement', 'commensal', 'date_after2010', 'age_more60', 'female', 'pe_urinaire', 'pe_digestive', 'ceremi',
#             'coliville', 'LBC', 'PAR', 'ROAR', 'septicoli', 'colibafi', 'phylogroup', 'j_phylogroup', 'st', 'j_st_w', 'j_st_p',
#             'j_OH', 'j_fimh']]

    # save
    f2.to_csv(sys.stdout, sep='\t', index=False)
