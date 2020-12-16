"""
--- Part Two ---
Impressed, the Elves issue you a challenge: determine the 30000000th number spoken. For example, given the same starting numbers as above:

Given 0,3,6, the 30000000th number spoken is 175594.
Given 1,3,2, the 30000000th number spoken is 2578.
Given 2,1,3, the 30000000th number spoken is 3544142.
Given 1,2,3, the 30000000th number spoken is 261214.
Given 2,3,1, the 30000000th number spoken is 6895259.
Given 3,2,1, the 30000000th number spoken is 18.
Given 3,1,2, the 30000000th number spoken is 362.
Given your starting numbers, what will be the 30000000th number spoken?
"""
#04:38:24  10998

def play_game(numbers):
    last_occurences = {}
    for i in range(len(numbers)):
        last_occurences[numbers[i]] = [i + 1, i + 1]
    
    last_item = numbers[-1]
    index = last_occurences[last_item][0] + 1
    
    while True:
        current_item = last_occurences[last_item][1] - last_occurences[last_item][0]

        if current_item in last_occurences:
            if last_occurences[current_item][0] == last_occurences[current_item][1]:
                last_occurences[current_item][1] = index
            else:
                last_occurences[current_item][0] = last_occurences[current_item][1]
                last_occurences[current_item][1] = index
        else:
            last_occurences[current_item]  = [index, index]

        index += 1
        last_item = current_item

        if index == 30_000_000 + 1:
            print('30Mth number is:', current_item)

            return


input = [0, 13, 1, 8, 6, 15]
play_game(input)