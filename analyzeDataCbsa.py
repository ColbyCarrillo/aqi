# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:46:22 2021

@author: Colby
"""

 
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import datetime


# Read in two files written out in analyzeDataCbsa.oy
base_dir = "C:/Eden/AQI/"
part_1_file = "subset_cbsa_aqi_part1.csv"
part_2_file = "subset_cbsa_aqi_part2.csv"


df_1 = pd.read_csv(base_dir + part_1_file)
df_2 = pd.read_csv(base_dir + part_2_file)

final_df = pd.concat([df_1, df_2])


# Parse to pandas date
final_df["Date"] = pd.to_datetime(final_df["Date"])

final_df["Year"] = pd.DatetimeIndex(final_df["Date"]).year
final_df["Month"] = pd.DatetimeIndex(final_df["Date"]).month

uniq_states = pd.unique(final_df["State"])



# Attempting to plot the grouped by data (State, Year) in a averaged year timeseries
df_gb = final_df.groupby(["State"])["AQI"].mean().plot()


#final_df.groupby(["State", "Year"])["AQI"].mean().plot()



