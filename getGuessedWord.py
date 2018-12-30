#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 23:30:07 2018

@author: XiaoweiWang
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    Guess = ['_']*len(secretWord)
    for k in lettersGuessed:
        i = 0
        for l in secretWord:
            if l == k:
                Guess[i] = k
            i+=1
    return(' '.join(Guess))
            