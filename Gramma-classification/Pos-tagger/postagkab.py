import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

G = nx.MultiDiGraph()
#list of kabyle tags
tags=[
('NC',0,()),
('CC',0,()),
('CS',0,()),
('MET',0,()),
('PRP',0,()),
('PPA',0,()),
('PAN',0,()),
('PAP',0,()),
('PSV',0,()),
('PPV',0,()),
('PRD',0,()),
('PRI',0,()),
('NMC',0,()),
('NMP',0,()),
('ADV',0,()),
('ADJ',0,()),
('VAI',0,()),
('VAF',0,()),
('VP',0,()),
('VPN',0,()),
('PA',0,()),
('VPPP',0,()),
('VPPN',0,()),
('VII',0,()),
('VAI',0,()),
('VPAIP',0,()),
('VPAIN',0,()),
('PRN',0,()),
('PRP',0,()),
('PRA',0,()),
('PDS',0,()),
('PDP',0,()),
('PNT',0,()),
('INT',0,()),
('$',0,()),
('%',0,()),
('PNCT',0,()),
('PADJ',0,()),
('PREAL',0,()),
('PRL',0,())
]

edges=[]    # Edges list
#this function renders the tag index in the tags kab array
def index_of_tag(tag):
    l=0
    while l< len(tags):
        c= tags[l]
        b=c[0]
        #print (b)
        #print (tag)
        if (tag==b):
            return (l)
        l=l+1






regexp ='[-A-Zḍčǧḥṛṣẓṭţɣɛ« ».,:1-9a-z]+/[A-Z]+' # regular expression to retreive the couple (tagged wor/tag)
text="Tukkist/NMC seg/PRP ungal/NMC «/PNCT iḍ/NMC d/CC wass/NMC »/PNCT sɣur/PRP ɛ.Mezdad/NMP ./PNT Tasa/NMC ur/PRN tessager/VAF yiwen/NC ./PNT Maca/CS d/PREAL win/PRD i/PRP d-/PDP yufraren/VPPP gar/PRP tarwa/NMC -s/PAN ./PNT D/PREAL win/PRD i/PRL tḥemmel/VP aṭas/ADV ./PNT Ur/PRN tuksan/VPN ara/PRN ./PNT D/PREAL win/PRD i/PRL d/PREAL amenzu/NMC i/PRD tessider/VP ./PNT Ula/ADV d/PREAL tuccent/NMC deg/PRP umadaɣ/NMC yezga/VP yiwen/NC gar/PRP tarwa/NMC -s/PAN yufrar/VP -d/PDP ɣef/PRP wiyaḍ/PRI ./PNT Qqaren/VAI d/PREAL ddnub/NMC ɣef/PRP tasa/NMC ma/CC ur/PRN tessaɛdel/VPN tarwa/NMC -s/PAN ,/PNCT ma/CC tella/VP tneḥyaft/VP gar/PRP -asen/PAP ./PNT Neţat/PPA ddnub/NMC ur/PRN t-/PPV tewwi/VPN ara/PRN :/PNCT d/PREAL ayen/PRI ara/PRP yečč/PA wa/PRD i/PRL teţen/VAI wiyaḍ/PRI ./PNT D/PREAL ayen/PRI ara/PRP yels/PA i/PRL ţlusun/VAI daɣen/ADV ./PNT  Asmi/CS meẓẓiy/ADJ d/PREAL amaɛlal/NMC kan/ADV ,/PNCT yeṛwa/VP lehlak/NMC d/PREAL axessar/NMC ./PNT Ulac/ADV aṭṭan/NMC ur/PRN t-/PPV nebla/VPPN Ussan/NMC imenza/NMC mi/CS d-/PDP ilul/VP yedla/VP -d/PDS fell/PRP -as/PAP unezyuf/NMC ,/PNCT yečča/VP -yas/PSV yakk/ADV timeccacin/NMC -is/PAN ./PNT"
text=text.replace("  "," ")
text=text.replace("   "," ")
a=text.split(" ")
i=0
start=0
while i<len(a)-1:

    b=a[i].split("/")  #split a couple
    print (b[1])
    tuplea=tags[index_of_tag(b[1])] #look for the index of the tag
    #print (tuple)
    number=tuplea[1]+1#increment the tag count
    tuple_tag=tuplea[2]
    list_a=list(tuple_tag)
    #print(b[0])
    list_a.append(b[0])
    #print  (list_a)
    tuple_tag=tuple(list_a)
    tags[index_of_tag(b[1])]=(tuplea[0],number,tuple_tag)# update une tag count
    c=a[i+1].split("/") # this is for the last couple word/tag

    if(start==0) and (i==0): # the first start edge : First word in the text or the first edge after a dot
        G.add_edges_from([('Start',b[1])], weight=0)
        edges.append(('Start->'+b[1],1))
        start=1
    elif (start==0):
        G.add_edges_from([('Start',c[1])], weight=0) # edge start -> next word after a dot .
        start=1
        edges.append(('Start->'+c[1],1))

    elif (c[1]=='PNT'):

        G.add_edges_from([(c[1],'Stop')], weight=0) # when a dot is found, create an end
        edges.append((c[1]+'->Stop',1))
        G.add_edges_from([(b[1],c[1])], weight=0) # and create an edge betwen the dot and the previous tags
        edges.append((b[1]+'->'+c[1],1))
        start=0



    else:
        G.add_edges_from([(b[1],c[1])], weight=0) # create and edge between two neighbours
        edges.append((b[1]+'->'+c[1],1))
    i=i+1

