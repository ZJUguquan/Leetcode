#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jinyongyang
# @Date:   2015-08-09 00:59:46
# @Last Modified by:   jinyongyang
# @Last Modified time: 2015-08-09 01:06:02

import string


class CaesarCipher(object):

    key = -1

    def __init__(self, shift):
        self.key = shift

    def encode(self, message):
        transtab = string.maketrans(
            string.ascii_uppercase,
            string.ascii_uppercase[self.key % 26: 26] +
            string.ascii_uppercase[:self.key % 26])
        return message.upper().translate(transtab)


    def decode(self, message):
        transtab = string.maketrans(
            string.ascii_uppercase[self.key % 26: 26] +
            string.ascii_uppercase[:self.key % 26], string.ascii_uppercase)
        return message.upper().translate(transtab)



message = 'Codewars'
c = CaesarCipher(5);

print(c.encode('Codewars') )#, 'HTIJBFWX');
print(c.decode('HTIJBFWX') )#, 'CODEWARS');