# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 08:53:00 2021

@author: Colby
"""

import zipfile

# Specify file locations

path_base = 'C:/Eden/AQI/zip_data/'
file_base = 'daily_aqi_by_county_'
dest_base = 'C:/Eden/AQI/raw_data/'


# Get range of years to iterate on
years = range(2021, 1999, -1)



for y in years:
    
    # Specify temporary paths
    
    final_file_path = path_base + file_base + str(y) + ".zip"
    dest_file_path = dest_base
    #print(final_file_path)
    #print(dest_file_path)
    
    
    # Open file and extract all to destination location
    
    with zipfile.ZipFile(final_file_path, 'r') as zip_ref:
        zip_ref.extractall(dest_file_path)