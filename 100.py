#!/usr/bin/python3
import os
import subprocess
os.system('clear')
def banner():
    font = """	       ▄▄▄▄       ▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄  
	     ▄█░░░░▌     ▐░░░░░░░░░▌  ▐░░░░░░░░░▌ 
	    ▐░░▌▐░░▌    ▐░█░█▀▀▀▀▀█░▌▐░█░█▀▀▀▀▀█░▌
	     ▀▀ ▐░░▌    ▐░▌▐░▌    ▐░▌▐░▌▐░▌    ▐░▌
	        ▐░░▌    ▐░▌ ▐░▌   ▐░▌▐░▌ ▐░▌   ▐░▌
	        ▐░░▌    ▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌
	        ▐░░▌    ▐░▌   ▐░▌ ▐░▌▐░▌   ▐░▌ ▐░▌
	        ▐░░▌    ▐░▌    ▐░▌▐░▌▐░▌    ▐░▌▐░▌
	    ▄▄▄▄█░░█▄▄▄ ▐░█▄▄▄▄▄█░█░▌▐░█▄▄▄▄▄█░█░▌
	   ▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌  ▐░░░░░░░░░▌ 
	    ▀▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀    ▀▀▀▀▀▀▀▀▀  
                                         Version: 0.1
					 github:https://github.com/DLuta/100
					 Coder :D.Luta
  """
    print(font)

if __name__ == "__main__":
    banner()

###CHECK DIRECTORY
if not os.path.isdir("scanresult"): 
	
	# if the demo_folder2 directory is 
	# not present then create it. 
	os.makedirs("scanresult") 


target = input("		IP target:")

with open(f"scanresult/{target}", "w") as file:
    file.write(f"		###Target###\n")
    file.write(f"		###{target}###\n")
    file.write(f"		###GEOIP###\n")
    subprocess.run(["geoiplookup", target], stdout=file)
    subprocess.run(["curl", f"https://ipinfo.io/{target}"], stdout=file)

# DETECT OS
with open(f"scanresult/{target}", "a") as file:
    file.write("		###DETECT OS###\n")
    subprocess.run(["nmap", "-O", "--osscan-guess", "-Pn", target], stdout=file)

subprocess.run(["nmap", "-Pn", "-sT", "--scan-delay", "1s", "-oG", f"scanresult/{target}.txt", "-p", "80,102,443,502,530,593,789,1089-1091,1911,1962,2222,2404,4000,4840,4843,4911,9600,19999,20000,20547,34962-34964,34980,44818,46823,46824,55000-55003", target])

subprocess.run(["cat", f"scanresult/{target}.txt"], stdout=subprocess.PIPE)
subprocess.run(["rm", "-rf", f"scanresult/{target}.txt"])
subprocess.run(["more", f"scanresult/{target}"])




