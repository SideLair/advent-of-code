"""
--- Part Two ---
You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
Here are the other examples from above:

1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
What do you get if you add up the results of evaluating the homework problems using these new rules?
"""
#04:25:53   6450 

import re

def solve_parenthesis(example):
    while True:
        regex = re.match(r'([\d\+\*()]*)(\([\d\+\*]+\))([\d\+\*()]*)', example)
        
        if regex != None:
            #without parenthesis, also replacing only last occurence :)
            example = example[:regex.start(2)] + example[regex.start(2):].replace(regex.group(2), str(solve_parenthesis(regex.group(2)[1:-1])))
        else:
            break

    return solve_additions(example)


def solve_additions(example):
    while True:
        regex = re.match(r'.*(^|[*+(])(\d+\+\d+)([)*+]|$).*', example)
        if regex != None:
            example = example[:regex.start(2)] + example[regex.start(2):].replace(regex.group(2), str(solve(regex.group(2))))
        else:
            break

    return solve(example)  


def solve(example):
    result = None
    i = 0

    number = ''
    operator = ''

    while i < len(example):
        if result == None and example[i] in '+*':
            result = int(number)
            number = ''
            operator = example[i]
        elif example[i] in '+*' and operator != '':
            if operator == '+':
                result += int(number)
            elif operator == '*':
                result *= int(number)
            
            operator = example[i]
            number = ''
        else:
            number += example[i]

        i += 1

    if operator == '+':
        result += int(number)
    elif operator == '*':
        result *= int(number)
    else:
        result = int(number)
      
    return result


file = open('input.txt', 'r')
examples = [line.strip('\n').replace(' ', '') for line in file]

print('Sum of results:', sum([solve_parenthesis(example) for example in examples]))
