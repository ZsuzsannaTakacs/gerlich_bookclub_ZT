import click
import pandas as pd
import os
import requests
import io

@click.command()
@click.option('--input', '-i', help='URL of public repository')
@click.option('--outdir', '-o', help='Path to output directory')
@click.option('--filename', '-fn', help='Name of file to save')

def tidy_data(input, outdir, filename):
    download = requests.get(input).content
    df = pd.read_csv(io.StringIO(download.decode('utf-8')), sep ='\t')
    df = pd.melt(df, id_vars = ['Absolute time'], value_vars = list(df.columns)[1:], var_name='trace')
    df['trace'] = df['trace'].str.replace('Trace', '').astype('float')
    df.to_csv(os.path.join(outdir, f"{filename}"), index=False)

if __name__ == '__main__':
    tidy_data()
