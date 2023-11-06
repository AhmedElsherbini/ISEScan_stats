#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:11:16 2023

@author: ahmed
"""
#########################################
import pandas as pd
import glob
import os
import argparse
import warnings
#########################################
my_parser = argparse.ArgumentParser(description='Welcome!')
#print("example: $ python bakta_stat.py -i ./txt")



my_parser.add_argument('-i','--input_dir',
                       action='store',
                        metavar='input_dir',
                       type=str,
                       help="input_dir")

my_parser.add_argument('-p','--prefix',
                       action='store',
                        metavar='prefix',
                       type=str,
                       help="prefix")


###########################################
# Execute the parse_args() method
args = my_parser.parse_args()

###########################################
path  = args.input_dir

file_name = args.prefix
warnings.filterwarnings("ignore")

############################################
#path = "/media/ahmed/CC69-620B6/00_Ph.D/DATA_results/0_accolens_prop_database_work/0_analysis/5_ise/summary_insertion/sum"
#file_name ="hello"

all_files = glob.glob(os.path.join(path, "*.sum"))
df = [] # pd.concat takes a list of dataframes as an agrument

for csv in all_files:
    frame = pd.read_csv(csv,sep='\s+')
    frame['filename'] = os.path.basename(csv)
    df.append(frame)

df = pd.concat(df, ignore_index=True)

total = df['seqid'] == 'total'
df = df[~total]
df1 = df[['seqid']]

df1["Isolate"] = df["filename"].str.removesuffix(".fna.sum")
df1.columns = ["Elements", "Isolate"]

df2 =  df1[["Elements"]]


df2['freq'] = df2.groupby('Elements')['Elements'].transform('count')

df2 = df2.drop_duplicates(subset=['Elements'])


df2 = df2.sort_values('freq', ascending=False)

df2.to_excel("%s_frequency.xlsx"%(file_name),index=False)

#df2.to_excel("frequency.xlsx",index=False)


df3 = pd.crosstab(df1['Isolate'], df1['Elements'])

df3.to_excel("%s_heatmap.xlsx"%(file_name),index=True)


