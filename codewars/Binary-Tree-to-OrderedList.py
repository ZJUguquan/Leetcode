# coding: utf-8


# source: http://www.codewars.com/kata/54cec50f975ca6388a000b36/train/python


def tree_to_preorder_list(node):
    return [] if not node else [node.data,] + tree_to_preorder_list(node.left) + tree_to_preorder_list(node.right)

def tree_to_inorder_list(node):
    return [] if not node else tree_to_inorder_list(node.left) + [node.data,] + tree_to_inorder_list(node.right)

def tree_to_postorder_list(node):
    return [] if not node else tree_to_postorder_list(node.left) + tree_to_postorder_list(node.right) + [node.data,]


===== thnn


def tree_to_inorder_list(node, rootMID = []):
    if not node: return rootMID
    if node.left is not None:
        tree_to_inorder_list(node.left)
    if node.right is not None:
        tree_to_inorder_list(node.right)
    rootMID.append(node.data)
    return rootMID


def tree_to_preorder_list(node, rootFIRST = []):
    if not node: return rootFIRST
    rootFIRST.append(node.data)
    if node.left is not None:
        tree_to_preorder_list(node.left)
    if node.right is not None:
        tree_to_preorder_list(node.right)
    return rootFIRST

def tree_to_postorder_list(node, rootLAST = []):
    if not node: return rootLAST
    if node.left is not None:
        tree_to_postorder_list(node.left)
    if node.right is not None:
        tree_to_postorder_list(node.right)
    rootLAST.append(node.data)
    return rootLAST


