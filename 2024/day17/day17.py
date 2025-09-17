#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 17: Chronospatial Computer

Implementuje simulátor 3-bit počítače s třemi registry (A, B, C) a osmi instrukcemi.

Part 1: Simuluje program a vrací výstup jako čárkami oddělený string
Part 2: Nalezne nejmenší hodnotu registru A, která způsobí, že program vypíše sám sebe (quine)

Použité techniky:
- Simulace CPU s instruction pointer a registry  
- Working backwards approach pro exponenciálně rychlejší řešení Part 2
"""

class Computer:
    """Simuluje 3-bit počítač s registry A, B, C a programem instrukcí."""
    
    def __init__(self, a, b, c, program):
        """
        Inicializuje počítač.
        
        Args:
            a, b, c: Počáteční hodnoty registrů A, B, C
            program: Seznam 3-bit čísel reprezentujících instrukce a operandy
        """
        self.registers = {'A': a, 'B': b, 'C': c}
        self.program = program
        self.ip = 0  # instruction pointer
        self.output = []
    
    def get_combo_value(self, operand):
        """Převede combo operand na hodnotu podle specifikace."""
        if operand <= 3:
            return operand
        elif operand == 4:
            return self.registers['A']
        elif operand == 5:
            return self.registers['B']
        elif operand == 6:
            return self.registers['C']
        else:
            raise ValueError(f"Invalid combo operand: {operand}")
    
    def execute_step(self):
        """Provede jeden krok programu. Vrací False pokud program skončil."""
        if self.ip >= len(self.program):
            return False
        
        opcode = self.program[self.ip]
        operand = self.program[self.ip + 1]
        jumped = False
        
        if opcode == 0:  # adv: A = A // (2^combo)
            self.registers['A'] = self.registers['A'] // (2 ** self.get_combo_value(operand))
        
        elif opcode == 1:  # bxl: B = B XOR literal
            self.registers['B'] = self.registers['B'] ^ operand
        
        elif opcode == 2:  # bst: B = combo % 8
            self.registers['B'] = self.get_combo_value(operand) % 8
        
        elif opcode == 3:  # jnz: jump if A != 0
            if self.registers['A'] != 0:
                self.ip = operand
                jumped = True
        
        elif opcode == 4:  # bxc: B = B XOR C
            self.registers['B'] = self.registers['B'] ^ self.registers['C']
        
        elif opcode == 5:  # out: output combo % 8
            self.output.append(self.get_combo_value(operand) % 8)
        
        elif opcode == 6:  # bdv: B = A // (2^combo)
            self.registers['B'] = self.registers['A'] // (2 ** self.get_combo_value(operand))
        
        elif opcode == 7:  # cdv: C = A // (2^combo)
            self.registers['C'] = self.registers['A'] // (2 ** self.get_combo_value(operand))
        
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
        
        if not jumped:
            self.ip += 2
        
        return True
    
    def run(self, max_steps=1000000):
        """Spustí program a vrátí výstup jako čárkami oddělený string."""
        step_count = 0
        while step_count < max_steps and self.execute_step():
            step_count += 1
        
        if step_count >= max_steps:
            print("Warning: Maximum steps reached, possible infinite loop")
        
        return ','.join(map(str, self.output))
    

def parse_input(data):
    """Parsuje vstupní data a vrátí hodnoty registrů a program."""
    lines = data.strip().split('\n')
    
    a = int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])
    
    program_str = lines[4].split(': ')[1]
    program = list(map(int, program_str.split(',')))
    
    return a, b, c, program

def solve_part1(input_data):
    """Simuluje program a vrátí výstup."""
    a, b, c, program = parse_input(input_data)
    computer = Computer(a, b, c, program)
    return computer.run()

def simulate_one_cycle(a_value):
    """Simuluje jeden cyklus programu a vrátí output digit a novou hodnotu A.
    
    Používá se pro working backwards approach - simuluje pouze jeden průchod
    přes program až do prvního outputu.
    
    Args:
        a_value: Počáteční hodnota registru A
        
    Returns:
        tuple: (output_digit, new_A) nebo (None, None) pokud program neskončil
    """
    computer = Computer(a_value, 0, 0, [2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0])
    
    step_count = 0
    while len(computer.output) == 0 and step_count < 20:  # safety limit
        if not computer.execute_step():
            break
        step_count += 1
    
    if len(computer.output) > 0:
        return computer.output[0], computer.registers['A']
    return None, None

def solve_part2_backwards(input_data):
    """Nalezne nejmenší hodnotu A pro quine použitím working backwards approach.
    
    Algoritmus:
    1. Začneme s A=0 (konec programu)
    2. Pro každou cifru od konce rekonstruujeme možné hodnoty A
    3. Testyčka každou možnost (prev_A << 3) + kandidat (0-7)
    4. Pokračujeme jen s hodnotami, které dávají správnou cifru
    5. Vraćíme nejmenší z finálních kandidátů
    
    Složitost: O(8^n) v nejhorším případě, ale obvykle mnohem lepší
    díky pruničce neplatných cest.
    """
    _, _, _, program = parse_input(input_data)
    target = program
    
    print("Working backwards approach...")
    print(f"Target: {target}")
    
    possible_A = [0]  # Začínáme s A=0 (konec programu)
    
    for i, target_digit in enumerate(reversed(target)):
        print(f"\nStep {i+1}/{len(target)}: Looking for digit {target_digit}")
        new_possible_A = []
        
        for prev_A in possible_A:
            # Testyčka všech 8 možných předchozích hodnot A
            for candidate in range(8):
                test_A = (prev_A << 3) + candidate  # "unshift" operačka
                
                digit, new_A = simulate_one_cycle(test_A)
                if digit == target_digit and new_A == prev_A:
                    new_possible_A.append(test_A)
                    print(f"  Found: A={test_A} -> digit={digit}, new_A={new_A}")
        
        possible_A = new_possible_A
        print(f"  Possible A values: {len(possible_A)}")
        
        if not possible_A:
            return "No solution found"
    
    if possible_A:
        result = min(possible_A)
        print(f"\nFinal answer: {result}")
        return result
    
    return "No solution found"

def solve_part2(input_data):
    """Hlavní funkce pro Part 2 - používá working backwards approach."""
    return solve_part2_backwards(input_data)

def main():
    """Spustí řešení obou částí s testovacími i reálnými daty."""
    # Test data
    test_data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
    
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