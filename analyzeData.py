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





data_file_path = 'C:/Eden/aqi/subset_aqi_az.csv'

raw_data_df = pd.read_csv(data_file_path)

raw_data_df["Date"] = pd.to_datetime(raw_data_df["Date"])


# Option alters display to show all column values
#pd.set_option('display.max_columns', None)


# Take a look into what values are within the data
for col in raw_data_df.columns:
    print("Column:",col)
    print(pd.unique(raw_data_df[col]))





# Take a subset to work with
tmp_df = raw_data_df.loc[raw_data_df["county Name"]=="Maricopa",["Date","AQI"]].sort_values(by=["Date"])
subset_tmp_df = tmp_df[tmp_df["Date"]>"2016-01-01"]
#plt.plot(subset_tmp_df["Date"],subset_tmp_df["AQI"])









# Alter figure size to get a better look
plt.figure(figsize=(20, 15))
plt.plot(subset_tmp_df["Date"],subset_tmp_df["AQI"])


# Add formatting to the figure
plt.xlabel("Date")
plt.ylabel("AQI")
plt.title("AQI (Maricopa) 2016 - June 2021")

# Attempt to customize the x axis dates to be by 6 month - WIP
plt.xlim(min(subset_tmp_df["Date"])-1, max(subset_tmp_df["Date"])+1)

plt.show()





# Alter figure size to get a better look
plt.figure(figsize=(30, 15))
plt.plot(tmp_df["Date"],tmp_df["AQI"])


# Add formatting to the figure
plt.xlabel("Date")
plt.ylabel("AQI")
plt.title("AQI (Maricopa) 2000 - June 2021")


plt.show()





# More complicated Graph 
#import matplotlib.dates as mdates
#
#fig, ax = plt.subplots()
#fig.set_size_inches(18.5, 10.5)
#ax.plot('Date', 'AQI', data = subset_tmp_df)
#
#frmt_half_year = mdates.MonthLocator(interval=6)
#ax.xaxis.set_major_locator(frmt_half_year)
#
## Minor ticks every month.
#frmt_month = mdates.MonthLocator()
#ax.xaxis.set_minor_locator(frmt_month)
#
## Text in the x axis will be displayed in 'YYYY-mm' format.
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
#
#
## Round to nearest years.
#datemin = np.datetime64(subset_tmp_df['Date'][0], 'Y')
#datemax = np.datetime64(subset_tmp_df['Date'][-1], 'Y') + np.timedelta64(1, 'Y')
#ax.set_xlim(datemin, datemax)
#
## Format the coords message box, i.e. the numbers displayed as the cursor moves
## across the axes within the interactive GUI.
#ax.format_xdata = mdates.DateFormatter('%Y-%m')
#ax.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
#ax.grid(True)
#
#fig.autofmt_xdate()
#
#plt.show()