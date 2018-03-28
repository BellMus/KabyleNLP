suffixe=[]
prefixe=[]

Ponctuation=['.',',',';','?','!',':','"','(',')','*','_']
#Construct suffixes and prefixes dictionaries
for i in open("c:/tal/affixescolles.txt",encoding='utf-8'):
    a=i
    a=a.replace("\ufeff","")
    a=a.replace("\n","")
    if (a[len(a)-1]=="-"):

     prefixe.append(str(a))
    else:
       suffixe.append(str(a))
#tokinize a token separated by spaces, exract unique morphemes : affixes and word affixed
def tokenize_word(word,suffixe,prefixe):
    a=''
    morpheme=word[0:word.find('-')+1]

    lemtized_word=' '
    if (morpheme in prefixe):
        word=word[word.find('-')+1:len(word)]
        lemtized_word=lemtized_word+' '+morpheme
        while word.find('-')>=0:

            morpheme=word[0:word.find('-')+1]
            word=word[word.find('-')+1:len(word)]
            lemtized_word=lemtized_word+' '+morpheme
        lemtized_word=lemtized_word+' '+word
    else:
        morpheme=word[0:word.find('-')]
        lemtized_word=lemtized_word+' '+morpheme
        word=word[word.find('-')+1:len(word)]
        while word.find('-')>=0:

           morpheme=word[0:word.find('-')]
           lemtized_word=lemtized_word+' '+'-'+morpheme
           word=word[word.find('-')+1:len(word)]
        lemtized_word=lemtized_word+' '+'-'+word



    return lemtized_word

# Lematize a sentence
def tokenize(sentence,suffixe,prefixe):
       a=sentence.split()
       sentence1=""
       for i in a: #mots
        if(i.find('-')<0):
            sentence1=sentence1+' '+i
        else:
            words=tokenize_word(i,suffixe,prefixe)
            sentence1=sentence1+' '+words
       return sentence1


text=""

f= open("c:/tal/mhenna_tokenized.txt","w+",encoding='utf-8') #file tokennized
g=open("c:/tal/mhenna.txt",encoding='utf-8') { file to tokennize
for line in g:
    #put ponctuaction between spaces
    for i in Ponctuation:

        if i=='.':
            line=line.replace(i,' '+i+' ')
        else:
            line=line.replace(i,' '+i+' ')

    ligne=tokenize(line,suffixe,prefixe)

    ligne=ligne.replace("  "," ")# delete double spaces
    ligne=ligne+'\n' # add the line end
    f.write(ligne)

f.close()
g.close()
