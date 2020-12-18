"""
--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?
"""
#02:48:13   5355

import re


def is_in_range(number, rule):
    return rule[0] <= int(number) <= rule[1] or rule[2] <= int(number) <= rule[3]


def clean_rules(rules, column):
    for rule in rules:
        if column in rules[rule][4]:
            rules[rule][4].remove(column)


def find_invalid(tickets, rules):
    for number in tickets:
        is_invalid = True

        for rule in rules:
            if is_in_range(number, rules[rule]):
                is_invalid = False
                break
        
        if is_invalid:
            return number
    
    return 0


def get_result(ticket_rules, my_ticket):
    result = 1
    for i in range(len(my_ticket)):
        if 'departure' in ticket_rules[i]:
            result *= my_ticket[i]

    print('Departure items multiplied:', result)

rule = r'^(\w+\s?\w*): (\d+)-(\d+) or (\d+)-(\d+)$'

file = open('input.txt', 'r')
data = [line.strip('\n') for line in file]

rules = {}
nearby_tickets = []
rules_ticket = ['x' for _ in range(20)]
potencial_rules_ticket = ['x' for _ in range(20)]

#parsing
for row in data:
    r = re.match(rule, row)
    if r != None:
        rules[r.group(1)] = (int(r.group(2)), int(r.group(3)), int(r.group(4)), int(r.group(5)), set())
    elif 'your ticket' in row:
        my_ticket = [int(n) for n in data[data.index('your ticket:') + 1].split(',')]
    elif row not in 'nearby tickets:':
        nearby_ticket = [int(n) for n in row.split(',')]
        nearby_tickets.append(nearby_ticket)

#ticket validation and creating pack of valid tickets
error_rate = 0
valid_tickets = [my_ticket]
for ticket in nearby_tickets:
    result = find_invalid(ticket, rules)
    error_rate += result
    if result == 0:
        valid_tickets.append(ticket)

#for every uncovered column try to use every rule. Ticket by ticket.
while len(rules) > 1:
    for column in range(len(rules_ticket)):
        potencial_rules = []
        if rules_ticket[column] == 'x':
            for rule in rules:
                is_valid = True
                for valid_ticket in valid_tickets:
                    if not is_in_range(valid_ticket[column], rules[rule]):
                        is_valid = False
                        break
                if is_valid:
                    potencial_rules.append(rule)

        #if there is only one potencial rule, simply assign it to column, in other ways mark potencial rules by the column
        if len(potencial_rules) == 1:
            rules_ticket[column] = potencial_rules[0]
            potencial_rules_ticket[column] = potencial_rules[0]
            clean_rules(rules, column)
            del rules[potencial_rules[0]]
        else:
            potencial_rules_ticket[column] = potencial_rules if potencial_rules != [] else rules_ticket[column]
            #add record of column to every touched rule
            for potencial_rule in potencial_rules:
                rules[potencial_rule][4].add(column)

    #check if there is a rule with only 1 potencial column
    for rule in rules:
        if len(rules[rule][4]) == 1:
            rules_ticket[list(rules[rule][4])[0]] = rule
            clean_rules(rules, list(rules[rule][4])[0])
            del rules[rule]
            break

get_result(rules_ticket, my_ticket)