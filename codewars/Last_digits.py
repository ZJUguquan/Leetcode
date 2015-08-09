#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jinyongyang
# @Date:   2015-08-09 20:42:04
# @Last Modified by:   jinyongyang
# @Last Modified time: 2015-08-09 20:42:24

def solution(digits):
    o = 0
    for i in range( len(str(digits)) - 4):
        if int(str(digits)[i: i+ 5]) > o:
            o = int(str(digits)[i: i+ 5])
    return o;


print solution(123456)