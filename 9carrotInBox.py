"""Carrot in a Box, by Al Sweigart al@inventwithpython.com
A silly bluffing game between two human players. Based on the game
from the show 8 Out of 10 Cats.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, beginner, game, two-player"""

import random

print('''Carrot in a Box, by Al Sweigart al@inwentwithpython.com

This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is very simple and silly game.

The first player looks into their box (the second player must close 
their eyes during this) The first player then says "There is a carrot 
in my box" or "There is not a carrot in my box". The second player then
 gets to decide if they want to swap boxes or not.
 ''')
input('Press Enter to begin...')

p1_name = input('Human player 1, enter your name: ')
p2_name = input('Human player 2, enter your name: ')
player_names = p1_name[:11].center(11) + p2_name[:11].center(11)

print('''HERE ARE TWO BOXES:
  __________
 /         /| 
+---------+ | 
|   BOX   | |
|   RED   | /
+---------+/

''')
