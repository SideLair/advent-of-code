#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 14: Restroom Redoubt

Part 1: Calculate safety factor after 100 seconds (product of quadrant counts)
Part 2: Find Christmas tree pattern by minimizing safety factor (entropy)
"""

import re


def parse_robots(data):
    """
    Parse input data into list of robot configurations.
    Each line: p=x,y v=vx,vy
    Returns list of tuples: (x, y, vx, vy)
    """
    robots = []
    lines = data.strip().split('\n')
    
    for line in lines:
        if line.strip():
            # Parse: p=0,4 v=3,-3
            match = re.search(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
            if match:
                x, y, vx, vy = map(int, match.groups())
                robots.append((x, y, vx, vy))
    
    return robots


def simulate_robots(robots, width, height, seconds=100):
    """
    Calculate final positions of all robots after given seconds.
    Uses direct calculation instead of step-by-step simulation.
    
    Returns list of final positions: [(x, y), ...]
    """
    final_positions = []
    
    for x, y, vx, vy in robots:
        # Direct calculation: final_pos = (start + seconds * velocity) % size
        final_x = (x + seconds * vx) % width
        final_y = (y + seconds * vy) % height
        final_positions.append((final_x, final_y))
    
    return final_positions


def count_quadrants(positions, width, height):
    """
    Count robots in each quadrant.
    Grid has odd dimensions, so middle row/column don't count.
    
    For 11×7 grid:
    - Center: x=5, y=3 (excluded)
    - Q1 (top-left): x ∈ [0,4], y ∈ [0,2]
    - Q2 (top-right): x ∈ [6,10], y ∈ [0,2]  
    - Q3 (bottom-left): x ∈ [0,4], y ∈ [4,6]
    - Q4 (bottom-right): x ∈ [6,10], y ∈ [4,6]
    
    Returns (q1, q2, q3, q4) counts.
    """
    mid_x = width // 2
    mid_y = height // 2
    
    q1 = q2 = q3 = q4 = 0
    
    for x, y in positions:
        # Skip robots on middle lines
        if x == mid_x or y == mid_y:
            continue
            
        if x < mid_x and y < mid_y:
            q1 += 1  # Top-left
        elif x > mid_x and y < mid_y:
            q2 += 1  # Top-right
        elif x < mid_x and y > mid_y:
            q3 += 1  # Bottom-left
        elif x > mid_x and y > mid_y:
            q4 += 1  # Bottom-right
    
    return q1, q2, q3, q4


def solve_part1(data, width, height):
    """
    Solve part 1: Calculate safety factor after 100 seconds.
    Safety factor = product of robot counts in all 4 quadrants.
    """
    robots = parse_robots(data)
    print(f"Parsed {len(robots)} robots")
    
    # Simulate 100 seconds
    final_positions = simulate_robots(robots, width, height, seconds=100)
    
    # Count quadrants
    q1, q2, q3, q4 = count_quadrants(final_positions, width, height)
    
    print(f"Quadrant counts after 100 seconds:")
    print(f"  Q1 (top-left): {q1}")
    print(f"  Q2 (top-right): {q2}")
    print(f"  Q3 (bottom-left): {q3}")
    print(f"  Q4 (bottom-right): {q4}")
    
    safety_factor = q1 * q2 * q3 * q4
    return safety_factor




def visualize_grid(positions, width, height, max_lines=20):
    """
    Create simple ASCII visualization of robot positions.
    Limit output to max_lines for readability.
    """
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    # Mark robot positions
    for x, y in positions:
        grid[y][x] = '#'
    
    # Convert to string, but limit lines
    lines = []
    for row in grid[:max_lines]:
        lines.append(''.join(row))
    
    if height > max_lines:
        lines.append(f"... ({height - max_lines} more lines)")
    
    return '\n'.join(lines)


def solve_part2(data, width, height):
    """
    Find Christmas tree pattern by minimizing safety factor.
    When robots cluster into a tree, safety factor drops significantly.
    """
    robots = parse_robots(data)
    print(f"Searching for Christmas tree among {len(robots)} robots...")
    
    min_safety_factor = float('inf')
    best_tick = 0
    best_positions = []
    
    for tick in range(1, 10000):  # Search first 10k ticks
        positions = simulate_robots(robots, width, height, seconds=tick)
        q1, q2, q3, q4 = count_quadrants(positions, width, height)
        safety_factor = q1 * q2 * q3 * q4
        
        if safety_factor < min_safety_factor:
            min_safety_factor = safety_factor
            best_tick = tick
            best_positions = positions
            print(f"New minimum: {safety_factor} at tick {tick}")
        
        if tick % 1000 == 0:
            print(f"Checked {tick} ticks, best: {min_safety_factor} at {best_tick}")
    
    print(f"\n🎄 Christmas tree found at tick {best_tick}!")
    
    # Save visualization
    full_viz = visualize_grid(best_positions, width, height, max_lines=height)
    with open('tree.txt', 'w') as f:
        f.write(f"Christmas Tree at tick {best_tick}\n")
        f.write(f"Safety factor: {min_safety_factor}\n")
        f.write("="*width + "\n")
        f.write(full_viz)
    
    return best_tick


def main():
    """Run both parts with test and real data."""
    
    # Test data
    print("=== Test Data (11×7) ===")
    with open('test.txt', 'r') as f:
        test_data = f.read()
    
    test_result1 = solve_part1(test_data, width=11, height=7)
    print(f"Test Part 1: {test_result1}")
    
    # Real data
    print("\n=== Real Data (101×103) ===")
    with open('input.txt', 'r') as f:
        real_data = f.read()
    
    result1 = solve_part1(real_data, width=101, height=103)
    print(f"Part 1: {result1}")
    
    result2 = solve_part2(real_data, width=101, height=103)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
