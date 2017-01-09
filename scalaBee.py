#!/usr/bin/env python
# Arguments: numerOfTests program arg1Init-arg1Final arg2Init-arg2Final arg3Init-arg3Final...
# Ex: python scalaBee.py 2 ./examples/omp_pi 1,2,4,8 100000,1000000,10000000,100000000
# Dependencies: PrettyTable - pip install PrettyTable; Matplotlib - pip install matplotlib

# Importing everything needed
import os, sys, time
from subprocess import call
from prettytable import PrettyTable
import matplotlib.pyplot as plt

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

# Formatting Data to a more readable format
for i in range(len(problemSize)):
	for j in range(len(threads)):
		average_time[i][j]="{:.3f}".format(average_time[i][j])
		scalability[i][j]="{:.3f}".format(scalability[i][j])
		efficiency[i][j]="{:.3f}".format(efficiency[i][j])

# Creating tables to print
average_time_t = PrettyTable(['Problem Size / Threads']+threads)
scalability_t = PrettyTable(['Problem Size / Threads']+threads)
efficiency_t = PrettyTable(['Problem Size / Threads']+threads)
for i in range(len(problemSize)):
	average_time_t.add_row([problemSize[i]]+average_time[i])
	scalability_t.add_row([problemSize[i]]+scalability[i])
	efficiency_t.add_row([problemSize[i]]+efficiency[i])

# Printing tables
print "AVERAGE TIME IN SECONDS"
print average_time_t
print "\nSCALABILITY"
print scalability_t
print "\nEFFICIENCY"
print efficiency_t

# Creating plot results
plt.figure(1)
plt.subplot(311)
for i in range(len(problemSize)):
	plt.plot(threads,average_time[i])
plt.ylabel('Average Time in s')
plt.subplot(312)
for i in range(len(problemSize)):
	plt.plot(threads,scalability[i])
plt.ylabel('Scalability')
plt.subplot(313)
for i in range(len(problemSize)):
	plt.plot(threads,efficiency[i])
plt.ylabel('Efficiency')
plt.show()

