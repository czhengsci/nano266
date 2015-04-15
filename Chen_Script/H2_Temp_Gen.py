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
 H library "{Polarfunc_1st}"
end
dft
 mult 1
 xc {base_set}
end
task dft optimize

title "H2 dft freq"
charge 0
basis
 H library "{Polarfunc_2nd}"
end
dft
 mult 1
 xc {base_set}
end
task dft freq

title "H2 dft energy"
charge 0
basis
 H library "{Polarfunc_3rd}"
end
dft
 mult 1
 xc {base_set}
end
task dft energy
"""


# Function we used for H2_template file generate
def H2_temp_build(base_set,Polarfunc_1st, Polarfunc_2nd, Polarfunc_3rd):


    p = {
        'base_set':base_set,
        'Polarfunc_1st':Polarfunc_1st,
        'Polarfunc_2nd':Polarfunc_2nd,
        'Polarfunc_3rd':Polarfunc_3rd
    }

    with open('H2.nw','w') as f:
        f.write(H2TEMPLATE.format(**p))

    #This is the nwchem we call for calculation using H2 template file generated
    # os.system('nwchem H2.nw > H2.nwout')
    # command = 'nwchem ' + 'H2.nw ' + '> H2.nwout'
    # subprocess.call(command,shell=True)