#!/usr/bin/env python
__author__ = 'chenzheng'

import os
from monty.os import cd
import itertools
from H2_Temp_Gen import H2_temp_build
from N2_Temp_Gen import N2_temp_build
from NH3_Temp_Gen import NH3_temp_build

FUNCTIONALS = [['HFexch','xpbe96 cpbe96','B3LYP'],['HFexch','xpbe96 cpbe96','B3LYP']]
POLARIZATION_FUNC = [['6-31+G*','6-311+G*'],['6-31+G*','6-311+G*']]
POLAR_FUNC_FOLDER = list(itertools.product(*POLARIZATION_FUNC))
FUNCTIONALS_FOLDER = list(itertools.product(*FUNCTIONALS))
CWD = os.getcwd()

if __name__=='__main__':

    for functional_set in FUNCTIONALS_FOLDER:

        #Make directory for each functional and change into the functional directory before next for loop
        functional_foldername = '_'.join(functional_set)
        os.mkdir(functional_foldername)
        os.chdir(functional_foldername)

        #Get the functional folder path for subfolder creation
        functional_folder = os.getcwd()

        for sub_folder_ele in POLAR_FUNC_FOLDER:

            #Create subfolder based on element in combination list
            sub_foldername = '_'.join(sub_folder_ele)
            os.mkdir(sub_foldername)
            os.chdir(sub_foldername)


            #Record the current sub_folder path
            subfolder = os.getcwd()

            #Create H2 folder, cd into folder and created H2 input set based on base_ele tree it is in
            os.mkdir('H2')

            with cd('H2'):
                H2_temp_build(functional_set[0],functional_set[1],\
                              sub_folder_ele[0],sub_folder_ele[1])

            os.chdir(subfolder)

            #Creat N2 folder, cd into folder and created N2 input set with current base_ele
            os.mkdir('N2')
            with cd('N2'):
                N2_temp_build(functional_set[0],functional_set[1],\
                              sub_folder_ele[0],sub_folder_ele[1])

            os.chdir(subfolder)

            #Create NH3 folder
            os.mkdir('NH3')
            with cd('NH3'):
                NH3_temp_build(functional_set[0],functional_set[1],\
                               sub_folder_ele[0],sub_folder_ele[1])

            #Change back to the base folder where we keep all subfolder and continue to make next subfolder with similar sturcture
            os.chdir(functional_folder)

        #After subfolder creating done, jump back to the initial folder where we keep all functional_set folder
        os.chdir(CWD)





