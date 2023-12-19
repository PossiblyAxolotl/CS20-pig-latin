# PossiblyAxolotl
# Pig Latin Converter
# -=-=-=-=-=-=-=-=-=-=-=-=-
# Started Dec 19, 2023
# Last updated Dec 19, 2023

import streamlit as st

st.set_page_config(
    page_title="Pig Latin Converter",
    page_icon="🐷",
)

### processing

def pop_prefix(text):
    '''Separate the prefix from the text and return both the prefix and remaining text'''
    
    vowels = "aeiouy"
    
    lower_text = text.lower()
    
    # loop through vowels to find the first instance of one
    first_vowel = len(text)
    for vowel in vowels:
        vowel_location = lower_text.find(vowel)
        
        if vowel_location < first_vowel and vowel_location != -1:
            first_vowel = vowel_location
    
    # separate prefix from the reset of the word
    prefix = text[:first_vowel]
    remainder = text[first_vowel:]
    
    return prefix, remainder

def pop_punctuation(word):
    '''Return the word and the ending punctuation from it'''
    
    # initalize variables
    punctuation = ",.:;!?"
    end_symbol = ""
    
    # loop through symbols and remove any included from the text
    for symbol in punctuation:
        if symbol == word[-1]:
            end_symbol = symbol
            
            word = word[:-1] # character from word
            break
    
    return word, end_symbol

def pigify(word):
    '''Turn a word into pig latin.'''
    
    # get prefix and remainder
    prefix, remainder = pop_prefix(word.lower())

    # add y if there's no prefix for "yay"
    if len(prefix) < 1:
        prefix += "y"
    
    # reorder word parts
    new_word = remainder + prefix + "ay"
    
    # check if the word starts capitalized and transfer over
    starts_capitalized = word[0].isupper()
    
    if starts_capitalized:
        new_word = new_word.upper()[0] + new_word[1:]
    
    return new_word

def pigify_sentence(sentence):
    '''Turns the entire sentence into pig latin.'''
    
    sentence = sentence.strip()

    # return empty sentence
    if sentence == "":
        return ""

    # split sentence into individual words
    split_sentence = sentence.split(" ")
    
    pig_sentence = ""
    
    # remove punctuation, pigify the word, add back punctuation, and add a space
    for word in split_sentence:
        if not word.isnumeric():
            word, punctuation = pop_punctuation(word)
            
            pig_sentence += pigify(word) + punctuation + " "
        else:
            pig_sentence += word + " "
    
    # remove extra space from end
    return pig_sentence.removesuffix(" ")

### streamlit

'''
# Pig Latin Converter
'''

text_input = st.text_area("English Text", placeholder="The quick brown fox jumps over the lazy dog.")

st.write(pigify_sentence(text_input))