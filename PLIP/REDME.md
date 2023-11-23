# PLIP

Protein Ligand Interactions Profiling

### Install Docker Image
```sh
docker pull pharmai/plip
```

### Command
```sh
sudo docker run --rm -v ${PWD}:/results -w /results -u $(id -u ${USER}):$(id -g ${USER}) pharmai/plip:latest -f target.pdb -yv -o output_dir/ -x -t -y -p
```

### Output Directory
- output_dir
    - PyMOL Ray-traced images (-p) (.png)
    - PyMOL session files (-y) (.pse)
    - raw receptor pdb (.pdb)
    - plip fixed protein pdb (.pdb)
    - Text report files (-t) (.txt)
    - XML report files (-x) (.xml)

### Interactions
- Hydrophobic Interaction
- Hydrogen Bond
- Water Bridges
- pi-Stacking (parallel)
- pi-Stacking (perpendicular)
- pi-Cation Interaction
- Halogen Bond
- Salt Bridge
- Metal Complex