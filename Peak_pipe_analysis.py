import os
import sys
import csv

##Please call the files you wish to analyze by a simple nomenclature contained in one line of a txt file named "names.txt".

liste='10 100 200 300 400 500 650 800 950 1100 1200 1300 1400 1500 1650 1800'
# save the filename in the name array
name=liste.split()
inp=open(name[0],'r')
op=inp.readlines()
title_line=op[0]
title_line=list(title_line)

# filename preprocessing
# if there is any space in the line0, replace _ with space
for bli in range(len(op[0])):
    if title_line[bli]==' ' :
        title_line[bli]='_'
title_line="".join(title_line)
# the first line contains the title for each column
# save the title for each column into a list
# title_line = ['Assign_F1', 'Volume']
title_line=title_line.split()


# Create output files
for ri in range(len(title_line)) :             
    tab = open('Peak_evolution_'+title_line[ri]+'.txt','w')
    #csv_file = open(title_line[ri]+'.csv', 'w')
    # process each file 
    for i in range(len(name)):
        inp=open(name[i],'r')
        op=inp.readlines()
        totcar=''
        totnum=''
        # read line by line for each file
        for j in range(1, len(op)):
            data = op[j].split()
            totnum = totnum + '\t' + data[0]
            totcar = totcar + '\t' + data[ri]
            
        # only the first line should add the list of number line
        if i!=0 :
            totnum=''
        line='\n'+name[i]+totcar
        tab.writelines(totnum+line)
        
   
     
     
        
        
