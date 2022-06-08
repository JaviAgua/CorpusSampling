#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 22:00:21 2022

@author: javier aguado-orea
"""

# 01 Count the number of tokens and types in one file
# 02 Count the number of tokens and types in a second file
# 03 Compares the number of tokens and types in two files
# 04 Extract a random sample from the largest file

# Input file:
#	Two list of words or sentences into two txt files
#Output:
#	Two numbers of tokens
#	Two numbers of types
# The difference in tokens
# The difference in types

# Modules
import random
import re
import pandas as pd

#A couple of lines to ask for the first filename to read
txtfile1 = input('Enter name of FIRST file:')
msg1 = "The first file is "+txtfile1

txtfile2 = input('Enter name of SECOND file:')
msg2 = "The second file is "+txtfile2


#the txt files are now red as a dataset with two columns
data1 = pd.read_csv(txtfile1, sep="_", header = None)
data2 = pd.read_csv(txtfile2, sep="_", header = None)

#the columns are named as prefix and suffix variables
data1.columns = ["prefix", "suffix"]
data2.columns = ["prefix", "suffix"]

#Add a thrid column with both
data1["construction"] = data1[["prefix", "suffix"]].apply("_".join, axis=1)
data2["construction"] = data2[["prefix", "suffix"]].apply("_".join, axis=1)


#the frequencies of prefix and suffix are computed now
prefix_table1 = data1["prefix"].value_counts()
suffix_table1 = data1["suffix"].value_counts()
prefix_table2 = data2["prefix"].value_counts()
suffix_table2 = data2["suffix"].value_counts()

#number of tokens per file
ntokens1 = len(data1)
ntokens2 = len(data2)
msg3 = 'Number of tokens in FIRST text file :' + str(ntokens1)
msg4 = 'Number of tokens in SECOND text file :' + str(ntokens2)

#number of types per file and colum
ntypes_prefix1 = len(prefix_table1)
ntypes_prefix2 = len(prefix_table2)
ntypes_suffix1 = len(suffix_table1)
ntypes_suffix2 = len(suffix_table2)

msg5= 'Number of prefix types in FIRST text file :' + str(ntypes_prefix1)
msg6= 'Number of prefix types in SECOND text file :' + str(ntypes_prefix2)
msg7= 'Number of suffix types in FIRST text file :' + str(ntypes_suffix1)
msg8= 'Number of suffix types in SECOND text file :' + str(ntypes_suffix2)




ynprinttypes1 = input('Do you want to read the list of prefix types in the FIRST file? (y/n)')
if ynprinttypes1 == 'y':
    print (prefix_table1)    
ynprinttypes1 = input('Do you want to read the list of suffix types in the FIRST file? (y/n)')
if ynprinttypes1 == 'y':
    print (suffix_table1)    
ynprinttypes2 = input('Do you want to read the list of prefix types in the SECOND file? (y/n)')
if ynprinttypes2 == 'y':
    print (prefix_table2)
ynprinttypes1 = input('Do you want to read the list of suffix types in the SECOND file? (y/n)')
if ynprinttypes1 == 'y':
    print (suffix_table2)


# 03 Compares the number of tokens and types in two files starts here
# 04 Extract a random sample from the largest file starts here too

#Compare the two files
#First, compare tokens
tokendiff = ntokens2 - ntokens1

#def comparefilesfortokens(tokendiff):
if tokendiff == 0:
    #create a message
    msgtkn = 'Both files have the same size of tokens'
elif tokendiff > 0:
    #create a message
    msgtkn = 'SECOND file is ' + str(tokendiff) + ' tokens LARGER'
    #extract a sample from the second file
    txtfile2sample = data2['construction'].sample(n=abs(ntokens1), random_state=1)
    #sort the output
    txtfile2sample = txtfile2sample.sort_values()
    #create a name for the sample file
    txtfile2samplename = txtfile2[:-4]+'_sample.txt'
    #write the new file without the 'construction' header
    txtfile2sample.to_csv(txtfile2samplename, header=False, index=False)

    
elif tokendiff < 0:
    #create a message
    msgtkn = 'SECOND file is ' + str(abs(tokendiff)) + ' tokens SMALLER'
    #extract a sample from the first file
    txtfile1sample = data1['construction'].sample(n=abs(ntokens2), random_state=1)
    #sort the output
    txtfile1sample = txtfile1sample.sort_values()
    ####txtfile1sample.replace(',','\n')
    #create a name for the sample file
    txtfile1samplename = txtfile1[:-4]+'_sample.txt'
    #write the new file without the 'construction' header
    txtfile1sample.to_csv(txtfile1samplename, header=False, index=False)




# Feedback    
finalmsg = msg1 + "\r\n" + msg2 + "\r\n" + msg3 + "\r\n" + msg4 + "\r\n" + msg5 + "\r\n" + msg6 + "\r\n" + msg7 + "\r\n" + msg8 + "\r\n" + msgtkn




print(finalmsg)

