#!/usr/bin/env python3

def solve_part1(input_data):
    lines = input_data.strip().split('\n')
    
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    left_list.sort()
    right_list.sort()
    
    total_distance = 0
    for i in range(len(left_list)):
        distance = abs(left_list[i] - right_list[i])
        total_distance += distance
    
    return total_distance


def solve_part2(input_data):
    lines = input_data.strip().split('\n')
    
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    distinct_left = list(set(left_list))
    
    similarity_score = 0
    for num in distinct_left:
        count_in_right = right_list.count(num)
        similarity_score += num * count_in_right
    
    return similarity_score


def main():
    test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""
    
    print("Test data:")
    print(f"Part 1: {solve_part1(test_data)}")
    print(f"Part 2: {solve_part2(test_data)}")
    print()
    
    with open('input.txt', 'r') as f:
        input_data = f.read()
    
    print("Real data:")
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")


if __name__ == "__main__":
    main()