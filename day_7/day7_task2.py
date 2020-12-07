"""
--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""

class Bag:
    def __init__(self, color, inner_bags):
        self.color = color
        self.inner_bags = inner_bags


def check_bag(bag):
    colors = bag.replace(' contain', ',').replace(' bag,', ' bag.').replace(' bags,', ' bag.').replace(' bags.', ' bag.').split(' bag.')
    inner_bags = {}
    for i in range(1, len(colors) - 1):
        inner_bags[colors[i][3:]] = colors[i][1] if colors[i][1] != 'n' else 0

    return Bag(colors[0], inner_bags)


def bag_count(bag, bags):
    sum = 0

    for inner_bag in bag.inner_bags:
        if inner_bag == ' other':
            return 1
        else:
            for b in bags:
                if b.color == inner_bag:
                    sum += int(bag.inner_bags[inner_bag] * bag_count(b, bags))
    return 1 + sum


def sum_bags(bags):
    good_bags = [Bag('shiny gold', {'light chartreuse' : 2, 'drab black' : 2, 'bright orange' : 1, 'shiny teal' : 1})]
    #good_bags = [Bag('shiny gold', {'dark red' : 2})]

    for good_bag in good_bags:
        for color in good_bag.inner_bags:
            for bag in bags:
                if color == bag.color and bag not in good_bags:
                    good_bags.append(bag)

    
    print('Bag count is:', bag_count(good_bags[0], good_bags) - 1)   


file = open('input.txt', 'r')
bags = [check_bag(line.strip('\n')) for line in file]

sum_bags(bags)