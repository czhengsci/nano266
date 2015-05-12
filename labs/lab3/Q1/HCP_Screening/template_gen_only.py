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
k1 = [7,8,9,10,11,12,13] # k-point grid of 8x8x8
alat = [5.38,5.39,5.40,5.41,5.42,5.43,5.44,5.45,5.46] # The lattice parameter for the cell in Bohr.
ca_ratio = [1.72,1.73,1.74]
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
