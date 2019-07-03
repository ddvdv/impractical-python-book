"""Work with palindrom and palingram."""

import load_dictionary

dictionnary = load_dictionary.load('chap2/2of4brif.txt')
palindromes = []

for word in dictionnary:
    if word[:] == word[::-1]:
        palindromes.append(word)

print(*palindromes, sep="\n")
    