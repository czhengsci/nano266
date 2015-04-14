__author__ = 'chenzheng'

import os
import subprocess
import argparse

pjoin = os.path.join


H2TEMPLATE ="""
memory total 1000 mb
geometry units angstroms
 H 0 0 0
 H 0 0 0.7414
end

title "H2 dft optimize"
charge 0
basis
 H library "6-31G"
end
dft
 mult 1
 xc {base_set}
end
task dft optimize

title "H2 dft freq"
charge 0
basis
 H library "6-31G"
end
dft
 mult 1
 xc {base_set}
end
task dft freq

title "H2 dft energy"
charge 0
basis
 H library "6-311G"
end
dft
 mult 1
 xc {base_set}
end
task dft energy
"""


# Function we used for H2_template file generate
def H2_temp_build(basis_set):


    p = {
        'base_set':basis_set,
    }

    with open('H2.nw','w') as f:
        f.write(H2TEMPLATE.format(**p))

    #This is the nwchem we call for calculation using H2 template file generated
    os.system('nwchem H2.nw > H2.nwout')
    # command = 'nwchem ' + 'H2.nw ' + '> H2.nwout'
    # subprocess.call(command,shell=True)