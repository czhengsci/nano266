#!/usr/bin/env python

"""
Used for template generation only

Author: Shyue Ping Ong
"""

import os
import shutil
import itertools
from monty.os import cd

pjoin = os.path.join

# Load the Si.pw.in.template file as a template.
with open("Fe.bcc.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k = [11] # k-point grid of 9x9x9
alat = [5.15,5.20,5.25,5.3,5.31,5.32,5.33,5.34,5.35,5.36,5.37,5.38,5.39,5.40,5.45,5.5,5.55] # The lattice parameter for the cell in Bohr.

# Loop through different k-points.
for k,alat in list(itertools.product(*[k, alat])):
    # This generates a string from the template with the parameters replaced
    # by the specified values.


    # Let's define an easy jobname.
    jobname = "Fe_bcc_%s_%s" % (alat, k)

    os.makedirs(jobname)

    with cd(jobname):
        os.makedirs('tmp')
        tmp_folder = pjoin(os.getcwd(),'tmp/')
        s = template.format(alat=alat, k=k,tmp_folder=tmp_folder)
        # Write the actual input file for PWSCF.
        with open("%s.pw.in" % jobname, "w") as f:
            f.write(s)
        os.system("cp ../Fe.pbe-spn-kjpaw_psl.0.2.1.UPF .")

    #Print some status messages.
    # print("Running with alat = %s, k1 = %s, k3 = %s, ca_ratio = %s ..." % (alat, k1, k3, ca_ratio))

    print("Template generated with alat = %s, k = %s..." % (alat, k))