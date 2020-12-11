"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

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
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

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
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
"""
#02:55:03  10065
    
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


def get_adjacent_seats(central_seat, chair_list):                                                   #TODO remove central seat from adjacent seats
    rows = [n for n in range(central_seat[0] - 1, central_seat[0] + 1 + 1)]
    cols = [n for n in range(central_seat[1] - 1, central_seat[1] + 1 + 1)]
    surrounds = [n  for n in product(rows, cols) if (n in chair_list and n != central_seat)]

    return surrounds



def neighbour_count(seat, chair_list):                                                        #get adjacent seats and count occupied
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
        if chair_list[position] == 'L' and neighbour_count(position, chair_list) == 0:
            copy_chair_list[position] = '#'
        elif chair_list[position] == '#' and neighbour_count(position, chair_list) >= 4:
            copy_chair_list[position] = 'L'

    if chair_list == copy_chair_list:
        print('Count of #:',sum(value == '#' for value in copy_chair_list.values()))
        return None
    #print(copy_chair_list)
    return copy_chair_list


file = open('input.txt', 'r')
chair_plan = [line.strip('\n') for line in file]
chair_list = coords(chair_plan)
#print(chair_list)
while True:
    chair_list = final_occupation(chair_list)
    if chair_list == None:
        break
    