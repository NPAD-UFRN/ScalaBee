#!/usr/bin/env python
# Arguments: numerOfTests program arg1Init-arg1Final arg2Init-arg2Final arg3Init-arg3Final...
# Ex: python scalaBee.py 2 ./examples/omp_pi 1,2,4,8 100000,1000000,10000000,100000000
# Dependencies: PrettyTable - pip install PrettyTable; 

# Importing everything needed
import os, sys, time

def getColumn(matrix, z):
    return [row[z] for row in matrix]

def getRow(matrix, z):
    return [col[z] for col in matrix]

## Showing initial message
print "=================\nStarting ScalaBee\n=================\n"

## Getting Parameters
numberOfTests=int(sys.argv[1])
program=sys.argv[2]
param1=sys.argv[3]
param2=sys.argv[4]
problemSize=param2.split(",")
threads=param1.split(",")

#Printing parameters on screen
print "Program:\t\t" + program 
print "Number of Tests:\t%d" % numberOfTests 
print "Number of threads:\t", threads 
print "Problem Size:\t\t", problemSize 
print "\n"

# Creating bidimentional arrays
average_time = [[0 for x in range(len(threads))] for y in range(len(problemSize))]
scalability=[[0 for x in range(len(threads))] for y in range(len(problemSize))]
efficiency=[[0 for x in range(len(threads))] for y in range(len(problemSize))]

# Running program and measuring time
from subprocess import call
for i in range(len(problemSize)):
	for j in range(len(threads)):
		start_time = time.time()
		for k in range(numberOfTests):
			call([program, threads[j] , problemSize[i]])
		average_time[i][j] = (time.time() - start_time)/numberOfTests
		print "Elapsed time: %.3fs\n" % average_time[i][j]

# Calculate Scalability and Efficiency
for i in range(len(problemSize)):
	for j in range(len(threads)):
		scalability[i][j]=average_time[i][0]/average_time[i][j]
		efficiency[i][j]=scalability[i][j]/(int(threads[j]))

# Printing Average Time table
from prettytable import PrettyTable
average_time_t = PrettyTable(['Problem Size / Threads']+threads)
scalability_t = PrettyTable(['Problem Size / Threads']+threads)
efficiency_t = PrettyTable(['Problem Size / Threads']+threads)
for i in range(len(problemSize)):
	average_time_t.add_row([problemSize[i]]+average_time[i])
	scalability_t.add_row([problemSize[i]]+scalability[i])
	efficiency_t.add_row([problemSize[i]]+efficiency[i])
print "AVERAGE TIME IN SECONDS"
print average_time_t
print "\nSCALABILITY"
print scalability_t
print "\nEFFICIENCY"
print efficiency_t

