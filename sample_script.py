#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from cartopy import crs as ccrs

# Open file
fname='data/JRR-AOD_v2r3_j01_s202009152044026_e202009152045271_c202009152113150_thinned.nc'
aod_file_id = Dataset(fname)

# Import variables
AOD_550 = aod_file_id.variables['AOD550'][:,:]
AOD_lat = aod_file_id.variables['Latitude'][:,:]
AOD_lon = aod_file_id.variables['Longitude'][:,:]

# Make figure
fig = plt.figure()
ax = plt.subplot()
co_plot = ax.contourf(AOD_lon, AOD_lat, AOD_550)
fig.colorbar(co_plot, orientation='horizontal')
plt.savefig("AOD_plot.png")
