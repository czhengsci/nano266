__author__ = 'chenzheng'

import os
import subprocess

NH3TEMPLATE="""
memory total 1000 mb
geometry units angstroms noautoz
 N 0.257 -0.363 0.0
 H 0.257 0.727 0.0
 H 0.771 -0.727 0.89
 H 0.771 -0.727 -0.89
end

title "H3N1 dft optimize"
charge 0
basis
 H library "{Polarfunc_1st}"
 N library "{Polarfunc_1st}"
end
dft
 mult 1
 xc {functional_1st}
end
task dft optimize

title "H3N1 dft freq"
charge 0
basis
 H library "{Polarfunc_1st}"
 N library "{Polarfunc_1st}"
end
dft
 mult 1
 xc {functional_1st}
end
task dft freq

title "H3N1 dft energy"
charge 0
basis
 H library "{Polarfunc_2nd}"
 N library "{Polarfunc_2nd}"
end
dft
 mult 1
 xc {functional_2nd}
end
task dft energy
"""

# Function we used for NH3_template file generate
def NH3_temp_build(functional_1st,functional_2nd,Polarfunc_1st, Polarfunc_2nd):

    p = {
        'functional_1st':functional_1st,
        'functional_2nd':functional_2nd,
        'Polarfunc_1st':Polarfunc_1st,
        'Polarfunc_2nd':Polarfunc_2nd,
    }

    with open('NH3.nw','w') as f:
        f.write(NH3TEMPLATE.format(**p))

    #This is the nwchem call for calculation us NH3 template file generated above
    os.system('nwchem NH3.nw > NH3.nwout')
    # subprocess.call(command, shell=True)