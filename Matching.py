import os
import sys
import numpy as np
import csv


mutationList = []
pbdidList = []
mutNumberList = []

letter_to_3code_dic = {
    'A':'ALA',
    'R':'ARG',
    'N':'ASN',
    'D':'ASP',
    'B':'ASX',
    'C':'CYS',
    'E':'GLU',
    'Q':'GLN',
    'Z':'GLX',
    'G':'GLY',
    'H':'HIS',
    'I':'ILE',
    'L':'LEU',
    'K':'LYS',
    'M':'MET',
    'F':'PHI',
    'P':'PRO',
    'S':'SER',
    'T':'THR',
    'W':'TRP',
    'Y':'TYR',
    'V':'VAL',
    't':'sgs'

}

#amino acids have one letter codes and three letter codes, the two files we are dealing with 
#utilize different codes 




#mutnumberList is the site 
#now mutnumberList neds to be lined up with residueList 


#this is mcce files. 
#so if for example, 90 (mutationList[1]) is in residueList[i] #need 2 for loops!
           #if D is in residueList[i] and ASP is in residueList[i]
            #mccepkaList[i] no we need specific mccepkalist!

def get_mut():
    residueList = [] 
    mccepkaList = []
    PkaOfInterest = []
    with open('REALKevinAllieSNASE.tsv') as inf: 
	next(inf)
        for line in inf:
            col = line.split()
            if len(col[1]) < 6:
                mutationList.append(col[1])
                pbdidList.append(col[0])
                mutationNumber1 = filter(str.isdigit, col[1])
		mutatNUM1 = int(mutationNumber1)
                mutNumberList.append(mutatNUM1)
		
    return pbdidList, mutationList, mutNumberList



def retreive_pkaValue(pdb_dir,mut_name):
    
    k = 0
    if os.path.isdir('pdb_directories/'+pdb_dir):# path only for if already inside the python scripts directory
            f = open('pdb_directories/'+pdb_dir+'/pK.out', 'r')
            pka_out = f.readlines()[1:]   #can analyze each line ommitting the first one
            for line in pka_out:
                Pkout_list = line.split() 
 
                if letter_to_3code_dic[mut_name[-1]]  == Pkout_list[0][:3]:
		    mutatNUM2 = filter(str.isdigit, Pkout_list[0])
		    mutationNumber2 = int(mutatNUM2)

                    for everyitem in mutNumberList:
			mutnameNUM = filter(str.isdigit, mut_name)
			if int(mutnameNUM) == mutationNumber2:
                            if int(mutationNumber2) == everyitem:
                                print 'in directory', pdb_dir, 'mutname ',mut_name,'mutnum2 ', mutationNumber2,'everyitem ', everyitem
                

                
              

       



pbdidList, mutationList, mutNumberList = get_mut()


for every_dir in pbdidList: #goes through every directory that exists and part of pdbidlist
    for every_mut in mutationList:
        retreive_pkaValue(every_dir,every_mut)


 
