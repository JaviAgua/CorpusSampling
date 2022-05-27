#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 22:00:21 2022

@author: javier aguado-orea
"""
# 01 Count the number of tokens and types in one file
# 02 Count the number of tokens and types in a second file

# Input files:
#	Two lists of words or sentences into two txt files
#Output:
#	Two numbers of tokens
#	Two number of types


#A couple of lines to ask for the first filename to read
txtfile1 = input('Enter name of FIRST file:')
print(txtfile1)

print()

txtfile2 = input('Enter name of SECOND file:')
print(txtfile2)


#"read" simply counts the number of words, so it computes the tokens
inputfile1 = open(txtfile1, "rt")
data = inputfile1.read()
words1 = data.split()
ntokens1 = len(words1)

inputfile2 = open(txtfile2, "rt")
data = inputfile2.read()
words2 = data.split()
ntokens2 = len(words2)


print('Number of tokens in FIRST text file :', ntokens1)
print('Number of tokens in SECOND text file :', ntokens2)



#the next lines get the list of types

types1 = []
for word in words1:
    if word not in types1:
        types1.append(word)

types1.sort()
ntypes1 = len(types1)

types2 = []
for word in words2:
    if word not in types2:
        types2.append(word)
                
types2.sort()
ntypes2 = len(types2)


print('Number of types in FIRST text file :', ntypes1)
print('Number of types in SECOND text file :', ntypes2)


ynprinttypes1 = input('Do you want to read the list of typesin the FIRST file? (y/n)')
if ynprinttypes1 == 'y':
    print (types1)
    
ynprinttypes2 = input('Do you want to read the list of typesin the SECOND file? (y/n)')
if ynprinttypes2 == 'y':
    print (types2)

print('FIN')