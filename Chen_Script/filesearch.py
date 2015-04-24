#!/usr/bin/env python
import os, fnmatch,csv,re

pjoin = os.path.join
matches = {}
csvfile_name = 'data_test_record_0417.csv'

def file_proc(filepath):
	match_line=[]
	with open(filepath,'r') as datafile:
		for line in datafile:
			line = line.rstrip()
			if re.search('Total DFT energy',line):
				match_line = line.lstrip()
                matchdata =[match_line.split('=')[1].lstrip()]

	return matchdata

def file_proc2(filepath):
    file = open(filepath,'r')
    matchdata=[]
    for line in file:
        if re.search('Total DFT energy',line):
            matchline=line.rstrip()
            matchdata.append(matchline)

    return matchdata[-1].split('=')[1].lstrip()

def correction(filepath):
    file = open(filepath,'r')
    matchdata=[]
    for line in file:
        if re.search('Thermal correction to Enthalpy',line):
            matchline=line.rstrip()
            matchdata.append(matchline)

    return (matchdata[0].split('=')[1].lstrip()).split(' ')[0]

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

def geometry(filepath):

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

def geometry_bond_N2_H2(filepath):

    file = open(filepath,'r')
    matchdata=[]

    for line in file:
        if re.search('Final and change from initial internal coordinates',line):
            for l in range(0,12):
                matchline=next(file)
            matchdata.append(matchline)


    datatopro = matchdata[0].split(' ')[-5]

    return datatopro

def csv_write(csvfile,datatowrite):
	with open(csvfile,'wb') as csvfile:
		datawriter = csv.writer(csvfile, dialect="excel")
		datawriter.writerows(datatowrite)

datatocsv=[['Compounds','Functional_Used','Functional_1','Functional_2','Basis_Set','Basis_Set_Part_1','Basis_Set_Part_2','Total_DFT_Energy (Ha)','Total_DFT_Energy (kcal/mol)',\
            'Thermal Correction to Enthalpy (kcal/mol)','Corrected Enthalpy','CPU Time','Wall Time','Output_File_Path','Geometry Angle (Degree)','Bond Length (Angstroms)']]

for root, dirnames, filenames in os.walk('.'):

    for filenames in fnmatch.filter(filenames, '*.nwout'):

        #Get the path of file and split the file with delimiter '/'
        filepath = pjoin(root,filenames)
        funcional_use = filepath.split('/')[1]
        functionstring= filepath.split('/')[-3]
        compound = filepath.split('/')[-2]
        function_set = functionstring.split('_')

        # #Extract used functional
        # functional1 = funcional_use.split('_')[0]
        # functional2 = funcional_use.split('_')[1]

        #Extract energy data, function set data
        Energy_line = file_proc2(filepath)
        Energy_kcal = float(Energy_line)*627.503


        #Extract Thermal correction to Enthalpy
        thermal_correction = correction(filepath)
        Correct_Enthalpy = float(thermal_correction) + Energy_kcal

        #Extract CPU time
        time = cpu(filepath)

        datatorecord = [compound,funcional_use]
        datatorecord.extend(funcional_use.split('_'))
        datatorecord.append(functionstring)
        datatorecord.extend(function_set)

        datatorecord.append(Energy_line)
        datatorecord.append(Energy_kcal)

        datatorecord.append(thermal_correction)
        datatorecord.append(Correct_Enthalpy)

        datatorecord.append(time[-2].rstrip('s'))
        datatorecord.append(time[-1].rstrip('s'))

        datatorecord.append(filepath)

        #extract angle data
        if filenames == 'NH3.nwout':
            angle = geometry(filepath)
            bond_len = geometry_bond_NH3(filepath)
            datatorecord.append(angle)
            datatorecord.append(bond_len)

        #extract angle and bond length data of H2 and N2
        if filenames =='N2.nwout' or filenames== 'H2.nwout':
            bond_len = geometry_bond_N2_H2(filepath)
            datatorecord.append(' ')
            datatorecord.append(bond_len)

        # print datatorecord
        datatocsv.append(datatorecord)
        # csv_write(csvfile_name,datatorecord)


        # data_element_type = dirnames
        # matches.append(os.path.join(root, filename))

csv_write(csvfile_name,datatocsv)