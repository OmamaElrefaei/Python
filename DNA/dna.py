#A program that identifies a person based on their DNA.

"""
Created on Friday, January 17, 5:08 AM 2020

@author: Omama Elrefaei: my solution to a HarvardX: CS50 problem
"""

import csv
from sys import argv, exit


def main():
    
    # Check for invalid usage
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # initializing the titles and rows list
    rows = []
    dna = dict()
    individual = ''

    #open a CSV file and with keyword, will close the file for us:
    with open(argv[1], 'r') as csvfile:
        NameCSVFile = csv.reader(csvfile, delimiter=',')

        # extracting each data row one by one
        for row in NameCSVFile:
            rows.append(row)

    length = NameCSVFile.line_num
    width = len(rows[0])

    for i in range(1, length):
        dna[rows[i][0]] = STC(rows, width, i)

    if argv[1] == "databases/small.csv":
        for name in dna.keys():
            if dna[name] == databases_small(argv[2]):
                individual = name

    elif argv[1] == "databases/large.csv":
        for name in dna.keys():
            if dna[name] == databases_large(argv[2]):
                individual = name

    if individual:
        print(individual)
    else:
        print("No match")

    exit(0)


#Compute the longest run of consecutive repeats of the STR in the DNA sequence for the small database:
def databases_small(DNASeq):

    DNA = open(DNASeq).read()
    length = len(DNA)

    d = dict()

    #Assume that the STR counts will not match more than one individual:
    d['AGATC'] = 1
    d['AATG'] = 1
    d['TATC'] = 1

    for i in range(length - 10):
        for STC in d.keys():
            if DNA[i: i + 5] == STC and DNA[i + 5: i + 10] == DNA[i: i + 5]:
                d[STC] += 1
            elif DNA[i: i + 4] == STC and DNA[i + 4: i + 8] == DNA[i: i + 4]:
                d[STC] += 1

    return d


#Compute the longest run of consecutive repeats of the STR in the DNA sequence for the large database:
def databases_large(DNASeq):

    DNA = open(DNASeq).read()
    length = len(DNA)

    d = dict()
    
    #Assume that the STR counts will not match more than one individual:
    d['AGATC'] = 1
    d['TTTTTTCT'] = 1
    d['AATG'] = 1
    d['TCTAG'] = 1
    d['GATA'] = 1
    d['TATC'] = 1
    d['GAAA'] = 1
    d['TCTG'] = 1

    for i in range(length - 16):
        for STC in d.keys():
            if DNA[i: i + 8] == STC and DNA[i + 8: i + 16] == DNA[i: i + 8]:
                d[STC] += 1
            elif DNA[i: i + 5] == STC and DNA[i + 5: i + 10] == DNA[i: i + 5]:
                d[STC] += 1
            elif DNA[i: i + 4] == STC and DNA[i + 4: i + 8] == DNA[i: i + 4]:
                d[STC] += 1

    return d

# extracting the word name through the first column and the STR sequences through the remaining columns.
def STC(data, line, num):
    d = dict()
    for j in range(1, line):
        d[data[0][j]] = int(data[num][j])
    return d


main()