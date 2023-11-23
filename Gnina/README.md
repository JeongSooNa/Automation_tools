# Gnina

Protein Ligand Molecular Docking

### Install Docker Image
```sh
docker pull gnina/gnina
```

### Command

- In Linux Environments
```sh
docker run -v $(pwd):/scr gnina/gnina gnina -r /scr/rec.pdb -l /scr/lig.sdf --autobox_ligand /scr/crystal_ligand.mol2 -o /scr/docked.sdf
```

- In Docker Environments
```sh
gnina -r rec.pdb -l lig.sdf --autobox_ligand orig.sdf -o docked.sdf --scoring vinardo --cnn_scoring none --device 0
```

### Output & Log
- output sdf file : docking pose (default number : 9)
- log (needs save)
```
              _             
             (_)            
   __ _ _ __  _ _ __   __ _ 
  / _` | '_ \| | '_ \ / _` |
 | (_| | | | | | | | | (_| |
  \__, |_| |_|_|_| |_|\__,_|
   __/ |                    
  |___/                     

gnina v1.0.1 master:aa41230   Built Mar 23 2021.
gnina is based on smina and AutoDock Vina.
Please cite appropriately.

Commandline: gnina -r rec.pdb -l ligand.sdf --autobox_ligand lef.sdf --scoring vinardo -o docked.sdf
Using random seed: 1667878458

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
 | pose 0 | initial pose not within box
 | pose 0 | ligand outside box
 | pose 0 | ligand outside box
 | pose 0 | ligand outside box
 | pose 0 | ligand outside box

mode |  affinity  |    CNN     |   CNN
     | (kcal/mol) | pose score | affinity
-----+------------+------------+----------
    1       -5.53       0.6783      4.671
    2       -8.86       0.6773      4.368
    3       -7.23       0.6476      4.627
    4       -7.47       0.6266      4.709
    5       -8.02       0.6196      4.853
    6       -6.13       0.6191      4.600
    7       -7.71       0.6146      4.431
    8       -5.99       0.6102      4.772
    9       -8.27       0.5919      4.797
```