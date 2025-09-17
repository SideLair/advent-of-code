#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 15: Warehouse Woes

Part 1: Simulate robot pushing boxes in warehouse, calculate GPS coordinates sum
Part 2: TBD (wider boxes)
"""


def parse_input(filename):
    """
    Parse input file into warehouse grid and movement instructions.
    
    Returns:
        grid: 2D list representing warehouse
        robot_pos: (row, col) tuple of robot starting position
        moves: string of movement instructions
    """
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    # Split into warehouse map and moves
    parts = content.split('\n\n')
    warehouse_lines = parts[0].split('\n')
    moves = ''.join(parts[1].split('\n'))  # Remove newlines from moves
    
    # Create 2D grid
    grid = []
    robot_pos = None
    
    for row, line in enumerate(warehouse_lines):
        grid_row = list(line)
        grid.append(grid_row)
        
        # Find robot position
        if '@' in line:
            col = line.index('@')
            robot_pos = (row, col)
            grid_row[col] = '.'  # Replace robot with empty space
    
    return grid, robot_pos, moves


def get_direction(move_char):
    """Convert movement character to (row_delta, col_delta)."""
    directions = {
        '^': (-1, 0),  # Up
        'v': (1, 0),   # Down
        '<': (0, -1),  # Left
        '>': (0, 1)    # Right
    }
    return directions[move_char]


def can_push_boxes(grid, start_row, start_col, dr, dc):
    """
    Check if boxes can be pushed in given direction.
    
    Returns:
        True if push is possible, False otherwise
    """
    row, col = start_row, start_col
    
    # Follow the line of boxes
    while grid[row][col] == 'O':
        row += dr
        col += dc
    
    # Check what we hit at the end
    return grid[row][col] == '.'  # True if empty space, False if wall


def push_boxes(grid, start_row, start_col, dr, dc):
    """
    Push all boxes in a line by one position.
    Assumes can_push_boxes() returned True.
    """
    # Find the end of the box chain
    row, col = start_row, start_col
    while grid[row][col] == 'O':
        row += dr
        col += dc
    
    # Now (row, col) is the empty space at the end
    # Move the last box there
    grid[row][col] = 'O'
    
    # Remove the first box (where robot will move)
    grid[start_row][start_col] = '.'


def simulate_robot(grid, robot_pos, moves):
    """
    Simulate robot movement through warehouse.
    
    Returns:
        Final robot position (not needed for part 1, but good to have)
    """
    row, col = robot_pos
    
    for move in moves:
        dr, dc = get_direction(move)
        new_row, new_col = row + dr, col + dc
        
        # Check what's at the new position
        cell = grid[new_row][new_col]
        
        if cell == '#':
            # Hit wall, can't move
            continue
        elif cell == '.':
            # Empty space, move robot
            row, col = new_row, new_col
        elif cell == 'O':
            # Hit box, try to push
            if can_push_boxes(grid, new_row, new_col, dr, dc):
                push_boxes(grid, new_row, new_col, dr, dc)
                row, col = new_row, new_col
            # If can't push, robot doesn't move
    
    return (row, col)


def calculate_gps_sum(grid):
    """
    Calculate sum of GPS coordinates for all boxes.
    GPS coordinate = 100 * row + col
    """
    total = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'O':
                gps = 100 * row + col
                total += gps
    
    return total


def print_grid(grid, robot_pos=None):
    """Debug helper to visualize current state."""
    for row in range(len(grid)):
        line = ""
        for col in range(len(grid[row])):
            if robot_pos and (row, col) == robot_pos:
                line += '@'
            else:
                line += grid[row][col]
        print(line)
    print()


def solve_part1(filename):
    """
    Solve part 1: Simulate robot pushing boxes, return GPS sum.
    """
    print(f"Solving Day 15 Part 1 with {filename}")
    
    # Parse input
    grid, robot_pos, moves = parse_input(filename)
    print(f"Warehouse: {len(grid)}x{len(grid[0])}")
    print(f"Robot starts at: {robot_pos}")
    print(f"Total moves: {len(moves)}")
    
    # Simulate robot movement
    final_robot_pos = simulate_robot(grid, robot_pos, moves)
    print(f"Robot ends at: {final_robot_pos}")
    
    # Calculate GPS sum
    gps_sum = calculate_gps_sum(grid)
    
    return gps_sum


def widen_warehouse(grid):
    """
    Convert Part 1 warehouse to Part 2 format (double width).
    
    Transformations:
    # → ##
    . → ..
    O → []
    @ → @.
    """
    wide_grid = []
    
    for row in grid:
        wide_row = []
        for cell in row:
            if cell == '#':
                wide_row.extend(['#', '#'])
            elif cell == '.':
                wide_row.extend(['.', '.'])
            elif cell == 'O':
                wide_row.extend(['[', ']'])
            elif cell == '@':
                wide_row.extend(['@', '.'])
        wide_grid.append(wide_row)
    
    return wide_grid


def get_box_at(grid, row, col):
    """
    Get coordinates of complete box at given position.
    
    Returns:
        (left_row, left_col, right_row, right_col) or None if no box
    """
    cell = grid[row][col]
    
    if cell == '[':
        # This is left part of box
        return (row, col, row, col + 1)
    elif cell == ']':
        # This is right part of box
        return (row, col - 1, row, col)
    else:
        return None


def get_affected_boxes_vertical(grid, box_positions, dr):
    """
    Find all boxes that would be affected by pushing given boxes vertically.
    Uses BFS to find the complete set of affected boxes.
    
    Args:
        box_positions: set of (left_row, left_col) coordinates of boxes to push
        dr: direction (-1 for up, 1 for down)
    
    Returns:
        set of all affected box positions, or None if any box hits a wall
    """
    affected = set(box_positions)
    to_check = list(box_positions)
    
    while to_check:
        left_row, left_col = to_check.pop(0)
        
        # Check positions where this box would move
        new_left_row = left_row + dr
        new_right_row = left_row + dr
        
        # Check if box would hit walls
        if (grid[new_left_row][left_col] == '#' or 
            grid[new_right_row][left_col + 1] == '#'):
            return None  # Can't push - hits wall
        
        # Check for boxes in the way
        left_box = get_box_at(grid, new_left_row, left_col)
        right_box = get_box_at(grid, new_right_row, left_col + 1)
        
        for box in [left_box, right_box]:
            if box:
                box_pos = (box[0], box[1])  # Left position of found box
                if box_pos not in affected:
                    affected.add(box_pos)
                    to_check.append(box_pos)
    
    return affected


def can_push_boxes_part2(grid, start_row, start_col, dr, dc):
    """
    Check if boxes can be pushed in Part 2 (handles wide boxes).
    """
    if dc != 0:
        # Horizontal push - similar to Part 1 but handle [ and ]
        row, col = start_row, start_col
        
        while grid[row][col] in ['[', ']']:
            col += dc
        
        return grid[row][col] == '.'
    
    else:
        # Vertical push - complex case
        box = get_box_at(grid, start_row, start_col)
        if not box:
            return True
        
        box_pos = (box[0], box[1])  # Left position
        affected = get_affected_boxes_vertical(grid, {box_pos}, dr)
        
        return affected is not None


def push_boxes_part2(grid, start_row, start_col, dr, dc):
    """
    Push boxes in Part 2 (handles wide boxes).
    """
    if dc != 0:
        # Horizontal push
        if dc == 1:  # Moving right
            # Find end of box chain
            col = start_col
            while grid[start_row][col] in ['[', ']']:
                col += 1
            
            # Move boxes right (from end to start)
            while col > start_col:
                grid[start_row][col] = grid[start_row][col - 1]
                col -= 1
            grid[start_row][start_col] = '.'
            
        else:  # Moving left (dc == -1)
            # Find end of box chain
            col = start_col
            while grid[start_row][col] in ['[', ']']:
                col -= 1
            
            # Move boxes left (from end to start)
            while col < start_col:
                grid[start_row][col] = grid[start_row][col + 1]
                col += 1
            grid[start_row][start_col] = '.'
    
    else:
        # Vertical push
        box = get_box_at(grid, start_row, start_col)
        if not box:
            return
        
        box_pos = (box[0], box[1])
        affected = get_affected_boxes_vertical(grid, {box_pos}, dr)
        
        if affected:
            # Clear all affected boxes first
            for left_row, left_col in affected:
                grid[left_row][left_col] = '.'
                grid[left_row][left_col + 1] = '.'
            
            # Place boxes in new positions
            for left_row, left_col in affected:
                new_row = left_row + dr
                grid[new_row][left_col] = '['
                grid[new_row][left_col + 1] = ']'


def calculate_gps_sum_part2(grid):
    """
    Calculate GPS sum for Part 2 (use leftmost coordinate of each box).
    """
    total = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '[':  # Only count left part of box
                gps = 100 * row + col
                total += gps
    
    return total


def solve_part2(filename):
    """
    Solve part 2: Wider warehouse with double-width boxes.
    """
    print(f"Solving Day 15 Part 2 with {filename}")
    
    # Parse input (same as Part 1)
    grid, robot_pos, moves = parse_input(filename)
    
    # Widen the warehouse
    wide_grid = widen_warehouse(grid)
    wide_robot_pos = (robot_pos[0], robot_pos[1] * 2)  # Robot x-coord doubles
    
    print(f"Wide warehouse: {len(wide_grid)}x{len(wide_grid[0])}")
    print(f"Robot starts at: {wide_robot_pos}")
    
    # Simulate with Part 2 logic
    row, col = wide_robot_pos
    
    for move in moves:
        dr, dc = get_direction(move)
        new_row, new_col = row + dr, col + dc
        
        cell = wide_grid[new_row][new_col]
        
        if cell == '#':
            continue
        elif cell == '.':
            row, col = new_row, new_col
        elif cell in ['[', ']']:
            if can_push_boxes_part2(wide_grid, new_row, new_col, dr, dc):
                push_boxes_part2(wide_grid, new_row, new_col, dr, dc)
                row, col = new_row, new_col
    
    final_robot_pos = (row, col)
    print(f"Robot ends at: {final_robot_pos}")
    
    # Calculate GPS sum
    gps_sum = calculate_gps_sum_part2(wide_grid)
    
    return gps_sum


def main():
    """Run both parts with test and real data."""
    
    # Test data first
    print("=== Test Data ===")
    test_result1 = solve_part1('test.txt')
    print(f"Test Part 1: {test_result1}")
    print()
    
    # Real data
    print("=== Real Data ===")
    result1 = solve_part1('input.txt')
    print(f"Part 1: {result1}")
    
    # Part 2
    print("=== Test Data Part 2 ===")
    test_result2 = solve_part2('test.txt')
    print(f"Test Part 2: {test_result2}")
    print()
    
    result2 = solve_part2('input.txt')
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
