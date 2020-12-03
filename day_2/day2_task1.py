"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

def parse_policy(policy):
    occurences = policy[:policy.find(' ')]
    min = int(occurences[:occurences.find('-')])
    max = int(occurences[occurences.find('-') + 1:])

    letter = policy[policy.find(occurences) + len(occurences) + 1:policy.find(':')]
    password = policy[policy.find(letter) + len(letter) + 2:]
    
    return (min, max, letter, password)

def validate_policy(policy):
    min, max, letter, pswd = parse_policy(policy)

    return min <= pswd.count(letter) and pswd.count(letter) <= max

def check_policies(policy_list):
    counter = 0
    for policy in policy_list:
        if validate_policy(policy):
            counter += 1

    return counter

file = open('input.txt', 'r')
passwords = [line.rstrip('\n') for line in file]


print('Valid passwords:', check_policies(passwords), len(passwords))