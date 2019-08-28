# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:00:25 2019

@author: amirreza.sharifi
"""
###

#this is a new code to work with the new and old data format

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from Label import label
from makefig import makefig

Pollutant = ['E. Coli  MPN' , 'Escherichia coli'] #pick the right pollutant


#read first setion of the data
DB1 = pd.read_csv('1984-2018.csv',low_memory=False)
List1=['Monitoring Location ID' , 'Activity Start Date' , 'Characteristic Name' , 'Result Value','Result Unit']
DB1_sub = DB1[List1][DB1['Characteristic Name'].isin(Pollutant)]
DB1_sub=DB1_sub.dropna(axis=0)
DB1_sub = pd.DataFrame(DB1_sub.iloc[:,[0,1,3]])
DB1_sub.columns = ['station' , 'date' , 'E. Coli']
del DB1


#read second setion of the data
DB2 = pd.read_csv('Dec2018-onwards.csv',low_memory=False)
List2 = ['Station ' , 'Date M/D/Y' , 'E. Coli  MPN']  # pick the right column
DB2_sub = DB2[List2]
DB2_sub=DB2_sub.dropna(axis=0)
DB2_sub.columns = ['station' , 'date' , 'E. Coli']
del DB2


# join the databses
DB = pd.concat([DB1_sub,DB2_sub])
del DB1_sub , DB2_sub , List1 , List2

#clean up
DB['date']= pd.to_datetime(DB['date']) 
DB['month'] = DB['date'].dt.month
#remove <>
DB['E. Coli']=DB['E. Coli'].astype(str).str.replace('<', '')
DB['E. Coli']=DB['E. Coli'].astype(str).str.replace('>', '')
DB['E. Coli']=DB['E. Coli'].astype(str).str.replace('?', '')
DB['E. Coli']=DB['E. Coli'].astype(float)


#Label
label(DB)

#
Station = 'Potomac Mainstem'
Data = DB[DB['Watershed'] == Station]


makefig(Data , Station)





