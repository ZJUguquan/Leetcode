#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jinyong.Yang
# @Date:   2015-11-17 13:43:53
# @Last Modified by:   Jinyong.Yang
# @Last Modified time: 2015-11-17 13:46:51


def factory(Number):

    def multiply(args):
        res = [i*Number for i in args]
        return res

    return multiply


myarr = [1,2,3]

five = factory(5)

print(five(myarr))