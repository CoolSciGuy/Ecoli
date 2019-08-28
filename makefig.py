#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:25:18 2019

@author: amirrezasharifi
"""

def makefig1(Data, Station):
    
    import matplotlib.pyplot as plt 
    
    plt.figure(3, figsize = (12,6))
    Data.boxplot(column = ['E. Coli'],by='station' , figsize = (15,6),showfliers=False)
    
    
    plt.suptitle("")
    plt.title('Boxplot of Ambient E. Coli over stations in ' + Station)
    plt.gcf().autofmt_xdate()
 
    
    plt.ylim(0,2500)
    plt.ylabel('E. coli (MPN)')
    
    plt.suptitle("")
    plt.gcf().autofmt_xdate()
    
    plt.axhline(y=410, color='r', linestyle=':')
    plt.axhline(y=126, color='b', linestyle=':')
    plt.axhline(y=235, color='g', linestyle=':')
    plt.savefig(Station+" boxplot-by station", dpi=300  )

    
def makefig2(Data, Station):
    
    import matplotlib.pyplot as plt 
    
    fig = plt.figure(dpi=200 , figsize = (15,9))
    ax = fig.add_subplot(111    )
    
    plt.rcParams.update({'font.size': 9})
    
    title = 'Ambient E. coli in ' + Station
    plt.title(title)
    
    ax.grid(True)
    
    #sns.barplot(x='month' , y='E. Coli' , data=Data)    
    #sns.boxenplot(x="month", y='E. Coli', data=Data ,color =  'blue' )    
    #Data.plot( x= 'date' , y = 'E. Coli' ,alpha=0.1 , style = '.' , ax=ax)
    

    plt.scatter(x=Data['date'] , y=Data['E. Coli'] , marker = '.' , s=20 )
    
    
    
    #cooment to tser
    plt.ylim(0,2500)
    plt.ylabel('E. coli (MPN)')
    
    plt.suptitle("")
    plt.gcf().autofmt_xdate()
    
    plt.axhline(y=410, color='r', linestyle=':')
    plt.axhline(y=126, color='b', linestyle=':')
    plt.axhline(y=235, color='g', linestyle=':')
    plt.savefig(Station+" scatterplot")
    # plt.show()