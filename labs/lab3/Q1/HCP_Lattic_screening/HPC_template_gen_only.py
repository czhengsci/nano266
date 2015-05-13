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
with open("Fe.hcp.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k1 = [9] # k-point grid of 8x8x8
alat = [4.7,4.71,4.72,4.73,4.74,4.75,4.76,4.77,4.78,4.79,4.8,4.81,4.82,4.83,4.84,4.85,4.86,4.87,4.88,4.89,4.9] # The lattice parameter for the cell in Bohr.
ca_ratio = [1.71,1.72,1.73,1.74]
# k1 = [7] # k-point grid of 8x8x8
# alat = [5.38,5.39] # The lattice parameter for the cell in Bohr.
# ca_ratio = [1.72]

# Loop through different k-points.
for k1,alat,ca_ratio in list(itertools.product(*[k1, alat,ca_ratio])):
    # This generates a string from the template with the parameters replaced
    # by the specified values.

    k3 = int(k1/1.7)


    # Let's define an easy jobname.
    jobname = "Fe_HCP_%s_%s_%s_%s" % (alat, str(ca_ratio).replace('.',''),k1,k3)

    os.makedirs(jobname)

    with cd(jobname):
        os.makedirs('tmp')
        tmp_folder = pjoin(os.getcwd(),'tmp/')
        s = template.format(alat=alat, k1=k1,k3=k3,calat=ca_ratio,tmp_folder=tmp_folder)
        # Write the actual input file for PWSCF.
        with open("%s.pw.in" % jobname, "w") as f:
            f.write(s)
        os.system("cp ../Fe.pbe-spn-kjpaw_psl.0.2.1.UPF .")

    #Print some status messages.
    # print("Running with alat = %s, k1 = %s, k3 = %s, ca_ratio = %s ..." % (alat, k1, k3, ca_ratio))
    # Run PWSCF. Modify the pw.x command accordingly if needed.
    # os.system("pw.x -inp {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    # print("Done. Output file is %s.out." % jobname)

    print("Template generated with alat = %s, k1 = %s, k3 = %s, ca_ratio = %s ..." % (alat, k1, k3, ca_ratio))
# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
# shutil.rmtree("tmp")
