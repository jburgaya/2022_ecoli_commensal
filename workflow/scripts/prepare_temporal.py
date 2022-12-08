#!/usr/bin/env python

'''Get temporal sequences input - date < 2010'''

def get_options():
    import argparse

    description = 'Get temporal analysis input'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('data',
                        help='Commensal dataset')

    return parser.parse_args()
    args.method

if __name__ == "__main__":
    options = get_options()

    import sys
    import os.path
    import pandas as pd

    # read file
    m = pd.read_excel(options.data)

    # change dataset
    m = m.drop(t.tail(2).index)
    m = m[m.Strain != 'LBC22a'].reset_index()
    m = m[m.Collection != 'Ceremi']
    m = m[m.Collection != 'Coliville']
    del m['index']

    # rename columns
    m.rename(columns={'Sampling date':'date', 'Strain':'code_rangement', 
                  'Sex (M or F)':'sex', 'Age':'age'}, inplace=True)

    # Add column for commensal
    m['commensal'] = [1 if x == x
                      else 1
                      for x in m['Collection']]
    # Reencode columns
    m['age_more60'] = [0 if x == "18-50"
                    else 0 if x == "20-60"
                    else 0 if x == "18-22"
                    else 0 if x < 60
                    else 1 if x > 60
                    else np.nan
                    for x in m['age'].values]
    m['female'] = [1 if x == 'F'
                  else 0 if x == 'M'
                  else np.nan
                  for x in m['sex']]

    # Drop reencoded columns and extra columns
    m = m.drop(columns=['sex', 'age', 'Location'])
    m = m.drop(columns=['Socio-demography', 'ATB consomption', 'location'])

    # save
    m.to_csv(sys.stdout, sep='\t', index=False)
