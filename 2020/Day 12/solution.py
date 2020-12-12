#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt", "r") as file: 
    data = file.read().strip().split("\n")
    
def move(position, instruction):
    """
    N means to move north by the given value.
    S means to move south by the given value.
    E means to move east by the given value.
    W means to move west by the given value.
    L means to turn left the given number of degrees.
    R means to turn right the given number of degrees.
    F means to move forward by the given value in the direction the ship is currently facing.
    """
    x, y, direction = position
    
    if instruction[0] == "N": 
        return (x, y + int(instruction[1:]), direction)
    if instruction[0] == "S":
        return (x, y - int(instruction[1:]), direction)
    if instruction[0] == "E":
        return (x + int(instruction[1:]), y, direction)
    if instruction[0] == "W":
        return (x - int(instruction[1:]), y, direction)
    
    if instruction[0] == "F": 
        return move((x, y, direction), f"{direction}{instruction[1:]}")
    
    if instruction[0] == "R":
        angle = int(instruction[1:]) // 90
        return (x, y, "NESW"[("NESW".index(direction) + angle) % 4])
    
    if instruction[0] == "L": 
        angle = int(instruction[1:])
        return move((x, y, direction), f"R{360-angle}")
    
    raise ValueError(f"Unknown instruction {instruction}")
    
assert move((0,0,"E"), "N10") == (0, 10, "E")
assert move((0,0,"W"), "N10") == (0, 10, "W")
assert move((0,0,"E"), "S10") == (0, -10, "E")
assert move((0,0,"E"), "E10") == (10, 0, "E")
assert move((0,0,"W"), "E10") == (10, 0, "W")
assert move((0,0,"E"), "F10") == (10, 0, "E")
assert move((0,0,"N"), "F10") == (0, 10, "N")
assert move((0,0,"E"), "R90") == (0, 0, "S")
assert move((0,0,"E"), "R270") == (0,0,"N")
assert move((0,0,"E"), "L90") == (0, 0, "N")

def run(data):
    position = (0,0,"E")
    for instruction in data: 
        position = move(position, instruction)
    return abs(position[0]) + abs(position[1]), position

print("Part 1", run(data))

def waymove(position, waypoint, instruction):
    """
    N means to move the waypoint north by the given value.
    S means to move the waypoint south by the given value.
    E means to move the waypoint east by the given value.
    W means to move the waypoint west by the given value.
    L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    F means to move forward to the waypoint a number of times equal to the given value.
    """
    x, y, direction = position
    wx, wy = waypoint
    
    if instruction[0] == "N": 
        return position, (wx, wy + int(instruction[1:]))
    if instruction[0] == "S":
        return position, (wx, wy - int(instruction[1:]))
    if instruction[0] == "E":
        return position, (wx + int(instruction[1:]), wy)
    if instruction[0] == "W":
        return position, (wx - int(instruction[1:]), wy)
    
    if instruction[0] == "F":
        dist = int(instruction[1:])
        return (x + dist * wx, y + dist * wy, direction), (wx, wy)
    
    if instruction[0] == "R": 
        angle = int(instruction[1:])
        if angle == 90: 
            return position, (wy, -wx)
        if angle == 180: 
            return position, (-wx, -wy)
        if angle == 270: 
            return position, (-wy, wx)
    
    if instruction[0] == "L":
        angle = int(instruction[1:])
        return waymove(position, waypoint, f"R{360-angle}")
    
def run(data):
    position, waypoint = (0,0,"E"), (10, 1)
    for instruction in data: 
        position, waypoint = waymove(position, waypoint, instruction)
    return abs(position[0]) + abs(position[1]), position, waypoint

print("Part 2", run(data))
