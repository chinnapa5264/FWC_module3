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




rinex_file = "./data/1.rnx"
output_file = './data/data.csv'

rinex_to_csv(rinex_file, output_file)


remove_empty_rows('./data/data.csv', './data/updated.csv')

df = pd.read_csv('./data/updated.csv')
sv = [0]#df ['sv'].tolist()
time=[0]
month=[0]
day =[0]
hour=[0]
minute =[0]
second=[0]
SVclockBias =df['SVclockBias'].tolist()
SVclockDrift=df['SVclockDrift'].tolist()
SVclockDriftRate=df['SVclockDriftRate'].tolist()
IODE = df['IODE'].tolist()
Crs = df['Crs'].tolist()
DeltaN = df['DeltaN'].tolist()
M0 = df['M0'].tolist()
Cuc = df['Cuc'].tolist()
Eccentricity= df['Eccentricity'].tolist()
Cus = df['Cus'].tolist()
sqrtA = df['sqrtA'].tolist()
Toe = df['Toe'].tolist()
Cic = df['Cic'].tolist()
Omega0 = df['Omega0'].tolist()
Cis = df['Cis'].tolist()
Io = df['Io'].tolist()
Crc = df['Crc'].tolist()
omega = df['omega'].tolist()
OmegaDot = df['OmegaDot'].tolist()
IDOT = df['IDOT'].tolist()
codesL2 = df['CodesL2'].tolist()
GPSWeek = df['GPSWeek'].tolist()
L2flag = df['L2Pflag'].tolist()
SVacc = df['SVacc'].tolist()
health = df['health'].tolist()
TGD = df['TGD'].tolist()
IODC =df['IODC'].tolist()
TransTime = df['TransTime'].tolist()

print(GPSWeek)

data = list([[a, b, c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag,ah,ai,] for a, b, c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag,ah,ai in list(zip(sv,time,month,day,hour,minute,second,SVclockBias,SVclockDrift,SVclockDriftRate,IODE,Crs,DeltaN,M0,Cuc,Eccentricity,Cus,sqrtA,Toe,Cic,Omega0,Cis,Io,Crc,omega,OmegaDot,IDOT,codesL2,GPSWeek,L2flag,SVacc,health,TGD,IODC,TransTime))])

print(data[0])

np.savetxt("data/data.txt",data)
