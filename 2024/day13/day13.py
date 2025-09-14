#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 13: Claw Contraption

Find the minimum tokens needed to win prizes from claw machines.
Each machine has two buttons (A and B) that move the claw by specific amounts.
Button A costs 3 tokens, Button B costs 1 token.
Each button can be pressed at most 100 times.

Part 1: Find cheapest way to reach exact prize position for each machine.

Uses Cramer's rule to solve the system of linear equations:
a * ax + b * bx = px
a * ay + b * by = py

Where:
- a, b = number of times to press buttons A and B
- ax, ay = movement per press of button A
- bx, by = movement per press of button B  
- px, py = prize position
"""

import re


def parse_machines(data):
    """
    Parse input data into list of machine configurations.
    Each machine has button A, button B, and prize coordinates.
    """
    machines = []
    lines = data.strip().split('\n')
    
    i = 0
    while i < len(lines):
        if lines[i].startswith('Button A:'):
            # Parse Button A: X+94, Y+34
            match_a = re.search(r'X\+(\d+), Y\+(\d+)', lines[i])
            ax, ay = int(match_a.group(1)), int(match_a.group(2))
            
            # Parse Button B: X+22, Y+67
            match_b = re.search(r'X\+(\d+), Y\+(\d+)', lines[i+1])
            bx, by = int(match_b.group(1)), int(match_b.group(2))
            
            # Parse Prize: X=8400, Y=5400
            match_p = re.search(r'X=(\d+), Y=(\d+)', lines[i+2])
            px, py = int(match_p.group(1)), int(match_p.group(2))
            
            machines.append((ax, ay, bx, by, px, py))
            i += 4  # Skip to next machine (including empty line)
        else:
            i += 1
    
    return machines


def solve_machine(ax, ay, bx, by, px, py, max_presses=100):
    """
    Solve single machine using Cramer's rule.
    
    System of equations:
    a * ax + b * bx = px
    a * ay + b * by = py
    
    Returns (a, b) if valid solution exists, None otherwise.
    Valid solution: a and b are non-negative integers ≤ max_presses.
    """
    # Calculate determinant
    D = ax * by - ay * bx
    
    if D == 0:
        # No unique solution (parallel lines)
        return None
    
    # Apply Cramer's rule
    a_num = px * by - py * bx
    b_num = ax * py - ay * px
    
    # Check if solutions are integers
    if a_num % D != 0 or b_num % D != 0:
        return None
    
    a = a_num // D
    b = b_num // D
    
    # Check constraints: non-negative and within press limit (if any)
    if a < 0 or b < 0:
        return None
    
    if max_presses is not None and (a > max_presses or b > max_presses):
        return None
    
    return a, b


def solve_part1(data):
    """
    Solve part 1: Find minimum tokens for all winnable machines.
    Each button can be pressed at most 100 times.
    """
    machines = parse_machines(data)
    total_tokens = 0
    winnable_count = 0
    
    for ax, ay, bx, by, px, py in machines:
        solution = solve_machine(ax, ay, bx, by, px, py, max_presses=100)
        
        if solution:
            a, b = solution
            tokens = 3 * a + 1 * b
            total_tokens += tokens
            winnable_count += 1
            print(f"Machine: A({ax},{ay}) B({bx},{by}) Prize({px},{py})")
            print(f"  Solution: {a}×A + {b}×B = {tokens} tokens")
    
    print(f"\nWinnable machines: {winnable_count}/{len(machines)}")
    return total_tokens


def solve_part2(data):
    """
    Solve part 2: Find minimum tokens with prize coordinates increased by 10000000000000.
    No limit on button presses for part 2.
    """
    machines = parse_machines(data)
    total_tokens = 0
    winnable_count = 0
    
    OFFSET = 10000000000000
    
    for ax, ay, bx, by, px, py in machines:
        # Add huge offset to prize coordinates
        px_new = px + OFFSET
        py_new = py + OFFSET
        
        solution = solve_machine(ax, ay, bx, by, px_new, py_new, max_presses=None)
        
        if solution:
            a, b = solution
            tokens = 3 * a + 1 * b
            total_tokens += tokens
            winnable_count += 1
            print(f"Machine: A({ax},{ay}) B({bx},{by}) Prize({px_new},{py_new})")
            print(f"  Solution: {a}×A + {b}×B = {tokens} tokens")
    
    print(f"\nWinnable machines: {winnable_count}/{len(machines)}")
    return total_tokens


def main():
    """Main function to run both parts with test and real data."""
    
    # Test with example data
    print("=== Testing with example data ===")
    with open('test.txt', 'r') as f:
        test_data = f.read()
    
    print("Input machines:")
    print(test_data.strip())
    print()
    
    test_result1 = solve_part1(test_data)
    print(f"\nTest Part 1 (minimum tokens): {test_result1}")
    
    test_result2 = solve_part2(test_data)
    print(f"\nTest Part 2 (minimum tokens with offset): {test_result2}")
    
    # Real data
    print("\n" + "="*50)
    print("=== Running with real data ===")
    with open('input.txt', 'r') as f:
        real_data = f.read()
    
    result1 = solve_part1(real_data)
    print(f"\nPart 1 (minimum tokens): {result1}")
    
    result2 = solve_part2(real_data)
    print(f"Part 2 (minimum tokens with offset): {result2}")


if __name__ == "__main__":
    main()
