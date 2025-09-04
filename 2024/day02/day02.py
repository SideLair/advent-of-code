#!/usr/bin/env python3

def solve_part1(input_data):
    """Check if reports are safe based on the rules."""
    safe_count = 0
    
    for line in input_data.strip().split('\n'):
        if line and not line.startswith('#'):
            levels = list(map(int, line.split()))
            if is_safe(levels):
                safe_count += 1
    
    return safe_count

def solve_part2(input_data):
    """Check if reports are safe with Problem Dampener - can remove one level."""
    safe_count = 0
    
    for line in input_data.strip().split('\n'):
        if line and not line.startswith('#'):
            levels = list(map(int, line.split()))
            
            # Nejdřív zkus bez odstraňování
            if is_safe(levels):
                safe_count += 1
                continue
            
            # Zkus odstranit každý level postupně
            found_safe = False
            for i in range(len(levels)):
                modified_levels = levels[:i] + levels[i+1:]
                if is_safe(modified_levels):
                    found_safe = True
                    break
            
            if found_safe:
                safe_count += 1
    
    return safe_count

def is_safe(levels):
    """Check if a report is safe based on the rules."""
    if len(levels) < 2:
        return True
    
    # Check if increasing or decreasing
    increasing = levels[1] > levels[0]
    
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i-1]
        
        # Check if direction is consistent
        if increasing and diff <= 0:
            return False
        if not increasing and diff >= 0:
            return False
        
        # Check if difference is within range [1, 3]
        abs_diff = abs(diff)
        if abs_diff < 1 or abs_diff > 3:
            return False
    
    return True

def main():
    # Test data
    test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
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