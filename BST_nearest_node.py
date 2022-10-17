
import unittest

def findClosestValueInBst(tree,target):
    return findClosestValueInBstHelper(tree,target,tree.value)

def findClosestValueInBstHelper(tree,target,closest):
    currentNode=tree
    while currentNode is not None:
        if abs(target-closest)>abs(target-currentNode.value):
            closest=currentNode.value
        if target<currentNode.value:
            currentNode=currentNode.left
        elif target>currentNode.value:
            currentNode=currentNode.right
        else:
            break
    return closest
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = findClosestValueInBst(root, 12)
        print(actual)
        self.assertEqual(expected, actual)
