# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:38:22 2019

@author: amirreza.sharifi
"""

def label(DB):
    import numpy as np
    
    Condition1 = DB['station'].isin(["AAG01",	"AAG02",	"ANA01",	"ANA02",	"ANA03",	"ANA04",	"ANA05",	"ANA06",	"ANA07",	"ANA08",	"ANA09",	"ANA10",	"ANA11",	"ANA12",	"ANA13",	"ANA14",	"ANA15",	"ANA16","ANA28",	"ANA17",	"ANA18",	"ANA19",	"ANA20",	"ANA21",	"ANA21 ",	"ANA22",	"ANA23",	"ANA24",	"ANA25",	"ANA26",	"ANA27",	"ANA29",	"ANA30"]) # Anacostia
    Condition2 = DB['station'].isin(["TDU01",	"TFC01",	"TFD01",	"TFE01",	"TFS01",	"THR01",	"TNA01",	"TNS01",	"TOR01",	"TPB01",	"TTX27",	"TUT01",	"TWB01",	"TWB02",	"TWB03",	"TWB04",	"TWB05",	"TWB06" , "TFS01"]) #Anacostia Trib
    Condition3 = DB['station'].isin(["KNG01",	"KNG02"]) # Kingman Island
    Condition4 = DB['station'].isin(["PMS01",	"PMS02",	"PMS03",	"PMS05",	"PMS07",	"PMS08",	"PMS09",	"PMS10",	"PMS11",	"PMS12",	"PMS13",	"PMS16",	"PMS18",	"PMS21",	"PMS21 ",	"PMS23",	"PMS25",	"PMS27",	"PMS29",	"PMS31",	"PMS33",	"PMS35",	"PMS37",	"PMS39",	"PMS41",	"PMS44",	"PMS46",	"PMS48",	"PMS51" , "PMS52"]) # Potomac
    Condition5 = DB['station'].isin(["TBK01",	"TBR01", "TCO01", "TCO06" , "TDA01" , "TDO01" , "TFB01" , "TFB02"]) # Potomac Trib
    Condition6 = DB['station'].isin(["RCR12","RCR01",	"RCR04","RCR07",	"RCR09"]) # Rock Creek
    Condition7 = DB['station'].isin(["TKV01",	"TLU01",	"TMH01",	"TPI01",	"TPO01",	"TPY01",	"TSO01"]) # Rock Creek Trib
    Condition8 = DB['station'].isin(["PWC04"]) # Ship Channel
    Condition9 = DB['station'].isin(["PTB01"]) # Tidal Basin
    Condition10 = DB['station'].isin(["CHAIN"]) # USGS chain Bridge
    conditions = [Condition1 , Condition2,Condition3 , Condition4,Condition5 , Condition6, Condition7 , Condition8, Condition9,Condition10]
    choices = ['Anacostia Mainstem', 'Anacostia Tributary' , 'Kingman Lake' , 'Potomac Mainstem' , "Potomac Tributary" , "Rock Creek" , "Rock Creek Tributary" , "Ship Channel" , "Tidal Basin"   , "Chain Bridge (USGS)"   ]
    DB['Watershed'] = np.select(conditions, choices)
    return DB