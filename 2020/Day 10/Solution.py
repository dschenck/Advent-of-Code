#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import functools

with open("input.txt", "r") as file: 
    data = [int(x) for x in file.read().strip().split("\n")]
   
# Part 1

def run(data):
    """
    Computes the number of 1-jolt differences multiplied 
    by the number of 3-jolt differences from the data, 
    adding the charging outlet (0 jolts) and the device
    (max of data + 3)

    Parameters
    ----------
    data : list
        list of jols.
    """
    data  = sorted([0, max(data) + 3] + data)
    diffs = collections.defaultdict(lambda: 0)
    
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        assert 0 <= diff <= 3
        diffs[diff]  += 1
    
    return diffs[1] * diffs[3]

print(run(data)) #2040
   
# Part 2

def split(numbers): 
    """
    Chunks the data in small batches
    A batch can be created if its bounds cannot be 
    removed from the larger sequence
    """
    chunks = []
    while True: 
        for i in range(1, len(numbers) - 1): 
            if (numbers[i+1] - numbers[i-1]) > 3: 
                chunks.append(numbers[0:i+1])
                numbers = numbers[i:]
                break
        else: 
            chunks.append(numbers)
            return chunks
        
def compute(numbers, permutations=None):
    """
    Compute the number of different permutations
    conditional on having no more than 3 difference
    between two consecutive numbers
    """
    if permutations is None: 
        permutations = set()
        
    permutations.add(tuple(numbers))
    
    for i in range(1, len(numbers)-1): 
        if (numbers[i+1] - numbers[i-1]) > 3: 
            continue
        compute(numbers[0:i]+numbers[i+1:], permutations)
    return len(permutations)

def solve(data): 
    """
    Finds the number of different permutations
    """
    numbers = sorted([0, max(data) + 3] + data)
    return functools.reduce(lambda acc, curr: acc * curr, 
                            [compute(chunk) for chunk in split(numbers)])

print(solve(data)) #28346956187648
            