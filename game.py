#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

grid = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
size = 4

def number_length(num):
    return len(str(num))

def render(grid):
    max_number_length = number_length(max(grid))
    border_size = max_number_length + 2
    border = ' ' + ('-' * border_size + ' ') * size

    print(border)
    for (index, ceil) in enumerate(grid):

        space_count = max_number_length - number_length(ceil) + 1
        spaces = ' ' * space_count
        
        if ceil == 0: 
            ceil = ' '

        if (index + 1) % size == 0:
            print(f'|{spaces}{ceil} |', end='')
            print('\n', end='')
            print(border)
        else:
            print(f'|{spaces}{ceil} ', end='')

def get_zero_index(grid):
    return grid.index(0)

def swap(grid, index_a, index_b):
    tmp = grid[index_a]
    grid[index_a] = grid[index_b];
    grid[index_b] = tmp

def move(grid ,cell):
    zero = get_zero_index(grid)
    if (cell < len(grid)) & (cell >= 0):
        if zero != cell:
            if (abs(zero - cell) == 1) | (abs(zero - cell) == size):
                swap(grid, cell, zero)

def event_handler():
    commandString = input('next step: ')

    def up():
        move(grid, get_zero_index(grid) + size)
    
    def down():
        move(grid, get_zero_index(grid) - size)

    def left():
        move(grid, get_zero_index(grid) + 1)
    
    def right():
        move(grid, get_zero_index(grid) - 1)

    def quite():
        os.sys.exit()

    def wrong_command():
        print('wrong command')

    commands = {'w': up, 's': down, 'a': left, 'd': right, 'q': quit}
    command = commands.get(commandString, wrong_command)
    command()

def game_loop():
    while True:
        os.system('clear')
        render(grid)
        event_handler()
        
game_loop()