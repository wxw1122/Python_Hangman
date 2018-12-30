#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 23:51:03 2018

@author: XiaoweiWang
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    all_letters = list(string.ascii_lowercase)
    Not = []
    for k in all_letters:
        if k not in lettersGuessed:
            Not.append(k)
    return(''.join(Not))