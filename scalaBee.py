#!/usr/bin/env python
## Arguments: numerOfTests program arg1Init-arg1Final arg2Init-arg2Final arg3Init-arg3Final...
## Ex: ./scalaBee 2 ./examples/omp_pi 1,2,4,8 100000,1000000,10000000,100000000

# Importing everything needed
import os
import sys


## Showing initial message
print "=================\nStarting ScalaBee\n=================\n"

## Getting Parameters


numberOfTests=sys.argv[1]
program=sys.argv[2]
param1=sys.argv[3]
param2=sys.argv[4]

problemSize=param2
threads=param1

print "Program:\t\t" +program 
print "Number of Tests:\t" + numberOfTests 
print "Number of threads:\t" + threads 
print "Problem Size:\t\t" + problemSize 