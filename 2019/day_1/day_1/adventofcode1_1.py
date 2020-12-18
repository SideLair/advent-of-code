import math

def countMass():
    with open('input_day1.txt', 'r') as file:
        content = file.read().splitlines()

    #print(content)

    sum1 = 0
    for item in content:
        sum1 += math.floor((float)(item) / 3)  - 2

    print('result =', sum1)

countMass()

