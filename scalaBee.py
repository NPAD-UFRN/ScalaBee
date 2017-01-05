#!/usr/bin/env python
# Arguments: numerOfTests program arg1Init-arg1Final arg2Init-arg2Final arg3Init-arg3Final...
# Ex: python scalaBee.py 2 ./examples/omp_pi 1,2,4,8 100000,1000000,10000000,100000000

# Importing everything needed
import os, sys, time


## Showing initial message
print "=================\nStarting ScalaBee\n=================\n"

## Getting Parameters
numberOfTests=int(sys.argv[1])
program=sys.argv[2]
param1=sys.argv[3]
param2=sys.argv[4]

problemSize=param2.split(",")
threads=param1.split(",")

print "Program:\t\t" + program 
print "Number of Tests:\t%d" % numberOfTests 
print "Number of threads:\t", threads 
print "Problem Size:\t\t", problemSize 
print "\n"

# Running program and measuring time

from subprocess import call

for i in range(len(problemSize)):
	for j in range(len(threads)):
		start_time = time.time()
		for k in range(numberOfTests):
			call([program, threads[j] , problemSize[i]])
		elapsed_time = time.time() - start_time
		print "Elapsed time: %.3fs\n" % elapsed_time