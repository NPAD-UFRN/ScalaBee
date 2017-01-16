#!/usr/bin/env python
# Arguments: python scalaBee.py numerOfTests program arg1Init-arg1Final arg2Init-arg2Final arg3Init-arg3Final...
# Ex: python scalaBee.py +nTe 3 ./examples/omp_pi {t8} {p{10000,100000,1000000}}
# Dependencies: PrettyTable - pip install PrettyTable; Matplotlib - pip install matplotlib

# Importing everything needed
import os, sys, time, argparse, re
import matplotlib.pyplot as plt
from math import log
from subprocess import call
from prettytable import PrettyTable
from matplotlib.ticker import MultipleLocator, FuncFormatter
from argparse import RawTextHelpFormatter

## Showing initial message
print "=================\nStarting ScalaBee\n=================\n"

## Getting Parameters
parser = argparse.ArgumentParser(description='https://github.com/danielholanda/ScalaBee',
								prefix_chars='+',
								formatter_class=RawTextHelpFormatter)
parser.add_argument('program', metavar='Prog', 
                    help='Your program\n    Example: .\\myProgram')
parser.add_argument('funcArguments', metavar='Arg', nargs='+',
                    help='Your program arguments \n'
                    '    Use {t4} or {t8} or {t16} or {t32} or ... istead of your thread number\n'
                    '    Use {p{size1,size2,...}} to indicate the problem sizes')
parser.add_argument('+nTe', metavar='numberOfTests', type=int,
                    help='Number of tests to be performed for each sample',default=1)
args = parser.parse_args()

# Find string with pattern {key{S,T,R,I,N,G}}
# Note that argFlag={p{154,123}} is read as argFlag={p154} argFlag={p123}
def findArg(input_list,key):
	argList = []
	argIndexList = []
	argFlag =''
	for i in range(len(input_list)):
		bracket_level = 0
		current = ''
		for index, c in enumerate(input_list[i]):
			if c == "{" and (bracket_level==0):
			    bracket_level += 1
			    initialChar = index
			elif c == key and bracket_level==1:
			    bracket_level += 1
			elif c != "}" and bracket_level==2:
			    current+=c
			elif c == "}" and bracket_level==2:
				argList.append(current)
				argFlag = input_list[i][:initialChar]
				argIndexList.append(i)
				break
			else:
				bracket_level==0				
	return argList, argFlag, argIndexList

# Filtering Parameters
threads, threadsFlag, threadsIndexList = findArg(args.funcArguments,'t')
problemSize, problemSizeFlag, problemSizeIndexList = findArg(args.funcArguments,'p')
numberOfTests=args.nTe
program=args.program

# Error Messages
if not threads:
	print "Number of threads not found. Exiting Program."
	exit()

if not problemSize:
	print "Problem Size not found. Assuming 1."
	problemSize = ['1']

# Transforming {t8} in {t1}{t2}{t4}{t8}
if len(threads)==1:
	aux=log(float(threads[0]),2)
	threads=[]
	for i in range(int(aux)+1):
		threads.append(str(2**i))

# Printing parameters on screen
print "Program:\t\t" + program 
print "Number of Tests:\t%d" % numberOfTests 
print "Number of threads:\t", threadsFlag, threads 
print "Problem Size:\t\t", problemSizeFlag, problemSize 
print "\n"

# Creating bidimentional arrays
average_time = [[0 for x in range(len(threads))] for y in range(len(problemSize))]
scalability=[[0 for x in range(len(threads))] for y in range(len(problemSize))]
efficiency=[[0 for x in range(len(threads))] for y in range(len(problemSize))]

# Running program and measuring time
for i in range(len(problemSize)):
	for j in range(len(threads)):
		#Creating command to run
		callCmd = args.funcArguments[:]
		callCmd[threadsIndexList[0]]=threadsFlag+threads[j]
		if problemSizeIndexList:
			callCmd[problemSizeIndexList[0]]=problemSizeFlag+problemSize[i]
			if len(problemSizeIndexList)>1:
				del callCmd[problemSizeIndexList[1]:problemSizeIndexList[-1]+1]
		#Running the program
		start_time = time.time()
		for k in range(numberOfTests):
			call([program]+callCmd)
		average_time[i][j] = (time.time() - start_time)/numberOfTests
		print "Average elapsed time per call: %.3fs\n" % average_time[i][j]

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
plt.subplot(412)
threadsPower2=[log(float(y),2) for y in threads];
scalabilityPower2=[[0 for x in range(len(threads))] for y in range(len(problemSize))]
for i in range(len(problemSize)):
	scalabilityPower2[i]=[log(float(y),2) for y in scalability[i]];
plt.suptitle('ScalaBee - Time, Scalability & Efficiency', fontsize=14, fontweight='bold')
for i in range(len(problemSize)):
	plt.semilogy(threadsPower2,average_time[i], 'o-', label=problemSize[i])
plt.ylabel('Average Time in s')
plt.xlabel('Threads')
plt.legend(bbox_to_anchor=(0., 1.3, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=.0)
plt.grid(True)
ax=plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: int(2**x)))
plt.subplot(413)
for i in range(len(problemSize)):
	plt.plot(threadsPower2,scalabilityPower2[i],'o-')
plt.ylabel('Scalability')
plt.xlabel('Threads')
plt.grid(True)
ax=plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: int(2**x)))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: int(2**y)))
plt.subplot(414)
for i in range(len(problemSize)):
	plt.plot(threadsPower2,efficiency[i], 'o-')
plt.ylabel('Efficiency')
plt.xlabel('Threads')
plt.grid(True)
plt.tight_layout()
ax=plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: int(2**x)))
ax.yaxis.set_major_locator(MultipleLocator(.2))
plt.show()