# this is for the last tag. We will increment its occurence

G.add_edges_from([(c[1],'Stop')], weight=0) # create and edge between two neighbours
edges.append((c[1]+'->Stop',1))

tuplea=tags[index_of_tag(c[1])]
number=tuplea[1]+1
tuple_tag=tuplea[2]
list_a=list(tuple_tag)
list_a.append(c[0])
tuple_tag=tuple(list_a)
tags[index_of_tag(c[1])]=(tuplea[0],number,tuple_tag)


val_map = {}
values = [val_map.get(node, 0.45) for node in G.nodes()]
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])

red_edges = [('Start','NMC'),('NMC','Stop')]
edge_colors = ['black' if not edge in red_edges else 'black' for edge in G.edges()]

pos=nx.spring_layout(G)

options = {
    'node_color': 'blue',
    'node_size': 800,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 13,
}
color_map = []
j=0
for node in G:
    #print (node)

    if str(node) =='Start' or str(node) =='Stop':
        color_map.append('blue')

    elif (len(str(node))>=4):
        color_map.append('olive')
    elif (len(str(node))==3):
        color_map.append('yellow')
    else:
        color_map.append('purple')
    j=j+1
nx.draw(G,pos, node_color = color_map, node_size=1500,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
#nx.draw_networkx_labels()
#networkx.draw_networkx_labels(graph,node_positions,font_size=16)
#nx.coloring.greedy_color(G, strategy='largest_first')
#nx.draw_networkx(G, arrows=True, **options)
#print (words)i
j=0
labels={}
for i in G.nodes:

    labels[i]=i

nx.draw_networkx_labels(G,pos,labels,font_size=16)

pylab.axis('off')
pylab.show()


# calculate the occurences of grammatical classes ant show them on histogram
x = np.arange(len(tags))
valeurs=[]
symbols=[]
i=0
while i< len (tags):
    if (tags[i][1] != 0):
        valeurs.append(tags[i][1])
        symbols.append(tags[i][0])
    i=i+1

x = np.arange(len(valeurs))
plt.bar(x, height= valeurs)
plt.xticks(x+.5, symbols);
plt.ylabel('Timeḍriwt/Tiseqqaṛ')
plt.xlabel('Ismilen inejrumen')
plt.show()


#calculate probabilities

edges_probabilities=[]

edges_probabilities=[[x,edges.count(x)] for x in set(edges)]
#print (t)





for i in edges_probabilities:
    edges_probabilities[edges_probabilities.index(i)]=(i[0],i[1]/len(edges))

for i in edges_probabilities :
    print (i)

print ('_________________')

x = np.arange(len(tags))
valeurs=[]
symbols=[]
i=0
while i< len (edges_probabilities):
    if (edges_probabilities[i][1] != 0):
        valeurs.append(edges_probabilities[i][1]*100)
        symbols.append(edges_probabilities[i][0][0])
        print (edges_probabilities[i][1]*100,"<-",edges_probabilities[i][0][0])
    i=i+1

x = np.arange(len(valeurs))
plt.bar(x, height= valeurs)
plt.xticks(x+.1, symbols);
plt.ylabel('Probabilité')
plt.xlabel('Transitions')
plt.show()
