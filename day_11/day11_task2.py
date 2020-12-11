"""
--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............
The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?
"""
#03:48:09   8809
    
from itertools import product
from collections import Counter
import copy

def coords(chair_plan):
    chair_list = {}
    for row_index in range(0, len(chair_plan)):
        for col_index in range(0, len(chair_plan[0])):
            chair_list[(row_index, col_index)] = chair_plan[row_index][col_index]
    #print(chair_list)
    return chair_list


def print_plan(chair_plan):
    for row in chair_plan:
        print(row)


def get_adjacent_seats(central_seat, chair_list):                                                   
    rows = [n for n in range(central_seat[0] - 1, central_seat[0] + 1 + 1)]
    cols = [n for n in range(central_seat[1] - 1, central_seat[1] + 1 + 1)]
    surrounds = [n  for n in product(rows, cols) if (n in chair_list and n != central_seat)]

    return surrounds


def is_valid(seat, chair_list):
    return seat in chair_list


def get_visible_seats(central_seat, chair_list):
    """
    012
    3x4
    567
    """
    directions = {
        '0' : (-1, -1),
        '1' : (-1, 0),
        '2' : (-1, 1),
        '3' : (0, -1),
        '4' : (0, 1),
        '5' : (1, -1),
        '6' : (1, 0),
        '7' : (1, 1),
        }
    radius = 1
    perspective = '01234567'
    #print(perspective)  


    while True:
        for position in perspective:                #8 hladovych if tvl
            if position not in 'L#.':
                current_seat = (central_seat[0] + radius * directions[position][0], central_seat[1] + radius * directions[position][1])

                if is_valid(current_seat, chair_list):
                    if perspective[int(position)] == position and chair_list[current_seat] != '.':
                        perspective = perspective.replace(position, chair_list[current_seat])
                else:
                    perspective = perspective.replace(position, '.')
            
        if len(perspective) == perspective.count('L') + perspective.count('#') + perspective.count('.'):
            return perspective.count('#')
        else:
            radius += 1


def neighbour_count(seat, chair_list):                                                        
    neighbors = 0
    #print('neighbor_count(adjacent_seats(', get_adjacent_seats(seat, chair_list))
    for position in get_adjacent_seats(seat, chair_list):
        
        if chair_list[position] == '#':
            neighbors += 1
    #print('neighbor_count(', neighbors)
    return neighbors



def final_occupation(chair_list):
    #(row, col)

    copy_chair_list = copy.deepcopy(chair_list)
    
    for position in chair_list:
        #print('FKIN pos', position)
        if chair_list[position] == 'L' and get_visible_seats(position, chair_list) == 0:
            copy_chair_list[position] = '#'
        elif chair_list[position] == '#' and get_visible_seats(position, chair_list) >= 5:
            copy_chair_list[position] = 'L'

    if chair_list == copy_chair_list:
        print('Count of #:', sum(value == '#' for value in copy_chair_list.values()))
        return None
    #print(copy_chair_list)
    return copy_chair_list


file = open('input.txt', 'r')
chair_plan = [line.strip('\n') for line in file]
chair_list = coords(chair_plan)

while True:
    chair_list = final_occupation(chair_list)
    if chair_list == None:
        break

#print(chair_list)
    