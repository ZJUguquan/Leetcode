#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jinyong.Yang
# @Date:   2015-12-02 11:27:02
# @Last Modified by:   Jinyong.Yang
# @Last Modified time: 2015-12-02 11:41:55


import re


# def seven_ate9(s):
#     return re.sub(r'(7+)(9+)', lambda m: str(m.group(1)), s)


def seven_ate9(s):
    while '797' in s:
        s = s.replace('797', '77')
    return s
