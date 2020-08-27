import pandas as pd
import os
import click

#input = "/groups/gerlich/members/ZsuzsannaTakacs/DataScience/PythonBookClub/Tidy_data_Homework/Localinput/"
#outdir = "/groups/gerlich/members/ZsuzsannaTakacs/DataScience/PythonBookClub/Tidy_data_Homework/Localinput/test/"
#suffix = "csv"

@click.command()
@click.option('--input', '-i', help='Path of input files')
@click.option('--outdir', '-o', help='Path of output directory')
@click.option('--suffix', '-s', help='File extension')

def tidy_data_local(input, outdir, suffix):
    for filename in os.listdir(input):
        if filename.endswith('txt'):
            with open(os.path.join(input, filename)) as f:
                df = pd.read_csv(f, sep = '\t')
                df = pd.melt(df, id_vars = "Absolute time", var_name='trace')
                df['trace'] = df['trace'].str.replace('Trace', '').astype('float')
                df.to_csv(os.path.join(outdir, f'{filename}_tidy.{suffix}'), index = False)

if __name__ == '__main__':
    tidy_data_local()