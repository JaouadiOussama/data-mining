import math
with open('F1_2.txt','r') as f:
    data = f.readlines()

seq=[]
for line in data:
    sequence=line.split(" ")
    seq=seq+sequence


seq1=[]
for i in range(0,92):
    seq1.append(seq[i].replace("\n",""))        
seq1.pop(0)                                 
seq1.pop(0)
seq1.pop(0)
seq1.pop(0)
seq1.pop(40)


nb=input('Donner la taille de k-gramme: ')      
nbr=int(nb)
attributs=[]
for i in range(0,87):
     attributs=attributs+[seq1[i][j:j+nbr] for j in range(0,len(seq1[i])-nbr+1,nbr)]
     
att=[]
for i in range(0,len(attributs)):
    if not attributs[i] in attributs[0:i-1]:    
        att.append(attributs[i])
        
occ=[[0 for x in range(len(att))] for y in range(87)]
for i in range(0,87):
    for j in range (0,len(att)):
        occ[i][j]=(seq1[i].count(att[j]))
        
boole=[[0 for x in range(len(att))] for y in range(87)]
for i in range(0,87):
    for j in range (0,len(att)):
        if (occ[i][j]!=0):
            boole[i][j]=1
        else:
            boole[i][j]=0

freq=[[0 for x in range(len(att))] for y in range(87)]
tot=len(att)
for i in range(0,87):
    for j in range (0,len(att)):
        if (occ[i][j]!=0):
            freq[i][j]=float("{0:.4f}".format(occ[i][j]/tot))
            
TF_IDF=[[0 for x in range(len(att))] for y in range(87)]
for i in range(0,87):
    for j in range (0,len(att)):
        if (freq[i][j]!=0):
            TF_IDF[i][j]=float("{0:.4f}".format(math.log(freq[i][j])))


f1=open('testb.txt','w')
for i in range(0,len(att)):            
    f1.write(att[i])
    f1.write("\t")
f1.write("Classe\n")            
for i in range(0,40):                  
    for j in range(0,len(att)):
        f1.write(str(boole[i][j]))
        f1.write("\t")
    f1.write("c1\n")
for i in range(40,87):
    for j in range(0,len(att)):
        f1.write(str(boole[i][j]))
        f1.write("\t")
    f1.write("c2\n")
f1.close()


f2=open('testf.txt','w')
for i in range(0,len(att)):            
    f2.write(att[i])
    f2.write("\t")
f2.write("Classe\n")            
for i in range(0,40):                  
    for j in range(0,len(att)):
        f2.write(str(freq[i][j]))
        f2.write("\t")
    f2.write("c1\n")
for i in range(40,87):
    for j in range(0,len(att)):
        f2.write(str(freq[i][j]))
        f2.write("\t")
    f2.write("c2\n")
f2.close()


f3=open('testo.txt','w')
for i in range(0,len(att)):         
    f3.write(att[i])
    f3.write("\t")
f3.write("Classe\n")            
for i in range(0,40):                  
    for j in range(0,len(att)):
        f3.write(str(occ[i][j]))
        f3.write("\t")
    f3.write("c1\n")
for i in range(40,87):
    for j in range(0,len(att)):
        f3.write(str(occ[i][j]))
        f3.write("\t")
    f3.write("c2\n")
f3.close()


f2=open('testt.txt','w')
for i in range(0,len(att)):            
    f2.write(att[i])
    f2.write("\t")
f2.write("Classe\n")            
for i in range(0,40):                  
    for j in range(0,len(att)):
        f2.write(str(TF_IDF[i][j]))
        f2.write("\t")
    f2.write("c1\n")
for i in range(40,87):
    for j in range(0,len(att)):
        f2.write(str(TF_IDF[i][j]))
        f2.write("\t")
    f2.write("c2\n")
f2.close()
