#!/usr/bin/env python3

def solve_part1(input_data):
    content = input_data.strip()
    parts = content.split('\n\n')
    rules_section = parts[0]
    pages_section = parts[1]
    
    rules = []
    for line in rules_section.split('\n'):
        x, y = map(int, line.split('|'))
        rules.append((x, y))
    
    pages = []
    for line in pages_section.split('\n'):
        page_list = list(map(int, line.split(',')))
        pages.append(page_list)
    
    def is_valid_order(page_list, rules):
        for x, y in rules:
            if x in page_list and y in page_list:
                x_pos = page_list.index(x)
                y_pos = page_list.index(y)
                if x_pos > y_pos:
                    return False
        return True
    
    valid_pages = [page_list for page_list in pages if is_valid_order(page_list, rules)]
    middle_sum = sum(page_list[len(page_list) // 2] for page_list in valid_pages)
    
    return middle_sum

def solve_part2(input_data):
    import functools
    
    content = input_data.strip()
    parts = content.split('\n\n')
    rules_section = parts[0]
    pages_section = parts[1]
    
    rules = []
    for line in rules_section.split('\n'):
        x, y = map(int, line.split('|'))
        rules.append((x, y))
    
    pages = []
    for line in pages_section.split('\n'):
        page_list = list(map(int, line.split(',')))
        pages.append(page_list)
    
    def is_valid_order(page_list, rules):
        for x, y in rules:
            if x in page_list and y in page_list:
                x_pos = page_list.index(x)
                y_pos = page_list.index(y)
                if x_pos > y_pos:
                    return False
        return True
    
    # Create rule set for O(1) lookups
    rule_set = set(rules)
    
    def compare(a, b):
        if (a, b) in rule_set:
            return -1  # a should come before b
        elif (b, a) in rule_set:
            return 1   # b should come before a
        else:
            return 0   # no constraint between a and b
    
    # Find invalid pages and fix them
    invalid_pages = [page_list for page_list in pages if not is_valid_order(page_list, rules)]
    
    fixed_pages = []
    for page_list in invalid_pages:
        # Sort using custom comparator
        sorted_pages = sorted(page_list, key=functools.cmp_to_key(compare))
        fixed_pages.append(sorted_pages)
    
    # Sum middle elements
    middle_sum = sum(page_list[len(page_list) // 2] for page_list in fixed_pages)
    
    return middle_sum

def main():
    # Test data
    with open('test.txt', 'r') as f:
        test_data = f.read()
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