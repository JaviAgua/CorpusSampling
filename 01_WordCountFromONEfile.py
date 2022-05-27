#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 22:00:21 2022

@author: javier aguado-orea
"""

# 01 Count the number of tokens and types in one file

# Input file:
#	A list of words or sentences into a txt file
#Output:
#	A number of tokens
#	A number of types


#A couple of lines to ask for the filename to read
txtfile = input('Enter file name:')
print(txtfile)


#"read" simply counts the number of words, so it computes the tokens
inputfile = open(txtfile, "rt")
data = inputfile.read()
words = data.split()
ntokens = len(words)

print('Number of tokens in text file :', ntokens)


#the next lines get the list of types
types = []
for word in words:
    if word not in types:
        types.append(word)

types.sort()
ntypes = len(types)
print('Number of types in text file :', ntypes)


ynprinttypes = input('Do you want to read the list of types? (y/n)')
if ynprinttypes == 'y':
    print (types)


print('FIN')