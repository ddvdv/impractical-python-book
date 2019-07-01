"""Pig Latin converter."""
input_sentence = input("Enter the sentence you want to translate to Pig Latin:
                ")
input_array = input_sentence.split()
result_array = []

for word in input_array:
    if word.isalpha():
        first_letter = word[0]
        new_word = ""
        if first_letter in ["a", "e", "i", "o", "u"]:
            new_word = word + "way"
        else:
            new_word = word[1:]
            new_word += first_letter
            new_word = new_word + "ay"
        result_array.append(new_word)
    else:
        result_array.append(word)

print(" ".join(result_array))
