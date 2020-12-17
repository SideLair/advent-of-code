"""
--- Part Two ---
For some reason, your simulated results don't match what the experimental energy source engineers expected. Apparently, the pocket dimension actually has four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (x,y,z,w), there exists a single cube (really, a hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3, the cube at x=0,y=2,z=3,w=4, and so on.

The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules for cycle updating still apply: during each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even though the pocket dimension is 4-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1x1 region of the 4-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z and w coordinate:

Before any cycles:

z=0, w=0
.#.
..#
###


After 1 cycle:

z=-1, w=-1
#..
..#
.#.

z=0, w=-1
#..
..#
.#.

z=1, w=-1
#..
..#
.#.

z=-1, w=0
#..
..#
.#.

z=0, w=0
#.#
.##
.#.

z=1, w=0
#..
..#
.#.

z=-1, w=1
#..
..#
.#.

z=0, w=1
#..
..#
.#.

z=1, w=1
#..
..#
.#.


After 2 cycles:

z=-2, w=-2
.....
.....
..#..
.....
.....

z=-1, w=-2
.....
.....
.....
.....
.....

z=0, w=-2
###..
##.##
#...#
.#..#
.###.

z=1, w=-2
.....
.....
.....
.....
.....

z=2, w=-2
.....
.....
..#..
.....
.....

z=-2, w=-1
.....
.....
.....
.....
.....

z=-1, w=-1
.....
.....
.....
.....
.....

z=0, w=-1
.....
.....
.....
.....
.....

z=1, w=-1
.....
.....
.....
.....
.....

z=2, w=-1
.....
.....
.....
.....
.....

z=-2, w=0
###..
##.##
#...#
.#..#
.###.

z=-1, w=0
.....
.....
.....
.....
.....

z=0, w=0
.....
.....
.....
.....
.....

z=1, w=0
.....
.....
.....
.....
.....

z=2, w=0
###..
##.##
#...#
.#..#
.###.

z=-2, w=1
.....
.....
.....
.....
.....

z=-1, w=1
.....
.....
.....
.....
.....

z=0, w=1
.....
.....
.....
.....
.....

z=1, w=1
.....
.....
.....
.....
.....

z=2, w=1
.....
.....
.....
.....
.....

z=-2, w=2
.....
.....
..#..
.....
.....

z=-1, w=2
.....
.....
.....
.....
.....

z=0, w=2
###..
##.##
#...#
.#..#
.###.

z=1, w=2
.....
.....
.....
.....
.....

z=2, w=2
.....
.....
..#..
.....
.....
After the full six-cycle boot process completes, 848 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles in a 4-dimensional space. How many cubes are left in the active state after the sixth cycle?
"""
#14:26:16  13986

#active and (2 or 3 active neighs) -> active
#inactive and 3 active neighs -> active

import copy

def active_state_count(hypercube):
    count = 0
    for z_cube in hypercube:     
        for y_slice in z_cube:
            for x_row in y_slice:
                for w_item in x_row:
                    if w_item == '#':
                        count += 1
    
    return count


def show(hypercube):
    for z_cube in hypercube:     
        for y_slice in z_cube:
            for x_row in y_slice:
                for w_item in x_row:
                    print(w_item, end='')

                print()
        
            print()

        print()


def get_neigbors(hypercube, coords):
    
    result = []
    for z in range(coords[3] - 1, coords[3] + 2):
        for y in range(coords[2] - 1, coords[2] + 2):
            for x in range(coords[1] - 1, coords[1] + 2):
                for w in range(coords[0] - 1, coords[0] + 2):
                    if (w, x, y, z) != coords:
                        try:
                            #not very nice but...
                            tmp =  hypercube[z][y][x][w]
                            result.append((w, x, y, z))
                        except:
                            pass

    return result


def get_active_neigbors(hypercube, neigbors):
    count = 0
    for neigbor in neigbors:
        if hypercube[neigbor[3]][neigbor[2]][neigbor[1]][neigbor[0]] == '#':
            count += 1

    return count


def apply_rules(hypercube):
    new_cube = copy.deepcopy(hypercube)

    for z in range(len(hypercube)):     
        for y in range(len(hypercube[0])):
            for x in range(len(hypercube[0][0])):
                for w in range(len(hypercube[0][0][0])):
                    active = get_active_neigbors(hypercube, get_neigbors(hypercube, (w, x, y, z)))
                    try:
                        #not very nice but...
                        if hypercube[z][y][x][w] == '.' and active == 3:
                            new_cube[z][y][x][w] = '#'
                        elif hypercube[z][y][x][w] == '#' and 2 <= active <= 3:
                            new_cube[z][y][x][w] = '#'
                        else:
                            new_cube[z][y][x][w] = '.'
                    except:
                        pass

    return new_cube



def expand(hypercube):
    #priprava pro prvni a posledni radek
    new_row = list((len(hypercube[0][0]) ) * '.')
    new_slice = [copy.deepcopy(new_row) for row in hypercube[0][0]]
    new_cube = [copy.deepcopy(new_slice) for row in hypercube[0][0][0]]

    hypercube.insert(0, copy.deepcopy(new_cube))
    hypercube.append(copy.deepcopy(new_cube))

    for z_cube in hypercube:
        z_cube.insert(0, copy.deepcopy(new_slice))
        z_cube.append(copy.deepcopy(new_slice))
        
        for y_slice in z_cube:
            y_slice.insert(0, list(new_row))
            y_slice.append(list(new_row))

            for x_row in y_slice:
                x_row.insert(0, '.')
                x_row.append('.')

    hypercube = apply_rules(hypercube)
    
    return hypercube
            


file = open('input.txt', 'r')
data = list([list(line.strip('\n')) for line in file])
cube = [[data]]

for i in range(6):
    cube = expand(cube)

print('Cubes in active state:', active_state_count(cube))
