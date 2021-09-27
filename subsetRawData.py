# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:13:54 2021

@author: Colby
"""

import os
import pandas as pd

# Specify variables to work with, one being a list of files in directory location

target_dir = "C:/Eden/AQI/raw_data/"
file_names = os.listdir(target_dir)


# Dataframe placeholder
final_df = pd.DataFrame()


for fi in file_names:
    
    # Load in temporary Dataframe and subset to only Arizona
    tmp_df = pd.read_csv(target_dir+fi)
    #print(tmp_df.columns)

    subset_tmp_df = tmp_df[tmp_df["State Name"]=="Arizona"]
    
    # Combine external Dataframe with temporary Dataframe
    final_df = pd.concat([final_df, subset_tmp_df])
    
    
# Write out csv of AZ only data
final_dir = "C:/Eden/AQI/"
final_file_name = "subset_aqi_az.csv"

final_df.to_csv(path_or_buf = final_dir + final_file_name, index = False)
