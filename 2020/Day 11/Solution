#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt", "r") as file: 
    data = [list(line) for line in file.read().strip().split("\n")]

def get_adjacents(position, plan):
    """
    Returns the value of each immediate adjacent seat for a given
    position (x, y) in the plan
    """
    for x in [-1,0,+1]: 
        for y in [-1, 0, +1]: 
            if x == 0 and y == 0: 
                continue
            if (position[0] + x) < 0 or (position[0] + x) >= len(plan):
                continue
            if (position[1] + y) < 0 or (position[1] + y) >= len(plan[0]):
                continue 
            yield plan[position[0] + x][position[1] + y]
    return

def get_first_seat(position, direction, plan): 
    """
    Returns the first seat (available or free) from the 
    position (x, y) in the given direction (x, y).
    """
    x, y = position[0] + direction[0], position[1] + direction[1]
    while 0 <= x < len(plan) and 0 <= y < len(plan[0]): 
        if plan[x][y] in ["#","L"]: 
            return plan[x][y]
        x, y = x + direction[0], y + direction[1]
    return "wall"

def get_extended_adjacents(position, plan):
    """
    Returns a list of extended adjacent positions (x, y) for a given
    position (x, y) in the plan
    """
    for x in [-1,0,+1]: 
        for y in [-1, 0, +1]: 
            if x == 0 and y == 0: 
                continue
            yield get_first_seat(position, (x, y), plan)
    return

# Common to part 1 and part 2

def transform(plan, threshold, finder):
    """
    Applies the seating plan logic once and returns 
    the new seating plan
    
    - If a seat is empty (L) and there are no 
    occupied seats adjacent to it, the seat becomes occupied.
    - If a seat is occupied (#) and X (threshold) or more 
    seats adjacent to it are also occupied, the seat becomes empty.
    - Otherwise, the seat's state does not change
    
    Parameters
    ---------------
    plan : list 
        the seating plan
    threshold : int
        the number of occupied adjacent seats which 
        causes a seat to become vacant
    finder : callable
        function which yields the adjacent seats for a given position
    """
    copy = [row[:] for row in plan]
    
    for r in range(len(plan)):
        for c in range(len(plan[0])):
            
            #if the seat is empty (L) and there are no occupied seats adjacent to it, 
            #the seat becomes occupied.
            if plan[r][c] == "L" and sum(seat == "#" for seat in finder((r, c), plan)) == 0:
                copy[r][c] = "#"
                    
            #If a seat is occupied (#) and five or more seats adjacent to it are also occupied, 
            #the seat becomes empty.
            elif plan[r][c] == "#" and sum(seat == "#" for seat in finder((r, c), plan)) >= threshold: 
                copy[r][c] = "L"
                
    return copy

def flatten(plan):
    """
    Flattens a seating plan into a single string
    """
    return "".join(["".join(row) for row in plan])

def run(data, algorithm): 
    """
    Transforms the seating plan until no further changes 
    are possible
    
    Parameters
    ------------
    data : list
        seating plan
    algorithm : callable
        function which takes a seating plan and transforms it
    """
    prev, curr = None, flatten(data)
    
    while prev != curr: 
        data = algorithm(data)
        prev, curr = curr, flatten(data)
        
    return sum(x == "#" for x in flatten(data))


print("Part 1", run(data, lambda plan: transform(plan, 4, get_adjacents))) #2438
print("Part 2", run(data, lambda plan: transform(plan, 5, get_extended_adjacents))) #2174
    