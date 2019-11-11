"""
Stack interface.
file: myStack.py
author: Arthur Nunes-Harwitt
This is the Stack data structure implemented by linked node sequences.

The Stack datatype constructor makes a growable stack of nodes.

"""

from typing import Any, Union
from dataclasses import dataclass

@dataclass
class Node:
    value: Any
    rest: Union[None, 'Node']

@dataclass
class Stack:
    size: int
    nodes: Union[None, Node]
    
def make_empty_stack():
    """
    Returns a new stack with size initialized to zero and
    nodes initialed to the empty list. 
    """
    return Stack(0, None)

def push(stack, element):
    """
    Add an element to the top of the stack. The stack state changes.
    """
    stack.nodes = Node(element, stack.nodes)
    stack.size = stack.size + 1

    
def top(stack):
    """
    Return top element on stack.  Does not change stack.
    precondition: stack is not empty
    """
    if is_empty(stack):
        raise IndexError("top of empty stack") 
    return stack.nodes.value

def pop(stack):
    """
    Remove the top element in the stack and returns the removed value. 
    The stack state changes.
    precondition: stack is not empty
    """
    if is_empty(stack):
        raise IndexError("pop on empty stack") 
    popped = stack.nodes.value
    stack.nodes = stack.nodes.rest
    stack.size = stack.size - 1
    return popped
    
def is_empty(stack):
    """
    Is the stack empty?
    """
    return stack.nodes == None
    
def size(stack):                                         
    """
    Return the # of elements
    """  
    return stack.size

