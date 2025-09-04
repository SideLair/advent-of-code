#!/usr/bin/env python3

def solve_part1(input_data):
    lines = input_data.strip().split('\n')
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])
    
    all_strings = []
    
    # Horizontal strings (rows)
    for row in grid:
        all_strings.append(''.join(row))
    
    # Vertical strings (columns)  
    for col in range(cols):
        all_strings.append(''.join(grid[row][col] for row in range(rows)))
    
    # Main diagonals (\) - top-left to bottom-right
    # Starting from top row
    for start_col in range(cols):
        diagonal = []
        row, col = 0, start_col
        while row < rows and col < cols:
            diagonal.append(grid[row][col])
            row += 1
            col += 1
        all_strings.append(''.join(diagonal))
    
    # Starting from left column (excluding top-left corner already covered)
    for start_row in range(1, rows):
        diagonal = []
        row, col = start_row, 0
        while row < rows and col < cols:
            diagonal.append(grid[row][col])
            row += 1
            col += 1
        all_strings.append(''.join(diagonal))
    
    # Anti-diagonals (/) - top-right to bottom-left
    # Starting from top row
    for start_col in range(cols):
        diagonal = []
        row, col = 0, start_col
        while row < rows and col >= 0:
            diagonal.append(grid[row][col])
            row += 1
            col -= 1
        all_strings.append(''.join(diagonal))
    
    # Starting from right column (excluding top-right corner already covered)
    for start_row in range(1, rows):
        diagonal = []
        row, col = start_row, cols - 1
        while row < rows and col >= 0:
            diagonal.append(grid[row][col])
            row += 1
            col -= 1
        all_strings.append(''.join(diagonal))
    
    # Count XMAS and SAMX in all strings
    count = 0
    for string in all_strings:
        count += string.count("XMAS")
        count += string.count("SAMX")
    
    return count

def solve_part2(input_data):
    lines = input_data.strip().split('\n')
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    # Look for X-MAS pattern: two MAS crossing at center 'A'
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == 'A':
                # Extract both diagonals through this 'A'
                diagonal1 = grid[row-1][col-1] + grid[row][col] + grid[row+1][col+1]  # \ diagonal
                diagonal2 = grid[row-1][col+1] + grid[row][col] + grid[row+1][col-1]  # / diagonal
                
                # Both diagonals must form MAS or SAM
                if (diagonal1 == "MAS" or diagonal1 == "SAM") and (diagonal2 == "MAS" or diagonal2 == "SAM"):
                    count += 1
    
    return count

def main():
    # Test data
    test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    
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