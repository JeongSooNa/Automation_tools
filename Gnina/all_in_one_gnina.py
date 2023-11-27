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



### Run Gnina Docking
### Command
### gnina -r rec.pdb -l lig.sdf --autobox_ligand orig.sdf --scoring vinardo --cnn_scoring none -o docked.sdf



os.chdir(current_path)