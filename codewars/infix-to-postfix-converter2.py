# -*- coding: utf-8 -*-
'''
Created on 14 Feb , 2015

@author: stevey
'''

# infix to Postfix converter

class InfixTree:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + str(self.root) + str(self.right)

primary = ['*', '/', '^']
secondary = ['+', '-']
numbers = ['0', '1', '2', '3', '4', '5' '6', '7', '8', '9']

def parse_operators(infix, operators):
    # loop while all operators are found
    while True:
        found_operators = False
        for idx, val in enumerate(infix):
            if val in operators:
                found_operators = True
                a = infix[idx - 1]
                b = infix[idx + 1]
                # replace operators and operands with a syntax tree
                infix[idx] = InfixTree(val, a, b)
                del infix[idx - 1]
                del infix[idx]
                break

        if found_operators == False:
            break

def parse_parenthesis(infix):
    cnt_par = -1
    start_idx = -1
    end_idx = -1
    # loop while all parentheses are found
    while True:
        found_parenthesis = False
        for idx, val in enumerate(infix):
            if not isinstance(val, str):
                continue
            # find the outer most brackets
            if '(' in val and cnt_par == -1:
                cnt_par = 1
                start_idx = idx
                found_parenthesis = True
            elif '(' in val:
                cnt_par += 1
            elif ')' in val:
                cnt_par -= 1

            if cnt_par == 0:
                end_idx = idx
                cnt_par = -1

                infix[start_idx] = solve(infix[start_idx + 1:end_idx])
                del infix[start_idx + 1:end_idx + 1]
                break

        if found_parenthesis == False:
            break


    return len(infix)

def solve(infix):

    # solve for parenthesis
    parse_parenthesis(infix)

    # solve for primary operators
    parse_operators(infix, primary)

    # solve for secondary operators
    parse_operators(infix, secondary)


    while len(infix) > 1:
        solve(infix)

    return infix[0]

def preorder_traversal(root):

    if isinstance(root, str):
        return root

    left = preorder_traversal(root.left)
    right = preorder_traversal(root.right)

    return left + right + root.root

def to_postfix (infix):
    """Convert infix to postfix"""
    infix = [x for x in infix]

    solve(infix)

    return preorder_traversal(solve(infix))