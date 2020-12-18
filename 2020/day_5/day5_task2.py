"""
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
"""
#01:34:53   9106

def switch_to_seat_ID(phrase):
    phrase = phrase.replace('R','1').replace('L','0').replace('B','1').replace('F','0')
    row = int(phrase[:-3], 2)
    col = int(phrase[-3:], 2)
    #print(row, col)
    return row * 8 + col


def highest_seat_ID(seats):
    highest_seat_ID = 0
    seat_IDs = []
    for seat in seats:
        seat_IDs.append(switch_to_seat_ID(seat))
        if seat_IDs[-1] > highest_seat_ID:
            highest_seat_ID = seat_IDs[-1]

    return highest_seat_ID, seat_IDs


def find_seat(seats):
    seat = seats[0] - 1
    for current_seat in seats:
        if seat + 1 == current_seat:
            seat = current_seat
        else:
            return current_seat - 1

file = open('input.txt', 'r')
seats = [line.strip('\n') for line in file]

print('Highest seat ID:', highest_seat_ID(seats)[0])

print(find_seat(sorted(highest_seat_ID(seats)[1])))