import math
import functools

def countMass(n, sum):
    fuel = math.floor((float)(n) / 3)  - 2
    if (fuel > 0):
        sum = countMass(fuel, sum)
        return sum + fuel
    return 0

with open('input_day1.txt', 'r') as file:
    content = file.read().splitlines()

#print(content)

sum1 = 0
for item in content:
   sum1 += countMass(item, sum1)

print(sum1)

