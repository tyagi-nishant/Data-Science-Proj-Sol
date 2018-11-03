
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d25/391a2922ad597ba080f4b99dea6d62842562d64845ef5df1a384561e.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Noida, Uttar Pradesh, India**, and the stations the data comes from are shown on the map below.

# In[1]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(25,'391a2922ad597ba080f4b99dea6d62842562d64845ef5df1a384561e')


# In[3]:

get_ipython().magic('matplotlib notebook')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('data/C2A2_data/BinnedCsvs_d25/391a2922ad597ba080f4b99dea6d62842562d64845ef5df1a384561e.csv')
#data=data.dropna(if 'Date' contains)
data2015=data.where(data['Date'].str.contains('2015')).dropna()
data2015['Date']=data2015.Date.str[5:]
print (data2015.head())
data['Date']=data.Date.str[5:]
print (data.head())
data=data.where(data['Date']!='02-29')

record_high=data.groupby('Date')['Data_Value'].max()
print (record_high.head())
record_low=data.groupby('Date')['Data_Value'].min()
print (record_low.head())
high2015=data2015.groupby('Date')['Data_Value'].max()
print (high2015.head())
low2015=data.groupby('Date')['Data_Value'].min()
print (low2015.head())

observation_dates=list(range(1,366))
x=np.linspace(1,365,365)
y=np.linspace(1,365,365)

record_high2015=high2015[high2015>=record_high.reindex_like(high2015)]
print (record_high2015.head())
x=[n for n in range(0,365) if (high2015.iloc[n]>=record_high.iloc[n])]
print (x)
record_low2015=low2015[low2015<=record_low.reindex_like(low2015)]
y = [n for n in range (0,365) if (low2015.iloc[n]>=record_low.iloc[n])]
print (y)


plt.figure(figsize=(8,8))
ax1=plt.gca()
ax1.set_xlabel('Day of the year')
ax1.set_ylabel('Temperature (tenths of degree C)')
ax1.set_title('Record Highest and Lowest temperatures of the day in an year')
plt.plot(observation_dates, record_high,'-o',observation_dates,record_low,'-o',zorder=1)
ax1.legend('record high temperatures','record low temperatures')
plt.scatter(x,record_high2015,s=100,c='red',zorder=2,alpha=0.7)
plt.scatter(y,record_low2015,s=100,c='red',zorder=2,alpha=0.7)

ax1.legend(['record high temperatures','record low temperatures','record broken in 2015'])
ax1.fill_between(observation_dates,record_high,record_low,facecolor='green',alpha=0.25)
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.show()

