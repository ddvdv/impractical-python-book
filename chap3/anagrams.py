"""Detect anagrams from dictionnary."""

import load_dictionary

dictionnary = load_dictionary.load('chap2/2of4brif.txt')

user_word = input("Enter a word to find its anagrams: ")
anagrams_results = []
user_word_sorted = sorted(user_word)

for word in dictionnary:
    word_sorted = sorted(word)
    if user_word_sorted == word_sorted and user_word != word:
        anagrams_results.append(word)

print("Anagrams = ", *anagrams_results, sep="\n")
