#Import Stuff
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from plotnine import *
#Set JSH WD
os.chdir('C:\\Users\\joshu\\OneDrive\\github\\BioComp\\Intro_Biocomp_ND_318_Tutorial7\\')
#reference lecture 11 and lecture 11 fasta
#Part1
#sudo code:
#import packages
#read in the fasta file (four things below)
#plan for storing info
#1 sequence ID, sequence length, % GC, Melting temp
#for loop (to collect ID, > is the header line vs a sequencel line)
    #if ">" in line:
        #capture sequence id
    #else next line:
#2 Length
    #get length of line: float(len(line))
#3 % GC
    #count Gs: line.count("G")
    #count Cs: line count("C")
    # Calc % GC (#G+c/length)
#4 Melting Temp
    #if length <=14:
        #calc melt temp
    #else:
        #-9999 (because instructions said so)
#summarize stored info

