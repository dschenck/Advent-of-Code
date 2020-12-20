#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt", "r") as file: 
    data = file.read().strip().split("\n")

import re
import functools
    
def evaluate(string, method="basic"):
    #if there are parentheses, evaluate inside and replace
    if re.search("\(.+\)", string):
        innergroup = re.search("\(([\d|\s|\+\*]+)\)", string).groups()[0]
        return evaluate(re.sub("\([\d|\s|\+\*]+\)", str(evaluate(innergroup, method)), string, count=1), method)
    
    #basic method: evaluate left to right
    if method == "basic":
        #no parentheses: evaluate left to right
        acc, op = None, None
        for i, token in enumerate(string.split(" ")): 
            if i == 0: 
                acc = int(token)
                continue
            if token in "*+":
                op = token
                continue
            acc = acc + int(token) if op == "+" else acc * int(token)
        return acc
    
    #advanced method: evaluate addition prior to product
    if method == "advanced":
        #if there are multiplication
        if "*" in string: 
            return functools.reduce(lambda acc, curr: acc * curr, 
                                    [evaluate(part, method) for part in string.split("*")])
            
        #if there are additions
        if "+" in string: 
            return functools.reduce(lambda acc, curr: acc + curr, 
                                    [evaluate(part, method) for part in string.split("+")])
        
        return int(string)

def run(data, method):
    return functools.reduce(lambda acc, curr: acc + evaluate(curr, method), data, 0)

print(run(data,"basic")) #18213007238947
print(run(data,"advanced")) #388966573054664