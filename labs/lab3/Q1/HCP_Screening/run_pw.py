#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calculations. If you don't know Python, get a quick primer from the official
Python documentation at https://docs.python.org/2.7/. The script is deliberately
simple so that only basic Python syntax is used and you can get comfortable with
making changes and writing programs.

Author: Shyue Ping Ong
"""

import os
import shutil
import itertools

# Load the Si.pw.in.template file as a template.
with open("Fe.hcp.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k1 = [6,7,8,9,10,11] # k-point grid of 8x8x8
alat = [5.38,5.39,5.40,5.41,5.42,5.43,5.44,5.45,5.46] # The lattice parameter for the cell in Bohr.
ca_ratio = [1.72,1.73,1.74]

# Loop through different k-points.
for k1,alat,ca_ratio in list(itertools.product(*[k1, alat,ca_ratio])):
    # This generates a string from the template with the parameters replaced
    # by the specified values.
    k3 = int(k1/1.7)
    s = template.format(alat=alat, k1=k1,k3=k3,calat=ca_ratio)

    # Let's define an easy jobname.
    jobname = "Fe_HCP_%s_%s_%s_%s" % (alat, str(ca_ratio).replace('.',''),k1,k3)

    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(s)

    #Print some status messages.
    print("Running with alat = %s, k1 = %s, k3 = %s, ca_ratio = %s ..." % (alat, k1, k3, ca_ratio))
    # Run PWSCF. Modify the pw.x command accordingly if needed.
    os.system("pw.x -inp {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    print("Done. Output file is %s.out." % jobname)

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
