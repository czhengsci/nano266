#!/usr/bin/env python
import os,fnmatch,csv,re

pjoin = os.path.join
pattern = re.compile(r'Total DFT energy')
matchdata=[]

def file_proc(filepath):
	match_line=[]
	with open(filepath,'r') as datafile:
         data = datafile.read()
         for mathces in re.findall("Total DFT energy*",data):
            print mathces
	    # for line in datafile:
         #     match = pattern.findall(line)
        #
         #     if match:
         #        print match
        # line = line.rstrip()
		# if re.search('Total DFT energy',line):
		# 	match_line = line.lstrip()
        #    matchdata =[match_line.split('=')[1].lstrip()]

	# return matchdata


def file_proc2(filepath):
    file = open(filepath,'r')
    matchdata=[]
    for line in file:
        if re.search('Total DFT energy',line):
            matchline=line.rstrip()
            matchdata.append(matchline)

    print matchdata[-1].split('=')[1].lstrip()

def correction(filepath):
    file = open(filepath,'r')
    matchdata=[]
    for line in file:
        if re.search('Thermal correction to Enthalpy',line):
            matchline=line.rstrip()
            matchdata.append(matchline)

    return (matchdata[0].split('=')[1].lstrip()).split(' ')[0]
	# return matchdata

def cpu(filepath):
    file = open(filepath,'r')
    matchdata=[]
    time = []
    for line in file:
        if re.search('Total times',line):
            matchline=line.rstrip()
            matchdata.append(matchline)
    for element in matchdata[0].split(' '):
        if re.search('s',element):
            time.append(element)

    return time

def geometry_angle(filepath):

    file = open(filepath,'r')
    matchdata=[]

    for line in file:
        if re.search('angle',line):
            for l in range(0,6):
                matchline=next(file)
                matchdata.append(matchline)

    datatopro = matchdata[-9:-6]

    datatopro = [float(ele.split(' ')[-1].rstrip('\n')) for ele in datatopro]

    return sum(datatopro)/len(datatopro)

def geometry_bond_NH3(filepath):

    file = open(filepath,'r')
    matchdata=[]

    for line in file:
        if re.search('internuclear distances',line):
            for l in range(0,6):
                matchline=next(file)
                matchdata.append(matchline)

    datatopro = matchdata[-9:-6]

    datatopro = [float(ele.split(' ')[-1].rstrip('\n')) for ele in datatopro]

    return sum(datatopro)/len(datatopro)

def geometry_bond_N2(filepath):

    file = open(filepath,'r')
    matchdata=[]

    for line in file:
        if re.search('Final and change from initial internal coordinates',line):
            for l in range(0,12):
                matchline=next(file)
            matchdata.append(matchline)


    datatopro = matchdata[0].split(' ')[-5]

    return datatopro

for root, dirnames, filenames in os.walk('.'):

    for filenames in fnmatch.filter(filenames, '*.nwout'):
        filepath = pjoin(root,filenames)
        # file_proc2(filepath)
        print geometry_bond_N2(filepath)