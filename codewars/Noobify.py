#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jinyong.Yang
# @Date:   2015-11-14 23:25:26
# @Last Modified by:   Jinyong.Yang
# @Last Modified time: 2015-11-14 23:39:04


def header(text):
    raw_text = text
    if len(text) > 31:
        text = 'OMG ' + text
    if raw_text.startswith('w'):
        text = 'LOL ' + text
    if raw_text.startswith('h'):
        text = text.upper()
    return text


def checkword(word):
    transform = {'to': '2', 'too': '2',
                 'for': '4', 'fore': '4',
                 'be': 'b', 'are': 'r', 'you': 'u',
                 'please': 'plz', 'people': 'ppl', 'really': 'rly',
                 'have': 'haz', 'know': 'no'
                 }
    if word in transform:
        return transform[word].upper(), 1
    elif 'o' in word or 's' in word:
        return word.replace('s', 'z').replace('o', '0').upper(), word.count('o') + word.count('s')
    else:
        return word, 0

def no_token(text):
    return text.replace('.','').replace(',', '').replace('\'', '')


# start with w + LOL
# length >= 32 + OMG
