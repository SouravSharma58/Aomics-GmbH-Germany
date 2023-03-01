import numpy as np
import pandas as pd
import argparse
from datetime import datetime
import matplotlib.pyplot as plt
from statistics import mean
from collections import defaultdict
from pprint import pprint
import warnings
import math
from matplotlib.backends.backend_pdf import PdfPages

def main():
    parser = argparse.ArgumentParser(description="A program for processing the trade raw files")
    parser.add_argument('-f', '--trading_file', type=str, required=True,
                        help='Please provide the input raw trading CSV file which is needed to be processed'
                             'Headers should be as first row of the file, and data should be in th')
    parser.add_argument('-re', '--reporter', type=str, required=True,
                        help='Please provide the reporter country name')
    parser.add_argument('-pa', '--partner', type=str, required=True,
                        help='Please provide the partner country name')
    parser.add_argument('-ocsv', '--output_file_csv', type=str, required=True,
                        help='Please provide the output file name where you want to store the processed file')
    args = parser.parse_args()

    delivarable7(args.reporter, args.partner, args.trading_file, args.output_file_csv)


def delivarable7(re, pa, trading , oc):
    #Import Data
    data = pd.read_csv(trading)
    del data['Unnamed: 0']
    data = data[data['PARTNER'] == 'GERMANY']
    d1 = data[data['DECLARANT'] =='INDIA']
    d2 = data[data['DECLARANT'] =='BANGLADESH']
    d3 = data[data['DECLARANT'] =='MYANMAR']
    d4 = data[data['DECLARANT'] =='NEPAL']
    d5 = data[data['DECLARANT'] =='VIETNAM']
    df = pd.concat([d1,d2,d3,d4,d5])
    df_export = df[df['FLOW']=='import']
    df_export['PERIOD'] = (df_export['PERIOD']/100).round(0)
    df_export_2019 = df_export[df_export['PERIOD']==2019.0]
    df_required=df_export_2019.sort_values('PERIOD', ascending=False).drop_duplicates(['PRODUCT_ID'])
    df_required=df_required.nlargest(5, ['VALUE_IN_EUROS'])
    print(df_required)
    fig, ax =plt.subplots(figsize=(6,8))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df_required.values,colLabels=df_required.columns,loc='center')
    pp = PdfPages(out)
    pp.savefig(fig, bbox_inches='tight')
    pp.close()
    

if __name__ == '__main__':
    main()