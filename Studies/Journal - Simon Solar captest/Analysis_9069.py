# PVCaptest analysis 
# Model vs Field data comparison for PV RESOLVE project.
## Based on DOE data prize sites 9069 (Simon Solar) and 7334 (Shine On Solar)
## Load Field data, SAM and DAS result files and run cap test
# Use solardatatools environment
# System 9069 details: system capacity (AC): 33MW. (DC): 38.6 MW
# Inverter channels: 40.  Inverter 7 approx temp. corr capacity: 800 kW
# 800kW * 40 inverters = 32MWdc

#In[]:
import pandas as pd
import matplotlib.pyplot as plt
import pvlib
import numpy as np
import os
from pathlib import Path
from datetime import datetime

plt.rcParams.update({'font.size': 22})
plt.rcParams['figure.figsize'] = (12, 4)

# %%
# https://pvcaptest.readthedocs.io/en/stable/examples/complete_capacity_test.html
import warnings
warnings.filterwarnings('ignore')

import pandas as pd

# import captest as pvc
import captest as ct
from captest import capdata as pvc
from bokeh.io import output_notebook, show

# uncomment below two lines to use cptest.scatter_hv in notebook
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')

#if working offline with the CapData.plot() method may fail
#run 'export BOKEH_RESOURCES=inline' at the command line before
#running the jupyter notebook

output_notebook()
# %%
pvdrdb_dir = r'C:\Users\cdeline\Documents\Archive\Fleets Data\PVDRDB_CACHE'

# %%
# Simon Solar 1-minute data
df_raw = pd.read_csv(os.path.join(pvdrdb_dir, '9069_ACPower.csv'), index_col='utc_measured_on')
df_raw.index = pd.to_datetime(df_raw.index).tz_localize('UTC').tz_convert('Etc/GMT+5')

# %%
# rename and combine reference cell
df_raw['reference_cell_poa_median'] = df_raw[[
       'reference_cell_01_poa_irradiance_(w/m2)_o_150232',
       'reference_cell_02_poa_irradiance_(w/m2)_o_150238',
       'reference_cell_03_poa_irradiance_(w/m2)_o_150235',
       'reference_cell_04_poa_irradiance_(w/m2)_o_150239',
       'reference_cell_05_poa_irradiance_(w/m2)_o_150236',
       'reference_cell_06_poa_irradiance_(w/m2)_o_150240',
       'reference_cell_08_poa_irradiance_(w/m2)_o_150241',
       'reference_cell_09_poa_irradiance_(w/m2)_o_150243',
       'reference_cell_10_poa_irradiance_(w/m2)_o_150244',
       'reference_cell_13_poa_irradiance_(w/m2)_o_150237']].median(axis=1)

# rename and combine module temperature sensors
df_raw['module_temperature_median'] = df_raw[[
        'thermocouple_01_back-of-module_temperature_(sensor_1)_(c)_o_150256',
        'thermocouple_02_back-of-module_temperature_(sensor_2)_(c)_o_150257',
        'thermocouple_02_back-of-module_temperature_(sensor_3)_(c)_o_150258',
        'thermocouple_03_back-of-module_temperature_(sensor_1)_(c)_o_150259',
        'thermocouple_05_back-of-module_temperature_(sensor_1)_(c)_o_150260',
        'thermocouple_06_back-of-module_temperature_(sensor_1)_(c)_o_150261',
        'thermocouple_06_back-of-module_temperature_(sensor_2)_(c)_o_150262',
        'thermocouple_06_back-of-module_temperature_(sensor_3)_(c)_o_150263',
        'thermocouple_06_back-of-module_temperature_(sensor_4)_(c)_o_150264',
        'thermocouple_06_back-of-module_temperature_(sensor_5)_(c)_o_150265',
        'thermocouple_08_back-of-module_temperature_(sensor_1)_(c)_o_150266',
        'thermocouple_08_back-of-module_temperature_(sensor_2)_(c)_o_150267',
        'thermocouple_08_back-of-module_temperature_(sensor_3)_(c)_o_150268',
        'thermocouple_09_back-of-module_temperature_(sensor_1)_(c)_o_150269',
        'thermocouple_10_back-of-module_temperature_(sensor_1)_(c)_o_150270']].median(axis=1)

