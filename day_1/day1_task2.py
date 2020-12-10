"""
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation.
They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""
#04:20:34  16809

def give_result(numbers):
    max_index = len(numbers) - 1

    for min_index in range(0, len(numbers)):
        mid_index = min_index + 1
        while max_index > mid_index:
            print(numbers[min_index] + numbers[mid_index] + numbers[max_index], min_index, mid_index, max_index, numbers[min_index], numbers[mid_index], numbers[max_index])

            while max_index > mid_index:
                if numbers[min_index] + numbers[mid_index] + numbers[max_index] == 2020:
                    print('RESULT', numbers[min_index] * numbers[mid_index] * numbers[max_index])
                    return
                elif numbers[min_index] + numbers[mid_index] + numbers[max_index] < 2020:
                    break
                
                mid_index += 1
            
            if numbers[min_index] + numbers[mid_index] + numbers[max_index] < 2020:
                break

            max_index -= 1
            mid_index = min_index + 1

file_expense_report = open('AoC_201201_1_input.txt', 'r')
expense_report = [int(line.rstrip('\n')) for line in file_expense_report]
expense_report_sorted = sorted(expense_report)

print(expense_report_sorted)
give_result(expense_report_sorted)
