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
with open("Fe.bcc.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k = [9] # k-point grid of 9x9x9
alat = [5.15,5.20,5.25,5.3,5.31,5.32,5.33,5.34,5.35,5.36,5.37,5.38,5.39,5.40,5.45,5.5,5.55] # The lattice parameter for the cell in Bohr.

# Loop through different k-points.
for k,alat in list(itertools.product(*[k, alat])):
    # This generates a string from the template with the parameters replaced
    # by the specified values.
    s = template.format(alat=alat, k=k)

    # Let's define an easy jobname.
    jobname = "Fe_bcc_%s_%s" % (alat, k)

    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(s)

    #Print some status messages.
    print("Running with alat = %s, k = %s..." % (alat, k))
    # Run PWSCF. Modify the pw.x command accordingly if needed.
    os.system("pw.x -inp {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    print("Done. Output file is %s.out." % jobname)

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