# rename and combine ambient temperature sensors
df_raw['ambient_temperature_median'] = df_raw[[
        'weather_station_01_ambient_temperature_(sensor_1)_(c)_o_150245',
        'weather_station_01_ambient_temperature_(sensor_1)_(c)_o_150245',
        'weather_station_03_ambient_temperature_(sensor_1)_(c)_o_150246',
        'weather_station_05_ambient_temperature_(sensor_1)_(c)_o_150247',
        'weather_station_06_ambient_temperature_(sensor_1)_(c)_o_150248',
        'weather_station_06_ambient_temperature_(sensor_2)_(c)_o_150249',
        'weather_station_06_ambient_temperature_(sensor_3)_(c)_o_150250',
        'weather_station_06_ambient_temperature_(sensor_4)_(c)_o_150251',
        'weather_station_06_ambient_temperature_(sensor_5)_(c)_o_150252',
        'weather_station_09_ambient_temperature_(sensor_1)_(c)_o_150253',
        'weather_station_10_ambient_temperature_(sensor_1)_(c)_o_150254',
        'weather_station_12_ambient_temperature_(sensor_1)_(c)_o_150255']].median(axis=1)

# rename other sensor channels
df_raw.rename(columns={
    'reference_cell_01_poa_irradiance_(w/m2)_o_150232': 'reference_cell_poa_1',
    'meter_1_ac_power_(kw)_meter_151040': 'meter_1_ac_power_kw',
    'meter_2_ac_power_(kw)_meter_151053': 'meter_2_ac_power_kw',
    'pyranometer_(class_a)_02a_poa_irradiance_(w/m2)_o_150233': 'poa_irradiance_02a',
    'pyranometer_(class_a)_02b_poa_irradiance_(w/m2)_o_150234': 'poa_irradiance_02b',
    'pyranometer_(class_a)_08_poa_irradiance_(w/m2)_o_150242': 'poa_irradiance_08',
    'pyranometer_(class_a)_12_ghi_irradiance_(w/m2)_o_150231': 'ghi_irradiance',
    'wind_sensor_12b_wind_direction_o_150272': 'wind_direction_deg',
    'wind_sensor_12b_wind_speed_(m/s)_o_150271': 'wind_speed_ms'
}, inplace=True)
#%%
# Inverter data channels.  Rename each of these just inverter_1_ac_power_(kw).
for col in df_raw.columns:
    if 'inverter' in col and 'ac_power' in col:
        df_raw.rename(columns={col: col.split('_inv_')[0].replace(' ', '_')}, inplace=True)


# %%
# Save a subset of data.  Columns to include:
columns_to_include = [
 'meter_1_ac_power_kw',
 'meter_2_ac_power_kw',
 'poa_irradiance_02a',
 'poa_irradiance_02b',
 'poa_irradiance_08',
 'ghi_irradiance',
 'reference_cell_poa_median',
 'reference_cell_poa_1',
 'module_temperature_median',
 'ambient_temperature_median',
 'wind_direction_deg',
 'wind_speed_ms']

df_subset = df_raw[columns_to_include + 
                   [col for col in df_raw.columns 
                    if 'inverter' in col and 'ac_power' in col]]
df_subset.to_csv(os.path.join('data', '9069_subset.csv'))





# %%
# re-load the data
df_9069 = pd.read_csv(os.path.join('data', '9069_subset.csv'), index_col='utc_measured_on', 
                     parse_dates=True)

# monthly cumulative production for each string
mindate = pd.to_datetime(df_9069.index[0])
minmonth = mindate.month + mindate.year * 12
df_9069['sequential_month'] = (pd.to_datetime(df_9069.index).month + pd.to_datetime(df_9069.index).year * 12 - minmonth)

