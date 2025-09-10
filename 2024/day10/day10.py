#!/usr/bin/env python3

from collections import deque

def parse_topographic_map(input_data):
    """
    Parse the input into a 2D grid of heights.
    
    Each character represents a height from 0-9.
    Returns a list of lists where grid[row][col] = height.
    """
    lines = input_data.strip().split('\n')
    grid = []
    
    for line in lines:
        if line.strip():  # Skip empty lines
            row = [int(char) for char in line.strip()]
            grid.append(row)
    
    return grid

def find_trailheads(grid):
    """
    Find all trailheads (positions with height 0) in the grid.
    
    Returns a list of (row, col) tuples representing trailhead positions.
    """
    trailheads = []
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                trailheads.append((row, col))
    
    return trailheads

def get_neighbors(row, col, grid):
    """
    Get valid neighboring positions (up, down, left, right) within grid bounds.
    
    Returns a list of (row, col) tuples for valid neighbors.
    """
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        
        # Check if the new position is within grid bounds
        if (0 <= new_row < len(grid) and 
            0 <= new_col < len(grid[new_row])):
            neighbors.append((new_row, new_col))
    
    return neighbors

def find_reachable_peaks(grid, start_row, start_col):
    """
    Find all peaks (height 9) reachable from a trailhead using BFS.
    
    A valid hiking trail:
    - Starts at height 0
    - Ends at height 9  
    - Each step increases height by exactly 1
    - Only moves horizontally/vertically
    
    Returns a set of (row, col) tuples representing reachable peaks.
    """
    if grid[start_row][start_col] != 0:
        return set()  # Not a valid trailhead
    
    # BFS to find all reachable positions
    queue = deque([(start_row, start_col, 0)])  # (row, col, current_height)
    visited = set()
    reachable_peaks = set()
    
    while queue:
        row, col, height = queue.popleft()
        
        # Skip if we've already visited this position at this height
        if (row, col, height) in visited:
            continue
        visited.add((row, col, height))
        
        # If we reached a peak (height 9), add it to our results
        if height == 9:
            reachable_peaks.add((row, col))
            continue
        
        # Explore neighbors that have height = current_height + 1
        for next_row, next_col in get_neighbors(row, col, grid):
            next_height = grid[next_row][next_col]
            
            # Valid trail step: height increases by exactly 1
            if next_height == height + 1:
                queue.append((next_row, next_col, next_height))
    
    return reachable_peaks

def solve_part1(input_data):
    """
    Solve part 1: Find the sum of scores of all trailheads.
    
    A trailhead's score = number of different height-9 positions 
    reachable from that trailhead via valid hiking trails.
    
    Process:
    1. Parse the topographic map
    2. Find all trailheads (height 0 positions)
    3. For each trailhead, count reachable peaks (height 9 positions)
    4. Sum all trailhead scores
    """
    grid = parse_topographic_map(input_data)
    trailheads = find_trailheads(grid)
    
    total_score = 0
    
    for row, col in trailheads:
        reachable_peaks = find_reachable_peaks(grid, row, col)
        score = len(reachable_peaks)
        total_score += score
        
        # Debug output for understanding
        print(f"Trailhead at ({row}, {col}): score = {score}")
    
    return total_score

def count_distinct_trails(grid, start_row, start_col):
    """
    Count the number of distinct hiking trails from a trailhead to any peak.
    
    A distinct trail is a unique path from height 0 to height 9.
    This is different from part 1 - we count paths, not just reachable destinations.
    
    Returns the total number of distinct trails (rating of the trailhead).
    """
    if grid[start_row][start_col] != 0:
        return 0  # Not a valid trailhead
    
    def dfs(row, col, height):
        """Recursive DFS to count all possible trails."""
        # Base case: reached a peak
        if height == 9:
            return 1
        
        trail_count = 0
        
        # Explore all valid neighbors
        for next_row, next_col in get_neighbors(row, col, grid):
            next_height = grid[next_row][next_col]
            
            # Valid trail step: height increases by exactly 1
            if next_height == height + 1:
                trail_count += dfs(next_row, next_col, next_height)
        
        return trail_count
    
    return dfs(start_row, start_col, 0)

def solve_part2(input_data):
    """
    Solve part 2: Find the sum of ratings of all trailheads.
    
    A trailhead's rating = number of distinct hiking trails that begin at that trailhead.
    
    Process:
    1. Parse the topographic map
    2. Find all trailheads (height 0 positions)
    3. For each trailhead, count distinct trails to any peak
    4. Sum all trailhead ratings
    """
    grid = parse_topographic_map(input_data)
    trailheads = find_trailheads(grid)
    
    total_rating = 0
    
    for row, col in trailheads:
        rating = count_distinct_trails(grid, row, col)
        total_rating += rating
        
        # Debug output for understanding
        print(f"Trailhead at ({row}, {col}): rating = {rating}")
    
    return total_rating

def main():
    # Test with the provided test data
    with open('test.txt', 'r') as f:
        test_data = f.read()
    
    print("=== Test Data ===")
    print("Grid:")
    grid = parse_topographic_map(test_data)
    for row in grid:
        print(''.join(map(str, row)))
    print()
    
    print("Part 1 (sum of trailhead scores):")
    part1_result = solve_part1(test_data)
    print(f"Result: {part1_result}")
    print()
    
    print("Part 2 (sum of trailhead ratings):")
    part2_result = solve_part2(test_data)
    print(f"Result: {part2_result}")
    print()
    
    # Real data
    with open('input.txt', 'r') as f:
        input_data = f.read()
    
    print("=== Real Data ===")
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))

if __name__ == "__main__":
    main()