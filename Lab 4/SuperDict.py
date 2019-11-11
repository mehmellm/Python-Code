'''
   Author: Jacob Mineo, Lucas Mehmel
   Course: CSC 112 lab
   program: SuperDict.py
   Purpose: 
'''
from Array import *
from BST import *

class SuperDict:
    def __init__(self, size=10):
        self.array = Array(size)
        self.max = size
        self.numused = 0
        self.tree = BST()
        self.debug = False

    # all your other methods here
    def hash_value(self, key):
        sum_key = SuperDict.hash_value_sum(key)
        hash_val = sum_key % self.max
        counter = 0
        while True:
                    if self.array[hash_val] != None:
                        hash_val += 1
                        counter += 1
                    if counter == self.max:
                        print("Error!!! No more space.")
                        return hash_val
                    if self.array[hash_val] == None:
                        return hash_val
                    if hash_val == len(self.array):
                        hash_val = 0
                    counter += 1
        
        def hash_value_sum(key):
            lenkey = 0
            for ch in key:
                lenkey += ord(ch)
            return lenkey

        def put(self,key,value):
            assert type(key) is str, "Parameter must be a string"
            assert type(value) is str, "Parameter must be a string"
            n = self.hash_value(key)
            if self.array[n] == None:
                node = BST.find(value)
                if node != None:
                    node.keylist.append(key)
                else:
                    BST.attach(value, key)
            else:
                old_val = self.array[n][1].payload
                old_key = self.array[n][1].keylist
                old_key.remove(key)
                node = BST.find(value)
                if node != None:
                    node.keylist.append(key)
                else:
                    BST.attach(value, key)
            self.array[n] = key, node
        def get(self, key):
            assert type(key) is str, "Parameter must be a string"
            n = self.hash_value(key)
            if self.array[n] == None:
                return None
            else:
                return self.array[n][1].payload
        def findKeys(self, value):
            assert type(value) is str, "Parameter must be a string"
            n = BST.find(value)
            if n == None:
                return None
            else:
                return n.keylist
        def getKeys():
            return[item[0] for item in self.array if item != None]
                    
        def getValues():
            return BST.makeList2()
                    
                
            

            
            
            
