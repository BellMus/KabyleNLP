import nltk
import sys

brown_tags_words = [ ]
brown_tags_words1 = [ ]

text=""
ligne=""
first=0
for ligne in open("c:/tal/corpuspos.txt",encoding='utf-8'):
    if (first!=0):
     brown_tags_words1.append( ("START", "START") )
    #brown_tags_words1.extend([ (tag[:2], word) for (word, tag) in ligne ])
     ligne=ligne.lower()
     ligne=ligne.replace("\n","")
     a=ligne.split(" ")

     for i in a:
        b=i.split("/")
        brown_tags_words1.append( (b[1],b[0]))
     brown_tags_words1.append( ("END", "END") )
    first=1

      #split a couple

print (brown_tags_words1)

# conditional frequency distribution
cfd_tagwords = nltk.ConditionalFreqDist(brown_tags_words1)
print (cfd_tagwords)
# conditional probability distribution
cpd_tagwords = nltk.ConditionalProbDist(cfd_tagwords, nltk.MLEProbDist)

cfd_tagwords = nltk.ConditionalFreqDist(brown_tags_words1)
# conditional probability distribution
cpd_tagwords = nltk.ConditionalProbDist(cfd_tagwords, nltk.MLEProbDist)

print("tiseqqar akken 'tukkist' ad yili d isem ", cpd_tagwords["nmc"].prob("tukkist"))
print("tiseqqar akken 'seg' ad yili d tanzeɣt", cpd_tagwords["prp"].prob("seg"))
print("tiseqqar akken 't-' ad yili d amqim uzwir n umyag", cpd_tagwords["ppv"].prob("t-"))
kab_tags = [tag for (tag, word) in brown_tags_words1 ]
cfd_tags= nltk.ConditionalFreqDist(nltk.bigrams(kab_tags))

cpd_tags = nltk.ConditionalProbDist(cfd_tags, nltk.MLEProbDist)

print("Ma nufa-d tazelɣa n tuqqna 'd', tiseqqar n yisem ara tt-id-iḍefren d", cpd_tags["cc"].prob("nmc"))
print( "Ma nufa-d tazelɣa n tilawt 'd', tiseqqar n yisem ara tt-id-iḍefren d", cpd_tags["preal"].prob("nmc"))
print( "Ma nufa-d tazelɣa n tilawt 'd', tiseqqar n umyag urmir ara ti-id-iḍefṛen", cpd_tags["preal"].prob("va"))

prob_tagsequence = cpd_tags["START"].prob("prn") * cpd_tagwords["prn"].prob("ur") * \
    cpd_tags["prn"].prob("vpn") * cpd_tagwords["vpn"].prob("tuksan") * \
    cpd_tags["vpn"].prob("prn") * cpd_tagwords["prn"].prob("ara") * \
    cpd_tags["prn"].prob("pnt") * cpd_tagwords["pnt"].prob(".") * \
    cpd_tags["pnt"].prob("END")


print( "Taseqqart n 'START prn vpn prn END' i 'Ur tuksan ara.:", prob_tagsequence)

#---------------------

distinct_tags = set(kab_tags)
#print (distinct_tags,'!!!!!!')

sentence = ["yenwa", "ad", "yeffeɣ","."]
#sentence = ["iɣil", "yektil", "her", "duck" ]
sentlen = len(sentence)

# viterbi:
# for each step i in 1 .. sentlen,
# store a dictionary
# that maps each tag X
# to the probability of the best tag sequence of length i that ends in X
viterbi = [ ]

# backpointer:
# for each step i in 1..sentlen,
# store a dictionary
# that maps each tag X
# to the previous tag in the best tag sequence of length i that ends in X
backpointer = [ ]

first_viterbi = { }
first_backpointer = { }
for tag in distinct_tags:
    # don't record anything for the START tag
    if tag == "START": continue
    first_viterbi[ tag ] = cpd_tags["START"].prob(tag) * cpd_tagwords[tag].prob( sentence[0] )
    first_backpointer[ tag ] = "START"

print(first_viterbi)
print(first_backpointer)

viterbi.append(first_viterbi)
backpointer.append(first_backpointer)

currbest = max(first_viterbi.keys(), key = lambda tag: first_viterbi[ tag ])
print( "Word", "'" + sentence[0] + "'", "current best two-tag sequence:", first_backpointer[ currbest], currbest)
# print( "Word", "'" + sentence[0] + "'", "current best tag:", currbest)

for wordindex in range(1, len(sentence)):
    this_viterbi = { }
    this_backpointer = { }
    prev_viterbi = viterbi[-1]

    for tag in distinct_tags:
        # don't record anything for the START tag
        if tag == "START": continue

        # if this tag is X and the current word is w, then
        # find the previous tag Y such that
        # the best tag sequence that ends in X
        # actually ends in Y X
        # that is, the Y that maximizes
        # prev_viterbi[ Y ] * P(X | Y) * P( w | X)
        # The following command has the same notation
        # that you saw in the sorted() command.
        best_previous = max(prev_viterbi.keys(),
                            key = lambda prevtag: \
            prev_viterbi[ prevtag ] * cpd_tags[prevtag].prob(tag) * cpd_tagwords[tag].prob(sentence[wordindex]))

        # Instead, we can also use the following longer code:
        # best_previous = None
        # best_prob = 0.0
        # for prevtag in distinct_tags:
        #    prob = prev_viterbi[ prevtag ] * cpd_tags[prevtag].prob(tag) * cpd_tagwords[tag].prob(sentence[wordindex])
        #    if prob > best_prob:
        #        best_previous= prevtag
        #        best_prob = prob
        #
        this_viterbi[ tag ] = prev_viterbi[ best_previous] * \
            cpd_tags[ best_previous ].prob(tag) * cpd_tagwords[ tag].prob(sentence[wordindex])
        this_backpointer[ tag ] = best_previous

    currbest = max(this_viterbi.keys(), key = lambda tag: this_viterbi[ tag ])
    print( "Word", "'" + sentence[ wordindex] + "'", "current best two-tag sequence:", this_backpointer[ currbest], currbest)
    # print( "Word", "'" + sentence[ wordindex] + "'", "current best tag:", currbest)


    # done with all tags in this iteration
    # so store the current viterbi step
    viterbi.append(this_viterbi)
    backpointer.append(this_backpointer)


# done with all words in the sentence.
# now find the probability of each tag
# to have "END" as the next tag,
# and use that to find the overall best sequence
prev_viterbi = viterbi[-1]
best_previous = max(prev_viterbi.keys(),
                    key = lambda prevtag: prev_viterbi[ prevtag ] * cpd_tags[prevtag].prob("END"))

prob_tagsequence = prev_viterbi[ best_previous ] * cpd_tags[ best_previous].prob("END")

# best tagsequence: we store this in reverse for now, will invert later
best_tagsequence = [ "END", best_previous ]
# invert the list of backpointers
backpointer.reverse()

# go backwards through the list of backpointers
# (or in this case forward, because we have inverter the backpointer list)
# in each case:
# the following best tag is the one listed under
# the backpointer for the current best tag
current_best_tag = best_previous
for bp in backpointer:
    best_tagsequence.append(bp[current_best_tag])
    current_best_tag = bp[current_best_tag]

best_tagsequence.reverse()
print( "The sentence was:", end = " ")
for w in sentence: print( w, end = " ")
print("\n")
print( "The best tag sequence is:", end = " ")
for t in best_tagsequence: print (t, end = " ")
print("\n")
print( "The probability of the best tag sequence is:", prob_tagsequence)


