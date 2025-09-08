#!/usr/bin/env python3

from collections import defaultdict

def parse_grid(input_data):
    """Parse input into grid and find antenna positions"""
    lines = input_data.strip().split('\n')
    grid = [list(line) for line in lines]
    height, width = len(grid), len(grid[0])
    
    # Group antennas by their frequency/type
    antennas = defaultdict(list)
    
    for row in range(height):
        for col in range(width):
            cell = grid[row][col]
            if cell != '.':
                antennas[cell].append((row, col))
    
    return grid, antennas, height, width

def calculate_antinodes_part1(antennas, height, width):
    """Calculate antinode positions for part 1"""
    antinodes = set()
    
    # For each antenna frequency/type
    for frequency, positions in antennas.items():
        # For each pair of antennas with same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                pos1, pos2 = positions[i], positions[j]
                r1, c1 = pos1
                r2, c2 = pos2
                
                # Calculate vector from pos1 to pos2
                dr = r2 - r1
                dc = c2 - c1
                
                # Antinode 1: extend beyond pos2 by same distance
                antinode1 = (r2 + dr, c2 + dc)
                if 0 <= antinode1[0] < height and 0 <= antinode1[1] < width:
                    antinodes.add(antinode1)
                
                # Antinode 2: extend beyond pos1 in opposite direction
                antinode2 = (r1 - dr, c1 - dc)
                if 0 <= antinode2[0] < height and 0 <= antinode2[1] < width:
                    antinodes.add(antinode2)
    
    return antinodes

def calculate_antinodes_part2(antennas, height, width):
    """Calculate antinode positions for part 2 (with harmonics)"""
    antinodes = set()
    
    # For each antenna frequency/type
    for frequency, positions in antennas.items():
        # For each pair of antennas with same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                pos1, pos2 = positions[i], positions[j]
                r1, c1 = pos1
                r2, c2 = pos2
                
                # Calculate vector from pos1 to pos2
                dr = r2 - r1
                dc = c2 - c1
                
                # Add all points along the line in both directions
                # Start from pos1 and go backwards
                r, c = r1, c1
                while 0 <= r < height and 0 <= c < width:
                    antinodes.add((r, c))
                    r -= dr
                    c -= dc
                
                # Start from pos1 and go forwards
                r, c = r1, c1
                while 0 <= r < height and 0 <= c < width:
                    antinodes.add((r, c))
                    r += dr
                    c += dc
    
    return antinodes

def solve_part1(input_data):
    """
    Find unique antinode positions created by pairs of same-frequency antennas.
    Each pair creates antinodes at positions extending the line between them.
    """
    grid, antennas, height, width = parse_grid(input_data)
    antinodes = calculate_antinodes_part1(antennas, height, width)
    return len(antinodes)

def solve_part2(input_data):
    """
    Find unique antinode positions with harmonics - antinodes occur at all
    positions along the line formed by any pair of same-frequency antennas.
    """
    grid, antennas, height, width = parse_grid(input_data)
    antinodes = calculate_antinodes_part2(antennas, height, width)
    return len(antinodes)

def main():
    # Test data from problem description
    test_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    
    print("Test data:")
    part1_result = solve_part1(test_data)
    part2_result = solve_part2(test_data)
    print(f"Part 1: {part1_result} (expected: 14)")
    print(f"Part 2: {part2_result}")
    
    # Validate test results
    assert part1_result == 14, f"Part 1 test failed: got {part1_result}, expected 14"
    print("✓ Part 1 test validation passed")
    print()
    
    # Real data
    with open('input.txt', 'r') as f:
        input_data = f.read()
    
    print("Real data:")
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")

if __name__ == "__main__":
    main()