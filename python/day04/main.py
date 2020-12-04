import string

data = []

with open("C:\\Dev\\projects\\advent-of-code\\python\\day04\\input.txt") as f:
    record = []
    for line in f.read().split("\n"):
        if line != '':
            for element in line.split(" "):
                record.append(element)
        else:
            data.append(record)
            record = []

valid = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

for record in data:
    found = [0, 0, 0, 0, 0, 0, 0, 1]

    for element in record:
        found[fields.index(element.split(":")[0])] += 1
    if 0 not in found:
        # use for part 1        valid += 1
        good = True
        for element in record:
            left = element.split(":")[0]
            right = element.split(":")[1]
            if left == "byr":
                if((int(right) < 1920) or (int(right) > 2002)):
                    good = False
            elif left == "iyr":
                if ((int(right) < 2010) or (int(right) > 2020)):
                    good = False
            elif left == "eyr":
                if ((int(right) < 2020) or (int(right) > 2030)):
                    good = False
            elif left == "hgt":
                measure = right[-2::]
                if measure == "cm":
                    value = int(right.split("cm")[0])
                    if value < 150 or value > 193:
                        good = False
                elif measure == "in":
                    value = int(right.split("in")[0])
                    if value < 59 or value > 76:
                        good = False
                else:
                    good = False
            elif left == "hcl":
                if len(right) != 7 or right[0] != "#":
                    good = False
                for x in right[1::]:
                    if x not in string.hexdigits:
                        good = False
            elif left == "ecl":
                if right not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    good = False
            elif left == "pid":
                if len(right) != 9 or right.isnumeric() == False:
                    good = False

        if good == True:
            valid += 1

print(str(valid))