#%%
# run solardatatools analysis of 9069 data. 
# meter 1 data quality:0.34
# meter 2 data quality:0.98
# inverter 1 data quality:0.84
# inverter 7 data quality: 0.91. Consistent performance


from solardatatools import DataHandler
dh_9069 = DataHandler(df_9069)

#%%
dh_9069.run_pipeline(power_col='inverter_07_ac_power_(kw)') #meter_2_ac_power_kw
dh_9069.report()

#%% 
# plot results
dh_9069.plot_heatmap("filled")
dh_9069.plot_capacity_change_analysis();
dh_9069.plot_polar_transform(lat=33.6762, lon=-83.676,  tz_offset=-5);

#%%
# 
filtered = df_9069[df_9069['poa_irradiance_02b'] > 60].copy()
filtered['inverter_07_tcorr'] = filtered['inverter_07_ac_power_(kw)']/filtered['poa_irradiance_02b'] *1000 *(
             1-0.004*(25-filtered['module_temperature_median']))
plt.figure()
plt.plot(filtered['poa_irradiance_02b'], 
         filtered['inverter_07_tcorr'],
         'k.',alpha=0.1)
plt.xlabel('poa_02b')
plt.ylabel('DCkW_Tcorr / POA')
plt.ylim(0,1500)
# approximate capacity.  
filt2 = filtered[(filtered['poa_irradiance_02b'] > 950) &  
                 (filtered['poa_irradiance_02b'] < 1050) & 
                 (filtered['inverter_07_ac_power_(kw)'] > 700) & 
                  (filtered['inverter_07_ac_power_(kw)'] < 1000)].copy()
print(f'Inverter 7 approx DC capacity: {filt2['inverter_07_tcorr'].mean():0.2f} kW')




# %%
# Calculate performance ratio for each inverter and meter channel

# performance ratio - define as separate function. 
def addPR(df, poa_col='reference_cell_poa_median', power_col = 'inverter_07_ac_power_(kw)'):
    df['Yr'] = df[poa_col] / 1000
    df['Yf']
    

    df['YfEMono'] = df.dc_power1 / 1740 #1760
    df['YfEBifi'] = df.dc_power2 / 1740 #1758
    df['YfXMono'] = df.dc_power4 / 1840 #1887
    df['YfXBifi'] = df.dc_power3 / 1840 #1868
    df['YfEModel'] = df.SunPower_SPR_E20_435_COM_modeled / 1740
    df['YfXModel'] = df.SunPower_SPR_X22_460_COM_modeled / 1840

    

    df['YrRatio'] = df.YrBack / df.Yr
    df['X/E'] = df.YfXMono / df.YfEMono

    df['EBifiRatio'] = df.dc_power2 / 1758 / (df.dc_power1 / 1760 )
    df['XBifiRatio'] = df.dc_power3 / 1868 / (df.dc_power4 / 1887 )#df.YfXBifi / df.YfXMono
    df['EMonoPR'] = df.YfEMono / df.Yr
    df['EBifiPR'] = df.YfEBifi / df.Yr
    df['XMonoPR'] = df.YfXMono / df.Yr
    df['XBifiPR'] = df.YfXBifi / df.Yr
    
    df['EModelPR'] = df.YfEModel / df.Yr
    df['XModelPR'] = df.YfXModel / df.Yr

    
    return df

# group by month values - define as separate function. 
def add_month_values(df):
    
    df['sequential_month'] = df.index
    # save the month and year in mm-yy format
    from dateutil.relativedelta import relativedelta
    df['mmyy'] = df['sequential_month'].apply(lambda x: (mindate + relativedelta(months=+x)).strftime("%m-%y"))

    # also save the month name
    df['month'] = df['sequential_month'].apply(lambda x: (mindate + relativedelta(months=+x)).strftime("%b"))
    return df