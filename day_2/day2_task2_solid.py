"""
--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

import re

def is_valid(policy):
    match = re.match(r'([0-9]+)\-([0-9]+)\ ([a-z]):\ ([a-z]+$)', policy)
    position1 = int(match.group(1))
    position2 = int(match.group(2))
    password = match.group(4)
    char = match.group(3)

    return (password[position1 - 1] == char) != (password[position2 - 1] == char)


def check_policies(policy_list):
    counter = 0

    for policy in policy_list:
        if is_valid(policy):
            counter += 1

    return counter


file = open('input.txt', 'r')
passwords = [line.rstrip('\n') for line in file]

print('Valid passwords:', check_policies(passwords))