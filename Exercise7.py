#Import Stufffff
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import re
from collections import Counter

#Set JSH WD and plot nine
os.chdir('C:\\Users\\joshu\\OneDrive\\github\\BioComp\\Intro_Biocomp_ND_318_Tutorial7\\')
from plotnine import *

#Set Om WD and plotnine
#os.chdir('/Users/omneelay/Desktop/Exercise7/Intro_Biocomp_ND_318_Tutorial7/')
#!pip install plotnine

#PART 1

# open fasta file
InFile=open("Lecture11.fasta","r")

sequenceID=[]
sequenceLength=[]
percentGC=[]

for Line in InFile:
    # remove newline character from file line
    Line=Line.strip()
    # if a sequence record
    if '>' in Line:
        # add the sequence ID (except the ">" character) to the sequenceID list
        sequenceID.append(Line[1:])
    # if a sequence line
    else:
        # get the number of characters in the sequence and convert to a float to avoid integer division
        seqLen=float(len(Line))
        # count the number of G's and C's
        nG=Line.count("G")
        nC=Line.count("C")
        # append values to the lists
        sequenceLength.append(seqLen)
        percentGC.append((nG+nC)/seqLen*100)

# close file
InFile.close()

#Histogram of Seq Length
plt.hist(sequenceLength)
plt.title("Histogram of Sequence Length")
plt.show()

#Histogram of GC Content
plt.hist(percentGC)
plt.title("Histogram of GC Content")
plt.show()


#PART 2
#pseudocode is below
#Get data, make into 2 columns
#Read data into python
PatsWL=pd.read_csv("data2.csv", sep='\t')
#for loop to count
SeptW=0
OctW=0
NovW=0
DecW=0
SeptL=0
OctL=0
NovL=0
DecL=0
for row in range(0,len(PatsWL)): 
    if PatsWL.iloc[row,0] == "Sept":
        if PatsWL.iloc[row,1] == 'W':
            SeptW = SeptW+1
        elif PatsWL.iloc[row,1] == 'L':
            SeptL = SeptL+1
    elif PatsWL.iloc[row,0] == "Oct":
        if PatsWL.iloc[row,1] == 'W':
            OctW = OctW+1
        elif PatsWL.iloc[row,1] == 'L':
            OctL = OctL+1 
    elif PatsWL.iloc[row,0] == "Nov":
        if PatsWL.iloc[row,1] == 'W':
            NovW = NovW+1
        elif PatsWL.iloc[row,1] == 'L':
            NovL = NovL+1 
    elif PatsWL.iloc[row,0] == "Dec":
        if PatsWL.iloc[row,1] == 'W':
            DecW = DecW+1
        elif PatsWL.iloc[row,1] == 'L':
            DecL = DecL+1 

WL=pd.DataFrame(np.array([SeptW, SeptL, OctW, OctL, NovW, NovL, DecW, DecL]).reshape((4,2)),columns=['Wins', 'Losses'])
WL['Month']=['Sept', 'Oct', 'Nov', 'Dec']
#Plot the data as a scatter plot and add trendline
    #pylab.plot(x,y,'o')
    #z = numpy.polyfit(x, y, 1)
    #p = numpy.poly1d(z)
    #pylab.plot(x,p(x),"r--")
WL.plot.bar() 
#WL.plot(x=['Wins','Loses'], y='Month', style='0') 

#PART 3
Data=pd.read_csv("data.txt", sep=',')
#calculate mean of all four population        
northaverage = Data.loc[Data['region'] == 'north', 'observations'].sum()/Data.loc[Data['region'] == 'north', 'observations'].count()
southaverage = Data.loc[Data['region'] == 'south', 'observations'].sum()/Data.loc[Data['region'] == 'south', 'observations'].count()
eastaverage = Data.loc[Data['region'] == 'east', 'observations'].sum()/Data.loc[Data['region'] == 'east', 'observations'].count()
westaverage = Data.loc[Data['region'] == 'west', 'observations'].sum()/Data.loc[Data['region'] == 'west', 'observations'].count()
#create barplot
#creat scatter plot using (geom_jitter()) to show observations within the populations
    
