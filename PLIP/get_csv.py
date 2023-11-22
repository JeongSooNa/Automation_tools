import os

list = os.listdir("patt6_7_plip/")
print(list[0])
print(len(list))

f = open("patt6_7_plip.csv","w")
f.write("PDB,Gnina_affinity,Gnina_CNN_pose_score,Gnina_CNN_affinity,Interaction_type,RESNR,RESTYPE\n")

for i in range(0,len(list)):
# for i in range(0,1):
    # r = open("rmsd_under1_pdbs/" + list[i].split(".")[0] + "/report.txt")
    r = open("patt6_7_plip/" + list[i] + "/report.txt")
    report = r.read()
    
    # Gnina score
    pdb = list[i].split(".")[0][:-2]
    pose = list[i].split(".")[0][-1:]
    g = open("C:/Users/jsna/Desktop/STAT3/output_lys/raw_log/" + list[i].split(".")[0][:-2] + "_log.txt")
    gnina = g.read()
    gnina_val = gnina.split("\n    " + pose)[1].split("\n")[0].split()
    # print(gnina_val)
    f.write(list[i].split(".")[0] + "," + gnina_val[0] + "," + gnina_val[1] + "," + gnina_val[2] + "\n")
    
    # Hydrophobic Interactions
    if "**Hydrophobic Interactions**" in report:
        tmp = report.split("**Hydrophobic Interactions**\n")[1].split("\n")[0].split("+")
        report_hi = report.split("+" + tmp[1].replace("-","=") + "+" + tmp[2].replace("-","=") + "+" + tmp[3].replace("-","=") + "+" + tmp[4].replace("-","=") + "+" + tmp[5].replace("-","=") + "+" + tmp[6].replace("-","=") + "+" + tmp[7].replace("-","=") + "+" + tmp[8].replace("-","=") + "+" + tmp[9].replace("-","=") + "+" + tmp[10].replace("-","=") + "+" + tmp[11].replace("-","=") + "+\n")[1].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + "\n\n")[0].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+")
        # print(len(report_hi))
        for j in range(0,len(report_hi)):
            RESNR = report_hi[j].split("|")[1].replace(" ","")
            RESTYPE = report_hi[j].split("|")[2].replace(" ","")
            f.write(",,,," + "Hydrophobic Interactions," + RESNR + "," + RESTYPE + "\n")
    
    # Hydrogen Bonds
    # if "**Hydrogen Bonds**\n+-------+---------+----------+-----------+-------------+--------------+-----------+----------+----------+-----------+-----------+----------+-----------+-------------+--------------+------------------------+------------------------+" in report:
    if "**Hydrogen Bonds**" in report:
        tmp = report.split("**Hydrogen Bonds**\n")[1].split("\n")[0].split("+")
        report_hb = report.split("+" + tmp[1].replace("-","=") + "+" + tmp[2].replace("-","=") + "+" + tmp[3].replace("-","=") + "+" + tmp[4].replace("-","=") + "+" + tmp[5].replace("-","=") + "+" + tmp[6].replace("-","=") + "+" + tmp[7].replace("-","=") + "+" + tmp[8].replace("-","=") + "+" + tmp[9].replace("-","=") + "+" + tmp[10].replace("-","=") + "+" + tmp[11].replace("-","=") + "+" + tmp[12].replace("-","=") + "+" + tmp[13].replace("-","=") + "+" + tmp[14].replace("-","=") + "+" + tmp[15].replace("-","=") + "+" + tmp[16].replace("-","=") + "+" + tmp[17].replace("-","=") + "+\n")[1].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + tmp[12] + "+" + tmp[13] + "+" + tmp[14] + "+" + tmp[15] + "+" + tmp[16] + "+" + tmp[17] + "+" + "\n\n")[0].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + tmp[12] + "+" + tmp[13] + "+" + tmp[14] + "+" + tmp[15] + "+" + tmp[16] + "+" + tmp[17] + "+")
        # print(len(report_hb))
        for j in range(0,len(report_hb)):
            RESNR = report_hb[j].split("|")[1].replace(" ","")
            RESTYPE = report_hb[j].split("|")[2].replace(" ","")
            f.write(",,,," + "Hydrogen Bonds," + RESNR + "," + RESTYPE + "\n")
    
    
    # Salt Bridges
    if "**Salt Bridges**" in report:
        tmp = report.split("**Salt Bridges**\n")[1].split("\n")[0].split("+")
        report_sb = report.split("+" + tmp[1].replace("-","=") + "+" + tmp[2].replace("-","=") + "+" + tmp[3].replace("-","=") + "+" + tmp[4].replace("-","=") + "+" + tmp[5].replace("-","=") + "+" + tmp[6].replace("-","=") + "+" + tmp[7].replace("-","=") + "+" + tmp[8].replace("-","=") + "+" + tmp[9].replace("-","=") + "+" + tmp[10].replace("-","=") + "+" + tmp[11].replace("-","=") + "+" + tmp[12].replace("-","=") + "+" + tmp[13].replace("-","=") + "+\n")[1].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + tmp[12] + "+" + tmp[13] + "+" + "\n\n")[0].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + tmp[12] + "+" + tmp[13] + "+")
        # print(len(report_sb))
        for j in range(0,len(report_sb)):
            RESNR = report_sb[j].split("|")[1].replace(" ","")
            RESTYPE = report_sb[j].split("|")[2].replace(" ","")
            f.write(",,,," + "Salt Bridges," + RESNR + "," + RESTYPE + "\n")
    # if "**Salt Bridges**\n+-------+---------+----------+----------------+-----------+-------------+--------------+------+-----------+-------------+--------------+-----------------------+-----------------------+" in report:
    #     report_sb = report.split("+=======+=========+==========+================+===========+=============+==============+======+===========+=============+==============+=======================+=======================+\n")[1].split("\n+-------+---------+----------+----------------+-----------+-------------+--------------+------+-----------+-------------+--------------+-----------------------+-----------------------+\n\n")[0].split("\n+-------+---------+----------+----------------+-----------+-------------+--------------+------+-----------+-------------+--------------+-----------------------+-----------------------+")
    #     print(len(report_sb))
    #     for j in range(0,len(report_sb)):
    #         RESNR = report_sb[j].split("|")[1].replace(" ","")
    #         RESTYPE = report_sb[j].split("|")[2].replace(" ","")
    #         f.write(",,,," + "Salt Bridges," + RESNR + "," + RESTYPE + "\n")
        
f.close()