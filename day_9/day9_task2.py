"""
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.
"""
#01:05:01   7844

def is_valid(preamble, number):

    for i in range(0, len(preamble)):
        for j in range (i + 1, len(preamble)):
            if i != j and preamble[i] + preamble[j] == number:
                return True

    return False


def find_invalid_number(numbers, preamble_length):
    
    for i in range(preamble_length, len(numbers)):
        if not is_valid(numbers[i - preamble_length:i], numbers[i]):
            find_weakness(numbers[:i], numbers[i])
            return numbers[i]

    print('No invalid number there :(')


def find_weakness(numbers, number):
    sum = 0
    weakness_nums = []

    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):    
            sum += numbers[j]
            weakness_nums.append(numbers[j])

            if sum == number:
                print('Encryption weakness:', min(weakness_nums) + max(weakness_nums))
            if sum > number:
                break

        sum = 0
        weakness_nums = []


file = open('input.txt', 'r')
numbers = [int(line.strip('\n')) for line in file]

print('Invalid number is:', find_invalid_number(numbers, 25))