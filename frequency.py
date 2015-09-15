# -*- coding: utf-8 -*-s
from collections import Counter
import os
import enchant
#stackoverflow.com/questions/11804481/pyenchant-without-german-dictionary
#Guide to install dictionaries

c = """VaqrprzoreoeratraWhyvhfraJnygreUbyynaqreqrgjrroebrefinaRqvguZnetbganne
NzfgreqnzNaarjvytenntzrrxbzraznnezbrgabtrrarragvwqwrovwbznoyvwiraBznmnyurgzbrvyvwxuroorabzNaarabtrracnnejrxraqnnegrubhqrafpuev
wsgRqvguSenaxvarraoevrsnnaTregehqAnhznaauhaiebrtrerohhezrvfwrvaSenaxs
hegnzZnva"""

current_c = ""

#Freq_in_cipher ranevzbgqhoutwyfsxjipcm
english_freq = "etaoinsrhldcumfpgwybvkxjqz"
d_eng = enchant.Dict("en_UK")

dutch_freq = "enatirodslghvkmubpwjczfxyq"
d_nl = enchant.Dict("nl")

#e n a t i r o d s l g h v k m u b p w j c z f x y (ë é ó) q
german_freq = "enisratdhulcgmobwfkzvpjyqx"
d_de = enchant.Dict("de_DE")

#e n i s r a t d h u l c g m o b w f k z v ü p ä ß j ö y q x
turkish_freq = "aeinrldkmuytsbozghvcpfjwxq"
#No turkish spell check
#a e i n r l ı d k m u y t s b o ü ş z g ç h ğ v c ö p f j w x q

sub_dict = {}

MAX_WORD_LENGTH = 15
MIN_WORD_LENGTH = 3
DICTIONARY = d_nl
FREQUENCY = dutch_freq


def brute_force_match_count(language_dict, c):
    match_count = 0
    for i in range(len(c)):
        for j in range(i + MIN_WORD_LENGTH, i + MAX_WORD_LENGTH + 1):
            if(j <= len(c)):
                word = c[i: j]
                #print c[i: j]
                if(language_dict.check(word)):
                    match_count = match_count + 1
                    print word, " ",
    print ""
    return match_count


if __name__ == "__main__":
    freq = Counter(c.lower()).most_common()
    f = [x[0] for x in freq if (x[0] != '\n')]
    sub_dict = dict(zip(f, FREQUENCY))

    while(1):
        os.system('clear')
        current_c = ""
        for l in c.lower():
            if(l in sub_dict):
                current_c = current_c + sub_dict[l]
            else:
                current_c = current_c + l

        print "ORIGINAL:"
        print c
        print "\nSUBSTITUTIONS: ", len(sub_dict)
        print sub_dict
        print "\nLETTER FREQUENCY IN THE CIPHERTEXT:"
        print f
        print "\nWITH SUBSTITUTIONS:"
        print current_c

        print "\nMATCHES: "
        count = brute_force_match_count(DICTIONARY, current_c)
        print count, " Words mathing."

        s1 = raw_input("\nInsert char to sub: ")
        s2 = raw_input("Insert sub: ")
        #c = c.replace(s1, s2)
        sub_dict[s1] = s2
