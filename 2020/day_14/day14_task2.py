"""
--- Part Two ---
For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

For example, consider the following program:

mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
When this program goes to write to memory address 42, it first applies the bitmask:

address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X
After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)
Next, the program is about to write to memory address 26 with a different bitmask:

address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX
This results in an address with three floating bits, causing writes to eight memory addresses:

000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is 208.

Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?
"""
#03:04:18   6312

import re
from itertools import accumulate

def parse(data):
    """
    return [mask, (memory, value)]
    """
    programs = []
    
    for item in data:
        regex = re.match(r'^mask = ([01X]{36})$|^mem\[(\d+)\] = (\d+)$', item)

        if 'mask' in item:
            programs.append([regex.group(1)])
        elif 'mem' in item:
            #dont understant indexes of groups. Oh I got it :D 0 index - means original item :)
            programs[-1].append((int(regex.group(2)), int(regex.group(3))))

    return programs
    

def apply_mask(mask, address):
    address = format(address, '036b')
    result = ''

    for bit in range(0, 36):
        result += address[bit] if mask[bit] == '0' else mask[bit]
    return result
    

def generate_floating_addresses(mask):
    missing_count = mask.count('X')
    addresses = []

    for n in range(0, 2 ** missing_count):
        n_bit = format(n, '0' + str(missing_count) + 'b')
        n_bit_i = 0
        result = ''

        for bit in mask:
            if bit != 'X':
                result += bit
            else:
                result += n_bit[n_bit_i]
                n_bit_i += 1

        addresses.append(int(result, 2))
    
    return addresses


def fill_memory(mask, values):
    for value in values:
        for address in generate_floating_addresses(apply_mask(mask, value[0])):
            memory[address] = value[1]

memory = {}

file = open('input.txt', 'r')
data = [line.strip('\n') for line in file]
programs = parse(data)

for program in programs:
    fill_memory(program[0], [item for item in program[1:]])

print('Sum of memory values:', sum(memory.values()))