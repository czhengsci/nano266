#!/usr/bin/env python
import os
import subprocess
from monty.os import cd
import argparse
import fnmatch

def proc_dic(rootfolder, filename, sub):

    filename_pre = rootfolder.rsplit('/', 1)[-1]
    rename = filename_pre + '.' + filename.split('.')[-1]
    command = 'mv F.out {}'.format(rename)
    # print filename
    with cd(rootfolder):
        os.system(command)
    print command


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
        used for file rename.""",
       )

    parser.add_argument("directories", metavar="dir",
                        type=str, nargs="+",
                        help="directories to process")

    args = parser.parse_args()

    for d in args.directories:
            for parent, subdir, files in os.walk(d):
                for filename in fnmatch.filter(files, '*.out'):
                    proc_dic(parent,filename,subdir)
