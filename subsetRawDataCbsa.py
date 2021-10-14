# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:13:54 2021

@author: Colby
"""

import os
import pandas as pd
import math

# Specify variables to work with, one being a list of files in directory location

target_dir = "C:/Eden/AQI/raw_data_cbsa/"
file_names = os.listdir(target_dir)


acceptable_states = ["AK", "AZ", "CA", "CO", "FL", "IL", "NY", "OR", "SC", "NC",\
                     "NV", "TN", "TX", "WA", "VA", "WV"]

# Dataframe placeholder
final_df = pd.DataFrame()



for fi in file_names:
    
    # Load in temporary Dataframe and subset to only Arizona
    tmp_df = pd.read_csv(target_dir+fi)
    #print(tmp_df.columns)
    
    tmp_df["State"] = tmp_df["CBSA"].str[-2:]
    
    subset_tmp_df = tmp_df[tmp_df["State"].isin(acceptable_states)]
    
    # Combine external Dataframe with temporary Dataframe
    final_df = pd.concat([final_df, subset_tmp_df])
    
    

print(final_df.shape)

# Splitting dataframe as over 1 million records - Not compatible with csv    
split = math.floor(final_df.shape[0]/2)   



df_splt_1 = final_df.iloc[:split,:]
df_splt_2 = final_df.iloc[split:,:]


# Write out csv of AZ only data
final_dir = "C:/Eden/AQI/"
final_file_name_1 = "subset_cbsa_aqi_part1.csv"
final_file_name_2 = "subset_cbsa_aqi_part2.csv"


# Write out of two dataframes
df_splt_1.to_csv(path_or_buf =  final_dir + final_file_name_1, index = False)
df_splt_2.to_csv(path_or_buf = final_dir + final_file_name_2, index = False)


