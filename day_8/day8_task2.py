"""
--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
"""
#01:19:31   7670


def get_executed(instructions):
    total_acc = 0
    i = 0
    executed_instructions = []
    
    while(i < len(instructions)):
        ins, value = instructions[i].split(' ')

        if ins == 'acc':
            total_acc += int(value)
            i += 1
        elif ins == 'jmp':
            i += int(value)
        elif ins == 'nop':
            i += 1

        if i not in executed_instructions:
            executed_instructions.append(i)
            if i == len(instructions) - 1:
                print("Index: {}, Total_acc: {}".format(i, total_acc))
                return i
        else:
            return i


def find_corrupted_instruction(instructions):
    potencial_danger_instructions = ['jmp', 'nop']
    
    for _ in range(0, len(potencial_danger_instructions)):
        for i in range(0, len(instructions)):
            ins = instructions[i][:3]

            if ins == potencial_danger_instructions[0]:
                instructions[i] = instructions[i].replace(ins, potencial_danger_instructions[1])

                if get_executed(instructions) == len(instructions) - 1:
                    return

                instructions[i] = instructions[i].replace(potencial_danger_instructions[1], ins)
        
        tmp = potencial_danger_instructions[0]
        potencial_danger_instructions[0] = potencial_danger_instructions[1]
        potencial_danger_instructions[1] = tmp


file = open('input.txt', 'r')
instructions = [line.strip('\n') for line in file]
find_corrupted_instruction(instructions)