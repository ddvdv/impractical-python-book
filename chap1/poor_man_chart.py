"""Poor man chart, take sentence as input and produce a chart.
showing the usage of each letter."""

import pprint

sentence = input("Enter a sentence you would like to analyze:  ")
sentence_array = list(sentence)
sentence_dict = {}

for letter in sentence_array:
    if letter.isalpha():
        if letter in sentence_dict:
            sentence_dict[letter].append(letter)
        else:
            sentence_dict[letter] = []


pprint.pprint(sentence_dict)
