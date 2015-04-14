__author__ = 'chenzheng'
__author__ = 'chenzheng'

import os
import subprocess
import argparse

pjoin = os.path.join


N2TEMPLATE ="""
memory total 1000 mb
geometry units angstroms
 N 0 0 0
 N 0 0 1.1
end

title "N2 dft optimize"
charge 0
basis
 N library "6-31G"
end
dft
 mult 1
 xc {base_set}
end
task dft optimize

title "N2 dft freq"
charge 0
basis
 N library "6-31G"
end
dft
 mult 1
 xc {base_set}
end
task dft freq

title "N2 dft energy"
charge 0
basis
 N library "6-311G"
end
dft
 mult 1
 xc {base_set}
end
task dft energy
"""


# Function we used for N2_template file generate
def N2_temp_build(basis_set):


    p = {
        'base_set':basis_set,
    }

    with open('N2.nw','w') as f:
        f.write(N2TEMPLATE.format(**p))

    #This is the nwchem we call for calculation using N2 template file generated
    os.system('nwchem N2.nw > N2.nwout')
    # command = 'nwchem ' + 'N2.nw ' + '> N2.nwout'
    # subprocess.call(command,shell=True)

