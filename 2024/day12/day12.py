#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 12: Garden Groups

Calculate the total price of fencing all regions in a garden map.
Each region is a connected group of garden plots with the same plant type.

Part 1: Price = area × perimeter for each region
Part 2: Price = area × number of sides for each region (bulk discount)

The garden map shows different plant types as letters. Connected plots
(horizontally or vertically adjacent) of the same letter form a region.
"""

from collections import deque


def parse_garden(data):
    """Parse the garden map into a 2D grid."""
    lines = data.strip().split('\n')
    return [list(line) for line in lines]


def get_neighbors(row, col, rows, cols):
    """Get valid neighboring coordinates (up, down, left, right)."""
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors


def find_region(garden, start_row, start_col, visited):
    """
    Find all plots in a region using BFS.
    Returns set of coordinates belonging to this region.
    """
    rows, cols = len(garden), len(garden[0])
    plant_type = garden[start_row][start_col]
    region = set()
    queue = deque([(start_row, start_col)])
    
    while queue:
        row, col = queue.popleft()
        if (row, col) in visited or (row, col) in region:
            continue
            
        if garden[row][col] != plant_type:
            continue
            
        region.add((row, col))
        visited.add((row, col))
        
        # Add neighbors to queue
        for nr, nc in get_neighbors(row, col, rows, cols):
            if (nr, nc) not in visited and garden[nr][nc] == plant_type:
                queue.append((nr, nc))
    
    return region


def calculate_perimeter(region, garden):
    """
    Calculate perimeter of a region.
    Perimeter = number of edges that border different plant types or garden boundary.
    """
    rows, cols = len(garden), len(garden[0])
    perimeter = 0
    
    for row, col in region:
        # Check all 4 directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            # Edge contributes to perimeter if it's outside garden or different plant type
            if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or 
                garden[nr][nc] != garden[row][col]):
                perimeter += 1
    
    return perimeter


def calculate_sides(region, garden):
    """
    Calculate number of sides of a region.
    A side is a continuous edge along one direction.
    """
    rows, cols = len(garden), len(garden[0])
    plant_type = garden[next(iter(region))[0]][next(iter(region))[1]]
    
    # For each direction, find all edge segments
    sides = 0
    
    # Check horizontal edges (top and bottom)
    for direction in [(-1, 0), (1, 0)]:  # up, down
        edges = set()
        for row, col in region:
            nr, nc = row + direction[0], col + direction[1]
            # This is an edge if neighbor is outside or different plant
            if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or 
                garden[nr][nc] != plant_type):
                edges.add((row, col, direction))
        
        # Group consecutive horizontal edges into sides
        visited_edges = set()
        for row, col, dir_vec in edges:
            if (row, col, dir_vec) in visited_edges:
                continue
            
            # Start a new side - extend left and right
            sides += 1
            visited_edges.add((row, col, dir_vec))
            
            # Extend right
            c = col + 1
            while (row, c, dir_vec) in edges:
                visited_edges.add((row, c, dir_vec))
                c += 1
            
            # Extend left
            c = col - 1
            while (row, c, dir_vec) in edges:
                visited_edges.add((row, c, dir_vec))
                c -= 1
    
    # Check vertical edges (left and right)
    for direction in [(0, -1), (0, 1)]:  # left, right
        edges = set()
        for row, col in region:
            nr, nc = row + direction[0], col + direction[1]
            # This is an edge if neighbor is outside or different plant
            if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or 
                garden[nr][nc] != plant_type):
                edges.add((row, col, direction))
        
        # Group consecutive vertical edges into sides
        visited_edges = set()
        for row, col, dir_vec in edges:
            if (row, col, dir_vec) in visited_edges:
                continue
            
            # Start a new side - extend up and down
            sides += 1
            visited_edges.add((row, col, dir_vec))
            
            # Extend down
            r = row + 1
            while (r, col, dir_vec) in edges:
                visited_edges.add((r, col, dir_vec))
                r += 1
            
            # Extend up
            r = row - 1
            while (r, col, dir_vec) in edges:
                visited_edges.add((r, col, dir_vec))
                r -= 1
    
    return sides


def solve_part1(data):
    """
    Solve part 1: Calculate total fencing cost using area × perimeter.
    """
    garden = parse_garden(data)
    rows, cols = len(garden), len(garden[0])
    visited = set()
    total_cost = 0
    
    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                region = find_region(garden, row, col, visited)
                if region:
                    area = len(region)
                    perimeter = calculate_perimeter(region, garden)
                    cost = area * perimeter
                    total_cost += cost
    
    return total_cost


def solve_part2(data):
    """
    Solve part 2: Calculate total fencing cost using area × number of sides.
    """
    garden = parse_garden(data)
    rows, cols = len(garden), len(garden[0])
    visited = set()
    total_cost = 0
    
    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                region = find_region(garden, row, col, visited)
                if region:
                    area = len(region)
                    sides = calculate_sides(region, garden)
                    cost = area * sides
                    total_cost += cost
    
    return total_cost


def main():
    """Main function to run both parts with test and real data."""
    
    # Test with example data
    print("=== Testing with example data ===")
    with open('test.txt', 'r') as f:
        test_data = f.read()
    
    print("Garden map:")
    print(test_data.strip())
    
    # Show detailed analysis for test data
    garden = parse_garden(test_data)
    visited = set()
    regions_info = []
    
    for row in range(len(garden)):
        for col in range(len(garden[0])):
            if (row, col) not in visited:
                region = find_region(garden, row, col, visited)
                if region:
                    plant_type = garden[row][col]
                    area = len(region)
                    perimeter = calculate_perimeter(region, garden)
                    sides = calculate_sides(region, garden)
                    regions_info.append((plant_type, area, perimeter, sides))
    
    print(f"\nRegions found:")
    for plant_type, area, perimeter, sides in regions_info:
        print(f"Region {plant_type}: area={area}, perimeter={perimeter}, sides={sides}")
        print(f"  Part 1 cost: {area} × {perimeter} = {area * perimeter}")
        print(f"  Part 2 cost: {area} × {sides} = {area * sides}")
    
    test_result1 = solve_part1(test_data)
    test_result2 = solve_part2(test_data)
    print(f"\nTest Part 1 (area × perimeter): {test_result1}")
    print(f"Test Part 2 (area × sides): {test_result2}")
    
    # Real data
    print("\n=== Running with real data ===")
    with open('input.txt', 'r') as f:
        real_data = f.read()
    
    result1 = solve_part1(real_data)
    print(f"Part 1 (area × perimeter): {result1}")
    
    result2 = solve_part2(real_data)
    print(f"Part 2 (area × sides): {result2}")


if __name__ == "__main__":
    main()
