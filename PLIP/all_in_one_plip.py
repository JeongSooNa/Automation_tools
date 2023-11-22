### PLIP All Process 
### PLIP calculation and get report
### get csv file from output report.txt
### JeongSoo Na
### 2023.11.22

### Packages import
import os
import sys

current_path = os.getcwd()

### parameter
### Input data : Directory include input pdb files
### Output directory : Directory saved PLIP output data and csv table
input_dir = sys.argv[1]
input_list = os.listdir(input_dir)
output_dir = sys.argv[2]
print("pdb number : " + str(len(input_list)))

os.chdir(input_dir)

### Make directory per pdb
try:
    if not os.path.exists(output_dir):
        os.system("sudo mkdir " + output_dir)
except OSError:
    print("Error : Directory is already exists.")

for i in input_list:
    try:
        if not os.path.exists(i):
            os.system("sudo mkdir " + output_dir + "/" + i.replace(".pdb",""))
    except OSError:
        print("Error : Directory is already exists.")
    

### Run PLIP
### command : sudo docker run --rm -v ${PWD}:/results -w /results -u $(id -u ${USER}):$(id -g ${USER}) pharmai/plip:latest -f target.pdb -yv -o output_dir/ -x -t -y -p
for i in input_list:
    os.system("sudo docker run --rm -v ${PWD}:/results -w /results -u $(id -u ${USER}):$(id -g ${USER}) pharmai/plip:latest -f " + i + " -yv -o " + output_dir + "/" + i.replace(".pdb","") + "/ -x -t -y -p")

### Report to csv table
f = open(output_dir + "/plip_value_table.csv")
f.write("PDB,Interaction_type,RESNR,RESTYPE,DIST,DIST_sub\n")





f.close()

os.chdir(current_path)