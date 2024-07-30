#AUTHOR:        Ru1722
#PROGRAM NAME:  simplePyFetch
#DESCRIPTION:   A simple python system fetch tool
#VERSION:       1.1
#DEV NOTES:     Simplified the code by using uptime from the subrpocess library to call the uptime command from the shell.

import platform
import psutil
from termcolor import colored
from datetime import datetime
import time
import subprocess

uname = platform.uname()

#You can change color and attribute to the text below
color = 'green'
attribute = 'blink'

boot_time_timestrap = psutil.boot_time()
boottime = datetime.fromtimestamp(boot_time_timestrap)
uptimeOutput = subprocess.check_output(['uptime'])
decodeUptime = uptimeOutput.decode('utf-8').strip()

OS = colored("OS:           ",color,attrs = [attribute])
CPU = colored("CPU:          ",color,attrs = [attribute])
Name = colored("SYSTEM NAME:  ",color,attrs = [attribute])
BT = colored("BOOT TIME:    ",color,attrs = [attribute])
UT = colored("SYSTEM UPTIME:",color,attrs = [attribute])

print(OS,platform.release())
print(CPU,platform.architecture()[0])
print(Name,platform.system())
print(BT,boottime.hour,":",boottime.minute,":",boottime.second,)
print(UT,decodeUptime)

