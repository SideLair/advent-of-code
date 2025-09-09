#!/usr/bin/env python3

def decode_disk_map(disk_map):
    """
    Decode the disk map string into a list representing the disk layout.
    
    The input alternates between file sizes and free space sizes.
    Files are numbered starting from 0.
    Free spaces are represented by '.' (dot).
    
    Example: "12345" -> "0..111....22222"
    - File 0: size 1 -> "0"
    - Free space: size 2 -> ".."
    - File 1: size 3 -> "111"
    - Free space: size 4 -> "...."
    - File 2: size 5 -> "22222"
    """
    disk = []
    file_id = 0
    is_file = True  # Start with file, then alternate with free space
    
    for char in disk_map:
        size = int(char)
        
        if is_file:
            # Add file blocks with current file ID
            disk.extend([str(file_id)] * size)
            file_id += 1
        else:
            # Add free space blocks
            disk.extend(['.'] * size)
        
        is_file = not is_file  # Alternate between file and free space
    
    return disk

def compact_disk(disk):
    """
    Compact the disk by moving file blocks from the end to fill free spaces from the left.
    
    Algorithm:
    1. Find the leftmost free space (.)
    2. Find the rightmost file block (not .)
    3. Move the file block to the free space
    4. Repeat until no more moves are possible
    """
    disk = disk.copy()  # Don't modify the original
    
    left = 0
    right = len(disk) - 1
    
    while left < right:
        # Find next free space from left
        while left < len(disk) and disk[left] != '.':
            left += 1
        
        # Find next file block from right
        while right >= 0 and disk[right] == '.':
            right -= 1
        
        # If we found both and they haven't crossed, swap them
        if left < right:
            disk[left] = disk[right]
            disk[right] = '.'
            left += 1
            right -= 1
    
    return disk

def calculate_checksum(disk):
    """
    Calculate the filesystem checksum.
    
    Checksum = sum of (position * file_id) for all file blocks.
    Free spaces (.) are ignored in the calculation.
    """
    checksum = 0
    
    for position, block in enumerate(disk):
        if block != '.':
            file_id = int(block)
            checksum += position * file_id
    
    return checksum

def solve_part1(input_data):
    """
    Solve part 1: Decode disk map, compact it, and calculate checksum.
    
    Process:
    1. Decode the input string into disk representation
    2. Compact the disk by moving files from right to left
    3. Calculate and return the checksum
    """
    disk_map = input_data.strip()
    
    # Step 1: Decode the disk map
    disk = decode_disk_map(disk_map)
    
    # Step 2: Compact the disk
    compacted_disk = compact_disk(disk)
    
    # Step 3: Calculate checksum
    checksum = calculate_checksum(compacted_disk)
    
    return checksum

def find_files(disk):
    """
    Find all files in the disk and return their information.
    Returns a dictionary: {file_id: (start_pos, size)}
    """
    files = {}
    i = 0
    
    while i < len(disk):
        if disk[i] != '.':
            file_id = int(disk[i])
            start_pos = i
            size = 0
            
            # Count consecutive blocks of the same file
            while i < len(disk) and disk[i] == str(file_id):
                size += 1
                i += 1
            
            files[file_id] = (start_pos, size)
        else:
            i += 1
    
    return files

def find_free_space(disk, required_size, max_pos):
    """
    Find the leftmost free space of at least required_size before max_pos.
    Returns the starting position or None if not found.
    """
    i = 0
    
    while i < max_pos:
        if disk[i] == '.':
            # Found start of free space, count consecutive dots
            start_pos = i
            free_size = 0
            
            while i < max_pos and disk[i] == '.':
                free_size += 1
                i += 1
            
            # Check if this free space is large enough
            if free_size >= required_size:
                return start_pos
        else:
            i += 1
    
    return None

def compact_whole_files(disk):
    """
    Compact the disk by moving whole files from right to left.
    
    Algorithm:
    1. Find all files and their positions/sizes
    2. Process files from highest ID to lowest
    3. For each file, try to find leftmost free space that fits
    4. If found, move the entire file there
    """
    disk = disk.copy()  # Don't modify the original
    files = find_files(disk)
    
    # Process files from highest ID to lowest
    for file_id in sorted(files.keys(), reverse=True):
        start_pos, size = files[file_id]
        
        # Try to find free space to the left of current position
        new_pos = find_free_space(disk, size, start_pos)
        
        if new_pos is not None:
            # Move the file to the new position
            # First, clear the old position
            for i in range(start_pos, start_pos + size):
                disk[i] = '.'
            
            # Then, place the file at the new position
            for i in range(new_pos, new_pos + size):
                disk[i] = str(file_id)
    
    return disk

def solve_part2(input_data):
    """
    Solve part 2: Decode disk map, compact whole files, and calculate checksum.
    
    Process:
    1. Decode the input string into disk representation
    2. Compact the disk by moving whole files from right to left
    3. Calculate and return the checksum
    """
    disk_map = input_data.strip()
    
    # Step 1: Decode the disk map
    disk = decode_disk_map(disk_map)
    
    # Step 2: Compact whole files
    compacted_disk = compact_whole_files(disk)
    
    # Step 3: Calculate checksum
    checksum = calculate_checksum(compacted_disk)
    
    return checksum

def main():
    # Test with the example from your description: "12345"
    test_simple = "12345"
    print("Simple test (12345):")
    
    # Decode step by step for demonstration
    disk = decode_disk_map(test_simple)
    print(f"Decoded: {''.join(disk)}")
    
    compacted = compact_disk(disk)
    print(f"Compacted: {''.join(compacted)}")
    
    checksum = calculate_checksum(compacted)
    print(f"Checksum: {checksum}")
    print()
    
    # Test with the provided test data
    with open('test.txt', 'r') as f:
        test_data = f.read().strip()
    
    print("Test data:")
    part1_result = solve_part1(test_data)
    print(f"Part 1: {part1_result}")
    print()
    
    # Real data
    with open('input.txt', 'r') as f:
        input_data = f.read()
    
    print("Real data:")
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")

if __name__ == "__main__":
    main()