#Thomas
#Date: 6 July 19
#This simple script shows how to execute shell commands

import os #first method
import subprocess #second method

#First Method of executing shell scripts
ls = 'ls -trl'

os.system(ls)

#store the output of a shell command
cmdOutput = os.popen("nl /etc/*release").read()

print (cmdOutput)

#Second Method of executing shell scripts
subprocess.call(["ls","-trl"])
