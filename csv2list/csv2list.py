import georinex as gr
import pandas as pd
import sys
import os
import math
import itertools
import numpy as np
import pytest
import xarray
from pytest import approx
from datetime import datetime, timedelta
import pymap3d as pr

sys.path.insert(0,'/FWC_module3')

from rinex2csv.rinex2csv import *
from str2float.str2float import *
from position.funcs import *
from conversions.funcs import *




rinex_file = "./data/gps.rnx"
output_file = './data/data.csv'

rinex_to_csv(rinex_file, output_file)


remove_empty_rows('./data/data.csv', './data/updated.csv')

df = pd.read_csv('./data/updated.csv')

GPSWeek = df['GPSWeek'].tolist()
Toe = df['Toe'].tolist()
Eccentricity= df['Eccentricity'].tolist()
sqrtA = df['sqrtA'].tolist()
Cic = df['Cic'].tolist()
Crc = df['Crc'].tolist()
Cis = df['Cis'].tolist()
Crs = df['Crs'].tolist()
Cuc = df['Cuc'].tolist()
Cus = df['Cus'].tolist()
DeltaN = df['DeltaN'].tolist()
Omega0 = df['Omega0'].tolist()
omega = df['omega'].tolist()
Io = df['Io'].tolist()
OmegaDot = df['OmegaDot'].tolist()
IDOT = df['IDOT'].tolist()
M0 = df['M0'].tolist()
TransTime = df['TransTime'].tolist()



data = list([(a, b, c) for a, b, c in list(zip(GPSWeek,Toe,Eccentricity,sqrtA,Cic,Crc,Cis,Crs,Cuc,Cus,DeltaN,Omega0,omega,Io,OmegaDot,IDOT,M0,TransTime))])

print(data)

np.savetxt("data/data.txt",data)
