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
#path = "/home/ahmed/ISEScan_stats/summ_folder/"

#file_name ="hello"
############################################

all_files = glob.glob(os.path.join(path, "*.sum"))
df = [] # pd.concat takes a list of dataframes as an agrument

for csv in all_files:
    frame = pd.read_csv(csv,sep='\s+')
    frame['filename'] = os.path.basename(csv)
    df.append(frame)

df = pd.concat(df, ignore_index=True)

total = df['seqid'] == 'total'
df = df[~total]
df1 = df[['seqid','family']]

df1["Isolate"] = df["filename"].str.removesuffix(".fna.sum")
df1.columns = ["Elements","copy","Isolate"]

df9 = df1.groupby(by=["Isolate","Elements"])['copy'].sum().to_frame().reset_index()

df10=df9[['Elements','copy']]

df10 = df1.groupby(by=["Elements"])['copy'].sum().to_frame().reset_index()

df10 = df10.sort_values('copy', ascending=False)

#df10.to_excel("%s_copy_frequency.xlsx"%(file_name),index=False)
df10.to_csv("%s_copy_frequency.csv"%(file_name),index=False,sep=',')

#df2.to_excel("frequency.xlsx",index=False)
df11 = pd.crosstab(index=df9['Isolate'],columns=df9["Elements"],values=df9['copy'],aggfunc=sum)
df11 = df11.fillna(0)
df11.to_csv("%s_heatmap_copy.csv"%(file_name),index=True,sep=',')
#df11.to_excel("%s_heatmap_copy.csv"%(file_name),index=True)


