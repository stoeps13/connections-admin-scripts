'''
Create a file (html or markdown) with the output of
    - JVMHeap
    - LogFiles
    - Ports
    - Variables

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Update:        2025-03-18

License:       Apache 2.0

ToDo: Add Markdown format
'''

import sys
import os.path

filename = raw_input('Path and Filename to Documentation file: ')
org_stdout = sys.stdout

if (os.path.isfile(filename)):
    answer = raw_input(
        "File exists, Overwrite, Append or Abort? (O|A|X)").lower()
    if answer == "o":
        sys.stdout = open(filename, "w")
    elif answer == "a":
        sys.stdout = open(filename, "a")
    else:
        print "Exit"
        sys.exit()
else:
    sys.stdout = open(filename, "w")

print '# J2EE Roles set for all Applications:'
execfile('ibmcnx/doc/j2eeroles.py')

print '# JVM Settings of all AppServers:'
execfile('ibmcnx/doc/JVMSettings.py')

print '# Used Ports:'
execfile('ibmcnx/doc/Ports.py')

print '# LogFile Settgins:'
execfile('ibmcnx/doc/LogFiles.py')

print '# WebSphere Variables'
execfile('ibmcnx/doc/Variables.py')

print '# DataSources and parameters'
execfile('ibmcnx/doc/DataSources.py')

sys.stdout.close()
sys.stdout = org_stdout
