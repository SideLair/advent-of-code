#!/usr/bin/env python3
import re

def solve_part1(input_data):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, input_data)
    total = sum(int(x) * int(y) for x, y in matches)
    return total

def solve_part2(input_data):
    # Najdi pozice všech don't() a do()
    dont_positions = [m.start() for m in re.finditer(r"don't\(\)", input_data)]
    do_positions = [m.start() for m in re.finditer(r"do\(\)", input_data)]
    
    # Najdi všechny mul(x,y) s jejich pozicemi
    mul_pattern = r'mul\((\d+),(\d+)\)'
    mul_matches = [(m.start(), int(m.group(1)), int(m.group(2))) for m in re.finditer(mul_pattern, input_data)]
    
    def is_enabled(position):
        # Najdi poslední don't() před touto pozicí
        last_dont = max([pos for pos in dont_positions if pos < position], default=-1)
        # Najdi poslední do() před touto pozicí
        last_do = max([pos for pos in do_positions if pos < position], default=-1)
        
        # Pokud není žádné don't() nebo do(), je enabled (defaultně zapnuto)
        if last_dont == -1 and last_do == -1:
            return True
        # Pokud poslední instrukce byla do(), je enabled
        if last_do > last_dont:
            return True
        # Pokud poslední instrukce byla don't(), je disabled
        return False
    
    # Sečti pouze enabled mul() operace
    total = sum(x * y for pos, x, y in mul_matches if is_enabled(pos))
    return total

def main():
    # Test data
    test_data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
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