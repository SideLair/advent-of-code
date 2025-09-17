#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 16: Reindeer Maze

Part 1: Find lowest score path through maze using Dijkstra's algorithm
Part 2: Count all tiles that are part of any best path
"""

import heapq
from collections import defaultdict
from typing import List, Tuple, Set, Dict, Any, Union


def parse_input(filename: str) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
    """Parse input file into maze grid and find start/end positions.
    
    Args:
        filename: Path to input file
        
    Returns:
        Tuple containing:
        - grid: 2D list representing maze
        - start_pos: (row, col) tuple of start position
        - end_pos: (row, col) tuple of end position
    """
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    grid = []
    start_pos = None
    end_pos = None
    
    for row, line in enumerate(lines):
        grid_row = list(line)
        grid.append(grid_row)
        
        # Find start and end positions
        if 'S' in line:
            col = line.index('S')
            start_pos = (row, col)
            grid_row[col] = '.'  # Replace with empty space
        
        if 'E' in line:
            col = line.index('E')
            end_pos = (row, col)
            grid_row[col] = '.'  # Replace with empty space
    
    return grid, start_pos, end_pos


def get_directions() -> Tuple[Dict[int, Tuple[int, int]], Dict[int, str]]:
    """Get direction mappings.
    
    Returns:
        Tuple containing:
        - directions: dict mapping direction index to (dr, dc)
        - direction_names: dict mapping direction index to name
    """
    directions = {
        0: (-1, 0),  # North (up)
        1: (0, 1),   # East (right)
        2: (1, 0),   # South (down)
        3: (0, -1)   # West (left)
    }
    
    direction_names = {
        0: "North",
        1: "East", 
        2: "South",
        3: "West"
    }
    
    return directions, direction_names


def get_possible_actions(current_dir: int) -> List[Tuple[str, int, int]]:
    """Get possible actions from current direction.
    
    Args:
        current_dir: Current direction (0=North, 1=East, 2=South, 3=West)
        
    Returns:
        List of (action_type, new_direction, cost) tuples where:
        - action_type: 'move', 'turn_left', or 'turn_right'
        - new_direction: Resulting direction after action
        - cost: Cost of the action
    """
    actions = []
    
    # Move forward (same direction)
    actions.append(('move', current_dir, 1))
    
    # Turn left (counterclockwise)
    new_dir = (current_dir - 1) % 4
    actions.append(('turn_left', new_dir, 1000))
    
    # Turn right (clockwise)  
    new_dir = (current_dir + 1) % 4
    actions.append(('turn_right', new_dir, 1000))
    
    return actions


def dijkstra_shortest_path(
    grid: List[List[str]],
    start_pos: Tuple[int, int],
    end_pos: Tuple[int, int],
    start_direction: int = 1
) -> Tuple[int, Dict[Tuple[int, int, int], Tuple[Tuple[int, int, int], str]]]:
    """Find shortest path using Dijkstra's algorithm.
    
    Args:
        grid: 2D list representing the maze
        start_pos: (row, col) starting position
        end_pos: (row, col) target position
        start_direction: Initial direction (1=East as per problem statement)
        
    Returns:
        Tuple containing:
        - min_cost: Minimum cost to reach end (inf if no path exists)
        - came_from: Dictionary for path reconstruction
    """
    directions, _ = get_directions()
    
    # Priority queue: (cost, row, col, direction)
    pq = [(0, start_pos[0], start_pos[1], start_direction)]
    
    # Best cost to reach each state
    best_cost = {}
    best_cost[(start_pos[0], start_pos[1], start_direction)] = 0
    
    # For path reconstruction
    came_from = {}
    
    while pq:
        current_cost, row, col, direction = heapq.heappop(pq)
        
        # Skip if we've found a better path to this state
        state = (row, col, direction)
        if state in best_cost and current_cost > best_cost[state]:
            continue
        
        # Check if we reached the end
        if (row, col) == end_pos:
            return current_cost, came_from
        
        # Try all possible actions
        for action_type, new_direction, action_cost in get_possible_actions(direction):
            new_cost = current_cost + action_cost
            
            if action_type == 'move':
                # Move forward in current direction
                dr, dc = directions[direction]
                new_row, new_col = row + dr, col + dc
                
                # Check bounds and walls
                if (0 <= new_row < len(grid) and 
                    0 <= new_col < len(grid[0]) and 
                    grid[new_row][new_col] != '#'):
                    
                    new_state = (new_row, new_col, new_direction)
                    
                    # Only add if we found a better path
                    if new_state not in best_cost or new_cost < best_cost[new_state]:
                        best_cost[new_state] = new_cost
                        came_from[new_state] = (state, action_type)
                        heapq.heappush(pq, (new_cost, new_row, new_col, new_direction))
            
            else:  # Turn left or right
                # Stay in same position, just change direction
                new_state = (row, col, new_direction)
                
                if new_state not in best_cost or new_cost < best_cost[new_state]:
                    best_cost[new_state] = new_cost
                    came_from[new_state] = (state, action_type)
                    heapq.heappush(pq, (new_cost, row, col, new_direction))
    
    return float('inf'), {}


def solve_part1(filename: str) -> int:
    """Solve part 1: Find lowest score path through maze.
    
    Args:
        filename: Path to input file
        
    Returns:
        Minimum cost to reach the end, or None if no path exists
    """
    # Parse input
    grid, start_pos, end_pos = parse_input(filename)
    
    # Find shortest path using Dijkstra
    min_cost, _ = dijkstra_shortest_path(grid, start_pos, end_pos)
    
    if min_cost == float('inf'):
        return None
    
    return min_cost


def find_all_best_paths(
    grid: List[List[str]],
    start_pos: Tuple[int, int],
    end_pos: Tuple[int, int],
    start_direction: int = 1
) -> Tuple[Set[Tuple[int, int]], int]:
    """Find all tiles that are part of any optimal path.
    
    Args:
        grid: 2D list representing the maze
        start_pos: (row, col) starting position
        end_pos: (row, col) target position
        start_direction: Initial direction (1=East as per problem statement)
        
    Returns:
        Tuple containing:
        - best_tiles: set of (row, col) positions on any best path
        - min_cost: the minimum cost to reach end (inf if no path exists)
    """
    directions, _ = get_directions()
    
    # Forward pass - find minimum cost to reach each state
    pq = [(0, start_pos[0], start_pos[1], start_direction)]
    dist = {}
    dist[(start_pos[0], start_pos[1], start_direction)] = 0
    
    while pq:
        current_cost, row, col, direction = heapq.heappop(pq)
        
        state = (row, col, direction)
        if state in dist and current_cost > dist[state]:
            continue
        
        # Try all possible actions
        for action_type, new_direction, action_cost in get_possible_actions(direction):
            new_cost = current_cost + action_cost
            
            if action_type == 'move':
                dr, dc = directions[direction]
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < len(grid) and 
                    0 <= new_col < len(grid[0]) and 
                    grid[new_row][new_col] != '#'):
                    
                    new_state = (new_row, new_col, new_direction)
                    
                    if new_state not in dist or new_cost < dist[new_state]:
                        dist[new_state] = new_cost
                        heapq.heappush(pq, (new_cost, new_row, new_col, new_direction))
            
            else:  # Turn
                new_state = (row, col, new_direction)
                
                if new_state not in dist or new_cost < dist[new_state]:
                    dist[new_state] = new_cost
                    heapq.heappush(pq, (new_cost, row, col, new_direction))
    
    # Find minimum cost to reach end
    min_cost = float('inf')
    for direction in range(4):
        end_state = (end_pos[0], end_pos[1], direction)
        if end_state in dist:
            min_cost = min(min_cost, dist[end_state])
    
    if min_cost == float('inf'):
        return set(), min_cost
    
    # Backward pass - find all states that can reach end optimally
    best_tiles = set()
    queue = []
    
    # Start from all end states with minimum cost
    for direction in range(4):
        end_state = (end_pos[0], end_pos[1], direction)
        if end_state in dist and dist[end_state] == min_cost:
            queue.append(end_state)
            best_tiles.add((end_pos[0], end_pos[1]))
    
    visited_backward = set(queue)
    
    while queue:
        row, col, direction = queue.pop(0)
        current_cost = dist[(row, col, direction)]
        
        # Check all possible previous states
        for action_type, prev_direction, action_cost in get_possible_actions(direction):
            prev_cost = current_cost - action_cost
            
            if action_type == 'move':
                # Previous state was one step back
                dr, dc = directions[prev_direction]
                prev_row, prev_col = row - dr, col - dc
                
                if (0 <= prev_row < len(grid) and 
                    0 <= prev_col < len(grid[0]) and 
                    grid[prev_row][prev_col] != '#'):
                    
                    prev_state = (prev_row, prev_col, prev_direction)
                    
                    if (prev_state in dist and 
                        dist[prev_state] == prev_cost and 
                        prev_state not in visited_backward):
                        
                        queue.append(prev_state)
                        visited_backward.add(prev_state)
                        best_tiles.add((prev_row, prev_col))
            
            else:  # Previous state was a turn
                # Same position, different direction
                prev_state = (row, col, prev_direction)
                
                if (prev_state in dist and 
                    dist[prev_state] == prev_cost and 
                    prev_state not in visited_backward):
                    
                    queue.append(prev_state)
                    visited_backward.add(prev_state)
                    best_tiles.add((row, col))
    
    return best_tiles, min_cost


def solve_part2(filename: str) -> int:
    """Solve part 2: Count tiles that are part of any best path.
    
    Args:
        filename: Path to input file
        
    Returns:
        Number of tiles that are part of any optimal path, or None if no path exists
    """
    # Parse input
    grid, start_pos, end_pos = parse_input(filename)
    
    # Find all best paths
    best_tiles, min_cost = find_all_best_paths(grid, start_pos, end_pos)
    
    if min_cost == float('inf'):
        return None
    
    return len(best_tiles)


def main() -> None:
    """Run both parts with test and real data."""
    # Test data first
    print("=== Test Data ===")
    test_result1 = solve_part1('test.txt')
    print(f"Test Part 1: {test_result1}")
    
    # Real data
    print("\n=== Real Data ===")
    result1 = solve_part1('input.txt')
    print(f"Part 1: {result1}")
    
    # Part 2
    print("\n=== Test Data Part 2 ===")
    test_result2 = solve_part2('test.txt')
    print(f"Test Part 2: {test_result2}")
    
    print("\n=== Real Data Part 2 ===")
    result2 = solve_part2('input.txt')
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
