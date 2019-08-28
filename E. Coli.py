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
from makefig import makefig1, makefig2

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

List0 = list(DB['Watershed'].unique())
List1 = [	"ANA01",	"ANA02",	"ANA03",	"ANA04",	"ANA05",	"ANA06",	"ANA07",	"ANA08",	"ANA09",	"ANA10",	"ANA11",	"ANA12",	"ANA13",	"ANA14",	"ANA15",	"ANA16","ANA28",	"ANA17",	"ANA18",	"ANA19",	"ANA20",	"ANA21",	"ANA21 ",	"ANA22",	"ANA23",	"ANA24",	"ANA25",	"ANA26",	"ANA27",	"ANA29",	"ANA30"]
List2 = ["PMS01",	"PMS02",	"PMS03",	"PMS05",	"PMS07",	"PMS08",	"PMS09",	"PMS10",	"PMS11",	"PMS12",	"PMS13",	"PMS16",	"PMS18",	"PMS21",	"PMS21 ",	"PMS23",	"PMS25",	"PMS27",	"PMS29",	"PMS31",	"PMS33",	"PMS35",	"PMS37",	"PMS39",	"PMS41",	"PMS44",	"PMS46",	"PMS48",	"PMS51" , "PMS52"]
List3 = ["RCR12","RCR01",	"RCR04","RCR07",	"RCR09"] # Rock Creek 

for Station in List0:

    Data = DB[DB['Watershed'] == Station]
    if (Data['E. Coli'].sum() != 0):

        makefig1(Data , Station)
#        makefig2(Data , Station)

    