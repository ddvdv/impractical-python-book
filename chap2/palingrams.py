"""Generate palingrams from dictionnary."""

import load_dictionary

dictionnary = load_dictionary.load('2of4brif.txt')
palingrams = []

for word in dictionnary:
    if len(word) > 1:
        for i in range(0, len(word)):
            if word[0:i:-1] in dictionnary and word[i:] == word[i::-1]:
                print(word)
                palingrams.append(word)

""" 
    if lengt >1
        for letter in word
            if first part in list and second part lindrom
                append wod to list
            if reverse word at the end of the word and first part palindrom
                append word t list """

palingrams_sorted = palingrams.sort()
print(palingrams_sorted)
