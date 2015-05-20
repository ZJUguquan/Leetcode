# coding: utf-8


# source: http://www.codewars.com/kata/54cec50f975ca6388a000b36/train/python
return_inorder = []
return_preorder = []
return_postorder = []


def tree_to_inorder_list(node):
    if node:
        tree_to_inorder_list(node.left)
        return_inorder.append(node.data)
        tree_to_inorder_list(node.right)


def tree_to_preorder_list(node):

    if node:
        return_preorder.append(node.data)
        tree_to_preorder_list(node.left)
        tree_to_preorder_list(node.right)


def tree_to_postorder_list(node):
    if node:
        tree_to_postorder_list(node.left)
        tree_to_postorder_list(node.right)
        return_postorder.append(node.data)
