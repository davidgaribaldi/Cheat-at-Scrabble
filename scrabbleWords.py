# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 14:48:29 2019

@author: davidg
"""

import string

# Take the unused letters and capitalize them and those to the next function
def uppercaseLetters(used_letters, alphabet):
    upper_Letters = []
    for l in used_letters:
        letter = l.upper()
        upper_Letters.append(letter)
#    print(upper_Letters)
    return unused_Letters(upper_Letters, alphabet)

# Will take letters in play and remove them from the alphabet and 
# send the alphabet minus inplay letters to the next function
def unused_Letters(letters, alphabet):
    for l in letters:                       
        alphabet.remove(l)
#    print(alphabet)
    return findPlayableWords(alphabet)

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
 
# Very similar to findPlayableWords, it takes that list and then removes all words with extra letters
# If we only have 1 A we can't play alas since we only have the one A.
def duplicateLetters(usable_Words):
    bad_Word_List = []
    for word in usable_Words:
        dupe_word = removeOffenders(word)
        if dupe_word != None:
            bad_Word_List.append(dupe_word)
    for word in bad_Word_List:
            usable_Words.remove(word)
    return usable_Words

# Actually finds the words with multiple of the same letter.                
def removeOffenders(word):
    for w in word:
        if word.count(w) > 1:
            return word

word_Score = 0
high_Score = 0
high_Scores = {}
scrabble_Scoring = {}
alphabet = list(string.ascii_uppercase)
values = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
scrabble_Scoring = dict(zip(alphabet, values))

unused_letters = []
used_letters = ['d', 'a', 'v', 'i', 'm']

usable_Words = uppercaseLetters(used_letters, alphabet)
#print(usable_Words)
usable_Words = duplicateLetters(usable_Words)
#print(usable_Words)


#Attributes scores to word based off of scrabble_Scoring
for word in usable_Words:
    for w in word:
        word_Score = word_Score + scrabble_Scoring[w]
        high_Scores[word] = word_Score
    if word_Score >= high_Score:
        high_Score = word_Score
    word_Score = 0

# Prints out the word and the score it would get if there were no modifiers 
# for all of the highest scoring words
for word, score in high_Scores.items():
    if score >= high_Score - 3:
        print(word, score)









