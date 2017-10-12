#Import Stufffff
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import re

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
#df=pd.DataFrame(PatsWL, columns=["Month", "WinLoss"])
#count=df["WinLoss"].value_counts()
#Win = []
#Loss = []
PatsWL.groupby(by=[''])

#df.WinLoss.str.count(substr)
#WinLoss.str.contains(r'[W]')
#df.WinLoss.str.contains(r'[W]')
word_regexs=[r'W',r'L']
pd.Series((df.words.str.contains(r).sum() for r in word_regexs), word_regexs, name='count')
#create data frame with the data
#Plot the data as a scatter plot and add trendline
    #pylab.plot(x,y,'o')
    #z = numpy.polyfit(x, y, 1)
    #p = numpy.poly1d(z)
    #pylab.plot(x,p(x),"r--")
    