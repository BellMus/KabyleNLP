consonnes=['b','c','č','d','ḏ','ḍ','f','g','ḡ','ǧ','h','ḥ','j','k','ḵ','l','m','n','q','r','ṛ','s','ṣ','t','ṯ','ṭ','ţ','v','w','x','y','z','ẓ','ž','ɣ','ɛ']

#classification par mode d'articulation
occlusives_sourdes=['t','ṭ','k','kw','q','qw']
occlusives_voisee=['b','bw','d','g','gw']
affriquee_sourde=['ţ','č']
affriquee_voisee=['ž','ǧ']
frictative_sourde=['v','f','ṯ','s','ṣ','c','cw','ḵ','ḵw','x','xw','ḥ','h']
frictative_voisee=['ḏ','ḍ','z','ẓ','j','jw','ḡ','ḡw','ɣ','ɣw','ɛ']
nasale=['m','n']
lateral=['l','lw']
roulee=['r','ṛ']
spirante=['w','y']

#classification par point d'articulation
bilabiale_plaine=['b','v','m','w']
bilabiale_labiale=['bw']
labiodentale=['f']
interdentale_plaine=['ṯ','ḏ']
interdentale_emphatique=['ḍ']
dental_plaine=['t','d','n','l','r']
dental_emphatique=['ṭ','lw','ṛ']
alveolaire_plaine=['ţ','ž','s','z']
alveolaire_emphatique=['ṣ','ẓ']
postalveolaire_plaine=['č','ǧ','c','j']
postalveolaire_emphatique=['cw','jw']
palatale_plaine=['ḡ','ḵ','y']
palatale_labiale=['ḡw','ḵw']
velaire_plaine=['k','g']
velaire_labiale=['kw','gw']
uvulaire_plaine=['q','ɣ','x']
uvulaire_labiale=['qw','ɣw','xw']
pharyngale=['ḥ','ɛ']
glottale=['h']


def mode_articulation (i):

    if (i in occlusives_sourdes):
        return 'occlusive sourde'

    elif (i in occlusives_voisee):
        return 'occlusive voisée'

    elif (i in affriquee_sourde):
        return 'affriquée sourde'
    elif (i in affriquee_voisee):
        return 'affiruqée voisée'
    elif (i in frictative_sourde):
        return 'frictative sourde'
    elif (i in frictative_voisee):
        return 'frictative voisée'
    elif (i in nasale):
        return 'nasale'
    elif (i in lateral):
        return 'laterale'
    elif (i in roulee):
        return 'roulée'
    elif (i in spirante):
        return 'spirante'

def point_articulation(i):
    if (i in bilabiale_plaine):
        return 'bilabiale  plaine'
    elif (i in bilabiale_labiale):
        return 'bilabiale labiale'
    elif (i in labiodentale):
        return 'labiodentale'
    elif (i in interdentale_plaine):
        return 'interdentale plaine'
    elif (i in interdentale_emphatique):
        return 'interdentale emphatique'
    elif (i in dental_plaine):
        return 'dentale plaine'
    elif (i in dental_emphatique):
        return 'dentale emphatique'
    elif (i in alveolaire_plaine):
        return 'alveolaire plaine'
    elif (i in alveolaire_emphatique):
        return 'alveolaire emphatique'
    elif (i in postalveolaire_plaine):
        return 'postalveolaireplaine'
    elif (i in postalveolaire_emphatique):
        return 'postalveolaire emphatique'
    elif (i in palatale_plaine):
        return 'palatale plaine'
    elif (i in palatale_labiale):
        return 'palatale labiale'
    elif (i in velaire_plaine):
        return 'velaire plaine'
    elif (i in velaire_labiale):
        return 'velaire labiale'
    elif (i in uvulaire_plaine):
        return 'uvulaire plaine'
    elif (i in 'uvulaire_labiale'):
        return 'uvulaire labiale'
    elif (i in pharyngale):
        return 'pharyngale'
    elif (i in glottale):
        return 'glotale'



for line in open("C:/tal/corpus-preterit7.txt",encoding='utf8'):
    i = line.split()
    if (len(i)>0):
        i=i[0]
        if(len(i)>0):
         #print (i)
         print (i,'->',mode_articulation (i[0:1]),'/',point_articulation(i[0:1]),'-->',mode_articulation (i[1:2]),'/',point_articulation(i[1:2]))

