#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt", "r") as file: 
    data = [int(x) for x in file.read().strip().split("\n")]
    
def sumcheck(target, numbers):
    """
    Checks the target number is the sum of any two distinct
    values in the numbers array
    
    Parameters
    ----------
    target : int
        the target value
    numbers : list
        list of numbers
    """
    for this in numbers:
        for that in numbers:
            if this == that:
                continue
            if this + that == target: 
                return True
    return False

assert sumcheck(3, [1,2,3]) == True
assert sumcheck(5, [3,1,5]) == False

def run(crypt, size=25):
    """
    Finds the number in the list of numbers (the crypt)
    which is not the sum of two of the previous 25 (size)
    numbers

    Parameters
    ----------
    crypt : list
        list of strictly positive numbers.
    size : int, optional
        Size of the preamble. The default is 25.
    """
    for i in range(len(crypt)):
        if i < size: 
            continue
        if sumcheck(crypt[i], crypt[i-size:i]) is False: 
            return crypt[i], i
    raise ValueError("Could not find solution")

print(run(data, 25))
#20874512, 537

def crack(crypt, target=20874512):
    """
    Finds a contiguous set of numbers in the input crypt which 
    sums to the target value, and returns the sum of the smallest
    and largest value

    Parameters
    ----------
    crypt : list
        list of numbers.
    target : int, optional
        target value. The default is 20874512.
    """
    for i in range(0, len(crypt)-1):
        for j in range(i+1, len(crypt)):
            #if the sum exceeds the target, no need to go further
            #given that each additional number will increase the total
            if sum(crypt[i:j]) > target: 
                break
            
            if sum(crypt[i:j]) == target: 
                return i, j, min(crypt[i:j]) + max(crypt[i:j])
            
    raise RuntimeError("Unable to crack crypt")
    
print(crack(data))
#(424, 441, 3012420)
