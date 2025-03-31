#!/usr/bin/env python3

import os
import subprocess


os.system('clear')

target = input("IP target: ")

if os.path.exists('scanresult'):
    pass
else:
    os.mkdir('scanresult')

os.system(f"rm -rf scanresult/{target}")
with open(f"scanresult/{target}", 'a') as f:
    f.write("###Target###\n")
    f.write(f"###{target}###\n")
    f.write("###GEOIP###\n")
    geoip_output = subprocess.check_output(['geoiplookup', target]).decode('utf-8')
    f.write(geoip_output)
    ipinfo_output = subprocess.check_output(['curl', f'https://ipinfo.io/{target}']).decode('utf-8')
    f.write(ipinfo_output)


with open(f"scanresult/{target}", 'a') as f:
    f.write("###DETECT OS###\n")
    nmap_output = subprocess.check_output(['nmap', '-O', '--osscan-guess', '-Pn', target]).decode('utf-8')
    f.write(nmap_output)

nmap_output = subprocess.check_output(['nmap', '-Pn', '-sT', '--scan-delay', '1s', '-oG', f"scanresult/{target}.txt", '-p', '80,102,443,502,530,593,789,1089-1091,1911,1962,2222,2404,4000,4840,4843,4911,9600,19999,20000,20547,34962-34964,34980,44818,46823,46824,55000-55003', target]).decode('utf-8')
with open(f"scanresult/{target}.txt", 'a') as f:
    f.write(nmap_output)

os.system(f"rm -rf scanresult/{target}.txt")
os.system(f"more scanresult/{target}")


