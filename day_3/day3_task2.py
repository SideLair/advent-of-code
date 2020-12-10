"""
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""
#06:20:22  28095 

def mark_place(item):
    #print(item)
    return 'O' if item == '.' else 'X'

def ride_thru(country, step_col, step_line):
    current_column = 1
    trees = 0

    for current_line in range(0, len(country), step_line):
        
        if current_column > 31:
            current_column -= 31

        if country[current_line][current_column - 1] == '#':
            trees += 1
        print(country[current_line][:current_column - 1] + mark_place(country[current_line][current_column - 1]) +  country[current_line][current_column:], trees)

        current_column += step_col

    return trees

file = open('input.txt', 'r')
country = [line.rstrip('\n') for line in file]

ride11 = ride_thru(country, 1, 1)
ride31 = ride_thru(country, 3, 1)
ride51 = ride_thru(country, 5, 1)
ride71 = ride_thru(country, 7, 1)
ride12 = ride_thru(country, 1, 2)
print(ride11, ride31, ride51, ride71, ride12, ' = ', ride11 * ride31 * ride51 * ride71 * ride12)
