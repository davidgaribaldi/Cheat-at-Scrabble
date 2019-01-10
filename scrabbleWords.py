# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 14:48:29 2019

@author: davidg
"""

import string

# Will take letters in play and remove them from the alphabet and 
# send the alphabet minus inplay letters to the next function
def unused_Letters(letters, alphabet):
    for l in letters:                       
        alphabet.remove(l)
    print(alphabet)
    return uppercaseLetters(alphabet)

# Take the unused letters and capitalize them and those to the next function
def uppercaseLetters(unused_letters):
    upper_Letters = []
    for l in unused_letters:
        letter = l.upper()
        upper_Letters.append(letter)
    print(upper_Letters)
    return findPlayableWords(upper_Letters)

# Function will take in ununsed capital letters and find words that have them
# and add them to a bad_word_list. Then it will remove those bad_words from the good_list
def findPlayableWords(unused_Upper_Letters):
    bad_word = ''
    bad_word_list = []
    with open("sowpods.txt") as f:
        word_List = f.read().splitlines()
    for word in word_List:
        bad_word = function(word, unused_Upper_Letters)
        if bad_word != None:
            bad_word_list.append(bad_word)
    for word in bad_word_list:
        word_List.remove(word)
    return word_List

# findPlayableWords sends all words down here to see if bad letters are in words
# If a bad letter is in a word then it sends to the word up to be added to the list
def function(word, letters):
    for w in word:
        if w in letters:
            return word

scrabble_Scoring = {}
alphabet = list(string.ascii_lowercase)
values = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
scrabble_Scoring = dict(zip(alphabet, values))

unused_letters = []
used_letters = ['a', 'e', 'c', 'p', 'b', 's', 'r','i']

useable_Words = unused_Letters(used_letters, alphabet)
