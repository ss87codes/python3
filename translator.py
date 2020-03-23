
"""
This program takes as input a name. if there is any vowel in the name
, replace it with the number 9
"""
vowels = ['a','A','e','E','i','I','o','O','u','U']

def translate(phrase):
    translated_word = ""
    for letter in phrase:
        if letter in vowels:
            translated_word = translated_word + "9"
        else:
            translated_word = translated_word + letter
    return translated_word

user_input = input("Please enter the word: ")
print(translate(user_input))

