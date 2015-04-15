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
 N library "{Polarfunc_1st}"
end
dft
 mult 1
 xc {base_set}
end
task dft optimize

title "N2 dft freq"
charge 0
basis
 N library "{Polarfunc_2nd}"
end
dft
 mult 1
 xc {base_set}
end
task dft freq

title "N2 dft energy"
charge 0
basis
 N library "{Polarfunc_3rd}"
end
dft
 mult 1
 xc {base_set}
end
task dft energy
"""


# Function we used for N2_template file generate
def N2_temp_build(base_set, Polarfunc_1st, Polarfunc_2nd, Polarfunc_3rd):


    p = {
        'base_set':base_set,
        'Polarfunc_1st':Polarfunc_1st,
        'Polarfunc_2nd':Polarfunc_2nd,
        'Polarfunc_3rd':Polarfunc_3rd
    }

    with open('N2.nw','w') as f:
        f.write(N2TEMPLATE.format(**p))

    #This is the nwchem we call for calculation using N2 template file generated
    # os.system('nwchem N2.nw > N2.nwout')
    # command = 'nwchem ' + 'N2.nw ' + '> N2.nwout'
    # subprocess.call(command,shell=True)

