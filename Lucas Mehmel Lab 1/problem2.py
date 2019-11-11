'''
   Author: Lucas Mehmel
   Course: CSC 112L
   Program: problem2.py
'''
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.leftchild = None
        self.rightchild = None

class BST:
    def __init__(self, key):
        self.root = key

    def add(self, somevalue):
        if self.root == None:
            return self.root = TreeNode(somevalue)
        else:
            self._add_aux(self.root,value)

    def _add_aux(self, currentnode, somevalue):
        if somevalue <= currentnode:
            if currentnode.leftchild == None:
                return currentnode.leftchild = TreeNode(somevalue)
            else:
                return _add_aux(currentnode.leftchild, somevalue)
        else:
            if currentnode.rightchild == None:
                return currentnode.rightchild = TreeNode(somevalue)
            else:
                return _add_aux(currentnode.rightchild, somevalue)
            
    def print_inorder(self):
        self._print_inorder_aux(self.root)

    def _print_inorder_aux(self, currentnode):
        if not currentnode: return
        self._print_inorder_aux(currentnode.leftchild)
        print(treenode.value)
        self._print_inorder_aux(currentnode.rightchild)
        
            

        
