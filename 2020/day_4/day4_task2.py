"""
--- Part Two ---
The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
"""
#05:26:16  19497

import re
from collections import OrderedDict

def validate_passport(passport):
    if (len(passport) == 8) or (len(passport) == 7 and 'cid' not in passport):
        print('OK délka/cin')

        if 1920 <= int(passport['byr']) <= 2002:
            print('OK byr')

            if 2010 <= int(passport['iyr']) <= 2020:
                print('OK iyr')

                if 2020 <= int(passport['eyr']) <= 2030:
                    print('OK eyr')

                    try:
                        number = int(passport['hgt'][:-2])
                    except:
                        return False
                    unit = passport['hgt'][-2:]
                    print(number, unit)
                    if (unit == 'cm' and (150 <= number <= 193)) or (unit == 'in' and (59 <= number <= 76)):
                        print('OK hgt')

                        reg = re.match(r'[#][0-9a-f]{6}', passport['hcl'])
                        print(passport['hcl'], reg)
                        if reg != None:
                            print('OK hcl')

                            if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                print('OK ecl')

                                try:
                                    number = int(passport['pid'])
                                    if 0 < number < 1_000_000_000 and len(passport['pid']) == 9:
                                        print('OK pid')
                                        return True
                                except:
                                    return False                                        

    return False 


def parse_input(input):
    valids = 0
    passports = []
    passport = {}
    for line in input:
        items = line.rstrip('\n').split(' ')
        #print(items)
        if items[0] == '':

            if validate_passport(passport):
                passports.append(OrderedDict(sorted(passport.items())))
                valids += 1
            #print(passport, len(passport), 'cid' in passport, valids)

            passport = {}
            print('\n\n')
        else:
            for item in items:
                if item != '':
                    key, value = item.split(':')
                    passport[key] = value


    if validate_passport(passport):
        passports.append(passport)
        valids += 1
    #print(passport, len(passport), 'cid' in passport, valids)

    passport = {}

    return passports


file = open('input.txt', 'r')
passports = parse_input(file)

print('Valid passports:', len(passports))

