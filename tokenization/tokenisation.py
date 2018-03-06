affixe=[]

Ponctuation=['.',',',';','?','!',':','"','(',')']
for i in open("c:/tal/affixescolles.txt",encoding='utf-8'):
    a=i
    a=a.replace("\ufeff","")
    a=a.replace("\n","")
    affixe.append(str(a))

for line in open("c:/tal/corpusliterraire.txt",encoding='utf-8'):
    for i in Ponctuation:
        line=line.replace(i,' '+i)
    for i in affixe:
        if (i[0]=='-'):
            line=line.replace(i,' '+i)
        else:
            line=line.replace(i,i+' ')

    line=line.replace("  "," ")
    print (line)






