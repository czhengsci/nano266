#!/usr/bin/env python
__author__ = 'chenzheng'

import os
import itertools
from H2_Temp_Gen import H2_temp_build
from N2_Temp_Gen import N2_temp_build
from NH3_Temp_Gen import NH3_temp_build

BASE_SET = ['HF','PBE','B3LYP']
POLARIZATION_FUNC = [['6-31G','6-31+G*'],['6-31G','6-31+G*'],['6-311G','6-311+G*']]
POLAR_FUNC_FOLDER = list(itertools.product(*POLARIZATION_FUNC))
CWD = os.getcwd()

if __name__=='__main__':

    for base_ele in BASE_SET:

        #Make directory for each base_set and change into the base_set directory before next for loop
        os.mkdir(base_ele)
        os.chdir(base_ele)

        #Get the base_ele folder path for subfolder creation
        base_ele_folder = os.getcwd()

        for sub_folder_ele in POLAR_FUNC_FOLDER:

            #Create subfolder based on element in combination list
            sub_foldername = '_'.join(sub_folder_ele)
            os.mkdir(sub_foldername)
            os.chdir(sub_foldername)


            #Record the current sub_folder path
            subfolder = os.getcwd()

            #Create H2 folder, cd into folder and created H2 input set based on base_ele tree it is in
            os.mkdir('H2')
            os.chdir('H2')
            H2_temp_build(base_ele)
            os.chdir(subfolder)

            #Creat N2 folder, cd into folder and created N2 input set with current base_ele
            os.mkdir('N2')
            os.chdir('N2')
            N2_temp_build(base_ele)
            os.chdir(subfolder)

            #Create NH3 folder
            os.mkdir('NH3')
            os.chdir('NH3')
            NH3_temp_build(base_ele,sub_folder_ele[0],sub_folder_ele[1],sub_folder_ele[2])

            #Change back to the base folder where we keep all subfolder and continue to make next subfolder with similar sturcture
            os.chdir(base_ele_folder)

        #After subfolder creating done, jump back to the initial folder where we keep all base_set folder
        os.chdir(CWD)





