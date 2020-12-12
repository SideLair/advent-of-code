"""
--- Part Two ---
Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

For example, using the same instructions as above:

F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?
"""
#01:55:49   6243 

def move(instructions):
    moves = {'E': 1, 'W': -1, 'N': 1, 'S': -1, 'R': 1, 'L': -1}
    sides = 'ESWN'
    current_direction = 'E'
    current_coords = (0, 0)
    current_waypoint_offset = (10, 1)
    current_waypoint_coords = (
        current_coords[0] + current_waypoint_offset[0], current_coords[1] + current_waypoint_offset[1])

    for instruction in instructions:
        if instruction[0] == 'F':
            koef = instruction[1]
            current_coords = (current_coords[0] + current_waypoint_offset[0]
                              * koef, current_coords[1] + current_waypoint_offset[1] * koef)

        if instruction[0] in 'EW':
            current_waypoint_offset = (
                current_waypoint_offset[0] + instruction[1] * moves[instruction[0]], current_waypoint_offset[1])
        elif instruction[0] in 'NS':
            current_waypoint_offset = (
                current_waypoint_offset[0], current_waypoint_offset[1] + instruction[1] * moves[instruction[0]])

        if instruction[0] in 'RL':
            rotations = [
                current_waypoint_offset,
                (current_waypoint_offset[1], - current_waypoint_offset[0]),
                (- current_waypoint_offset[0], - current_waypoint_offset[1]),
                (- current_waypoint_offset[1], current_waypoint_offset[0]),
            ]

            rotation = int((instruction[1] / 90) % 4)
            new_index = (sides.index(current_direction) + rotation * moves[instruction[0]]) % 4
            current_waypoint_offset = rotations[new_index]

        current_waypoint_coords = (current_coords[0] + current_waypoint_offset[0], current_coords[1] + current_waypoint_offset[1])

    print('Manhattan distance of {} is {}'.format(current_coords, abs(current_coords[0]) + abs(current_coords[1])))


file = open('input.txt', 'r')
instructions = [(line.strip('\n')[0], int(line.strip('\n')[1:]))
                for line in file]

print(instructions)
move(instructions)
