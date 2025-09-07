#!/usr/bin/env python3

def can_make_target(numbers, target, current_value=None, index=0, use_concat=False):
    """
    Recursively tries all combinations of +, *, and || operators between numbers
    to see if we can reach the target value.
    """
    if current_value is None:
        current_value = numbers[0]
        index = 1
    
    # Base case: processed all numbers
    if index == len(numbers):
        return current_value == target
    
    # Early pruning: if current value already exceeds target, no point continuing
    # (concatenation can make values even larger, so this still applies)
    if current_value > target:
        return False
    
    next_number = numbers[index]
    
    # Try addition
    if can_make_target(numbers, target, current_value + next_number, index + 1, use_concat):
        return True
    
    # Try multiplication
    if can_make_target(numbers, target, current_value * next_number, index + 1, use_concat):
        return True
    
    # Try concatenation (only in part 2)
    if use_concat:
        # Concatenate: convert both to string, join, convert back to int
        concat_value = int(str(current_value) + str(next_number))
        if can_make_target(numbers, target, concat_value, index + 1, use_concat):
            return True
    
    return False

def parse_line(line):
    """Parse a line like '781114: 614 6 2 2 2 53' into target and numbers list"""
    target_str, numbers_str = line.split(': ')
    target = int(target_str)
    numbers = [int(x) for x in numbers_str.split()]
    return target, numbers

def solve_part1(input_data):
    """
    Find equations that can be made valid by inserting + or * operators.
    Return sum of their target values.
    """
    lines = input_data.strip().split('\n')
    total = 0
    
    for line in lines:
        target, numbers = parse_line(line)
        if can_make_target(numbers, target, use_concat=False):
            total += target
    
    return total

def solve_part2(input_data):
    """
    Find equations that can be made valid by inserting +, *, or || operators.
    Return sum of their target values.
    """
    lines = input_data.strip().split('\n')
    total = 0
    
    for line in lines:
        target, numbers = parse_line(line)
        if can_make_target(numbers, target, use_concat=True):
            total += target
    
    return total

def main():
    # Test data from problem description
    test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    
    print("Test data:")
    print(f"Part 1: {solve_part1(test_data)}")
    print(f"Part 2: {solve_part2(test_data)}")
    print()
    
    # Real data
    with open('input.txt', 'r') as f:
        input_data = f.read()
    
    print("Real data:")
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")

if __name__ == "__main__":
    main()