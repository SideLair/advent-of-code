#!/usr/bin/env python3

def solve_part1(input_data):
    lines = input_data.strip().split('\n')
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])
    
    # Find guard starting position and direction
    guard_pos = None
    guard_dir = None
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = directions[grid[r][c]]
                grid[r][c] = '.'  # Clear starting position
                break
        if guard_pos:
            break
    
    # Direction rotation (right turn): up -> right -> down -> left -> up
    dir_cycle = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir_idx = dir_cycle.index(guard_dir)
    
    visited = set()
    visited.add(guard_pos)
    
    while True:
        r, c = guard_pos
        dr, dc = dir_cycle[current_dir_idx]
        next_r, next_c = r + dr, c + dc
        
        # Check if guard would leave the area
        if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
            break
            
        # Check if there's an obstacle ahead
        if grid[next_r][next_c] == '#':
            # Turn right (90 degrees clockwise)
            current_dir_idx = (current_dir_idx + 1) % 4
        else:
            # Move forward
            guard_pos = (next_r, next_c)
            visited.add(guard_pos)
    
    return len(visited)

def solve_part2(input_data):
    lines = input_data.strip().split('\n')
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])
    
    # Find guard starting position and direction
    start_pos = None
    start_dir = None
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                start_pos = (r, c)
                start_dir = directions[grid[r][c]]
                grid[r][c] = '.'  # Clear starting position
                break
        if start_pos:
            break
    
    # Get original path (positions guard visits without new obstacles)
    def get_original_path():
        dir_cycle = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        current_dir_idx = dir_cycle.index(start_dir)
        guard_pos = start_pos
        visited = set()
        visited.add(guard_pos)
        
        while True:
            r, c = guard_pos
            dr, dc = dir_cycle[current_dir_idx]
            next_r, next_c = r + dr, c + dc
            
            if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                break
                
            if grid[next_r][next_c] == '#':
                current_dir_idx = (current_dir_idx + 1) % 4
            else:
                guard_pos = (next_r, next_c)
                visited.add(guard_pos)
        
        return visited
    
    # Check if placing obstacle at position causes cycle
    def causes_cycle(obstacle_pos):
        if obstacle_pos == start_pos or grid[obstacle_pos[0]][obstacle_pos[1]] == '#':
            return False
            
        # Temporarily place obstacle
        grid[obstacle_pos[0]][obstacle_pos[1]] = '#'
        
        # Simulate guard movement with state tracking (position + direction)
        dir_cycle = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        current_dir_idx = dir_cycle.index(start_dir)
        guard_pos = start_pos
        states = set()  # Track (position, direction) pairs
        
        while True:
            state = (guard_pos, current_dir_idx)
            if state in states:
                # Cycle detected!
                grid[obstacle_pos[0]][obstacle_pos[1]] = '.'  # Remove temporary obstacle
                return True
            states.add(state)
            
            r, c = guard_pos
            dr, dc = dir_cycle[current_dir_idx]
            next_r, next_c = r + dr, c + dc
            
            # Check if guard would leave the area
            if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                grid[obstacle_pos[0]][obstacle_pos[1]] = '.'  # Remove temporary obstacle
                return False
                
            # Check if there's an obstacle ahead
            if grid[next_r][next_c] == '#':
                current_dir_idx = (current_dir_idx + 1) % 4
            else:
                guard_pos = (next_r, next_c)
    
    # Get all positions the guard visits in original path
    original_path = get_original_path()
    
    # Test each position on original path (except starting position)
    cycle_positions = 0
    test_positions = original_path - {start_pos}
    
    for pos in test_positions:
        if causes_cycle(pos):
            cycle_positions += 1
    
    return cycle_positions

def main():
    # Test data from problem description
    test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    
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