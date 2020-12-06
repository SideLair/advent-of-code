"""
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""

def give_result(numbers):
    max_index = len(numbers) - 1

    for min_index in range(0, len(numbers)):
        while max_index > min_index:
            print(numbers[min_index] + numbers[max_index], min_index, max_index, numbers[min_index], numbers[max_index])

            if numbers[min_index] + numbers[max_index] == 2020:
                print('RESULT', numbers[min_index] * numbers[max_index])
                return
            elif numbers[min_index] + numbers[max_index] < 2020:
                break
            
            max_index -= 1


file_expense_report = open('AoC_201201_1_input.txt', 'r')
expense_report = [int(line.rstrip('\n')) for line in file_expense_report]
expense_report_sorted = sorted(expense_report)

print(expense_report_sorted)
give_result(expense_report_sorted)
