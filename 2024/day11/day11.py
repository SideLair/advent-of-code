#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 11: Plutonian Pebbles

Stone transformation rules:
1. If stone is 0, it becomes 1
2. If stone has even number of digits, split into two stones (left half, right half with leading zeros removed)
3. Otherwise, multiply by 2024

Each iteration processes all stones simultaneously according to these rules.
"""

from collections import Counter


def transform_stone(stone):
    """
    Transform a single stone according to the rules.
    Returns a list of resulting stones (1 or 2 stones).
    """
    if stone == 0:
        return [1]
    
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        # Even number of digits - split in half
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])  # int() automatically removes leading zeros
        return [left, right]
    
    # Odd number of digits - multiply by 2024
    return [stone * 2024]


def simulate_stones(stones, iterations):
    """
    Simulate stone transformations for given number of iterations.
    Uses Counter for efficient handling of large numbers of identical stones.
    """
    # Use Counter to track how many of each stone value we have
    stone_counts = Counter(stones)
    
    for iteration in range(iterations):
        new_counts = Counter()
        
        for stone_value, count in stone_counts.items():
            # Transform this stone value and add results to new counts
            transformed = transform_stone(stone_value)
            for new_stone in transformed:
                new_counts[new_stone] += count
        
        stone_counts = new_counts
    
    return sum(stone_counts.values())


def solve_part1(data):
    """
    Solve part 1: Count stones after 25 iterations.
    """
    stones = list(map(int, data.strip().split()))
    return simulate_stones(stones, 25)


def solve_part2(data):
    """
    Solve part 2: Count stones after 75 iterations.
    """
    stones = list(map(int, data.strip().split()))
    return simulate_stones(stones, 75)


def main():
    """Main function to run both parts with test and real data."""
    
    # Test with example data
    print("=== Testing with example data ===")
    with open('test.txt', 'r') as f:
        test_data = f.read()
    
    print("Initial stones:", test_data.strip())
    
    # Show first few iterations for understanding
    stones = list(map(int, test_data.strip().split()))
    print(f"After 0 blinks: {stones} (count: {len(stones)})")
    
    for i in range(1, 7):
        result_count = simulate_stones(list(map(int, test_data.strip().split())), i)
        print(f"After {i} blinks: count = {result_count}")
    
    test_result1 = solve_part1(test_data)
    print(f"\nTest Part 1 (25 blinks): {test_result1}")
    
    # Real data
    print("\n=== Running with real data ===")
    with open('input.txt', 'r') as f:
        real_data = f.read()
    
    result1 = solve_part1(real_data)
    print(f"Part 1 (25 blinks): {result1}")
    
    result2 = solve_part2(real_data)
    print(f"Part 2 (75 blinks): {result2}")


if __name__ == "__main__":
    main()
