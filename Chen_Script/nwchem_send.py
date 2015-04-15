#!/usr/bin/env python

"""
Convenient job submit nwchem script for TSCC, the template is the standard submit_script.
which automatically generates submission scripts and sends them to the queue.
"""


__author__ = 'chenzheng'
__version__ = "1.0"
__email__ = "chz022@ucsd.edu"
__date__ = "Apr 14, 2015"

import os
import subprocess
import argparse
from monty.tempfile import ScratchDir


SCRATCH_ROOT = "/oasis/tscc/scratch/"
CWD = os.getcwd()
SUBMIT_FNAME = "submit_script"

TEMPLATE = """#!/bin/bash
#PBS -q {queue}
#PBS -N {name}
#PBS -l nodes={nnodes}:ppn={nproc}:{ibswitch}
#PBS -l walltime={walltime}
#PBS -o vasp.out
#PBS -e {name}.err
#PBS -V
#PBS -M {user}@ucsd.edu
#PBS -m {verbosity}
#PBS -A {account_name}
#PBS -d {dir}

#To run vasp, you need to load the nwchem module first.
module load nwchem

CURR_DIR=`pwd`

#You should always run your calculations on the scratch space.
#The next three lines create a unique scratch directory.
SCRATCH=/oasis/tscc/scratch/chz022/N2_nwchem_test/
mkdir $SCRATCH
cp * $SCRATCH
cd $SCRATCH

#This is the actual run command. VASP is run using mpirun.

mpirun -machinefile $PBS_NODEFILE -np 16 /opt/nwchem/bin/nwchem {Input_File} > {Output_File}

#This moves the completed calculation back to the working directory and cleanup.
mv * $CURR_DIR
"""

walltime_settings={
    'home':(24,240),
    'hotel':(24,168),
    'condo':(8,8),
    'glean':(24,240)
}


pjoin = os.path.join

tempscratch = pjoin(SCRATCH_ROOT, os.environ["USER"])

