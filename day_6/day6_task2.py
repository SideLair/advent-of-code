"""
--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""
#01:09:33   9007
   
def common_answers(answers):
    char_count = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        ans_count = 0

        for answer in answers:
            if letter in answer:
                ans_count += 1
            else:
                continue

        if ans_count == len(answers):
            if letter not in char_count:
                char_count[letter] = 1
            else:
                char_count[letter] += 1
    return len(char_count)



def sum_of_counts(results):
    sum_counts = 0
    group_results = []
    for result in results:
        if result == '':
            sum_counts += common_answers(group_results)
            group_results = []
        else:
            group_results.append(result)

    sum_counts += common_answers(group_results)
    group_results = []
    
    return sum_counts

def amount_unique_chars(phrase):
    char_count = {}
    for i in range(0, len(phrase)):
        if phrase[i] not in char_count:
            char_count[phrase[i]] = 1
        else:
            char_count[phrase[i]] += 1
    return len(char_count)


file = open('input.txt', 'r')
results = [line.strip('\n') for line in file]

print('Sum of counts:', sum_of_counts(results))