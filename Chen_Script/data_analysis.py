__author__ = 'chenzheng'

import numpy as np
import pandas as pd

datafile = pd.read_csv('data_test_record_analysis_test.csv',header=0)

#Filter out H2 and N2 line using formation energy column NaN value
datafile = datafile[datafile.Formation_Enthalpy.notnull()]