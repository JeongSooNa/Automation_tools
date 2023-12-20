### Gnina All Process 
### Gnina molecular docking
### get log data and make table from score & affinity
### JeongSoo Na
### 2023.11.23

### Packages import
import os
import sys

current_path = os.getcwd()

### parameter
input_dir = sys.argv[1]
input_list = os.listdir(input_dir)
output_dir = sys.argv[2]
print("Num : " + str(len(input_list)))

### Run Gnina Docking
### Command
### gnina -r rec.pdb -l lig.sdf --autobox_ligand orig.sdf --scoring vinardo --cnn_scoring none -o docked.sdf


### Get Gnina output log csv file

raw = ""
data = raw.split("-----+------------+------------+----------\n")[1].split("\n")
for j in data:
    index = j.split()[0]
    affinity = j.split()[1]
    cnn_pose_score = j.split()[2]
    cnn_affinity = j.split()[3]



os.chdir(current_path)


### How to calculate RMSD or get value in gnina raw script or options?