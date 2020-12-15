"""

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