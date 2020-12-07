import re
from functools import cache


def parse_data():
    with open('C:\\Dev\\projects\\advent-of-code\\python\\day07\\input.txt') as f:
        data = f.read()

    data = [
        (
            ' '.join(line.split()[:2]),
            re.findall(r'(\d) (\w+ \w+) bag', line)
        )
        for line in data.splitlines()
    ]

    return {
        line[0]: {part[1]: int(part[0]) for part in line[1]} for line in data
    }

def part1(data):

    @cache
    def has_shiny(bag):
        if 'shiny gold' in data[bag]:
            return True
        return any(has_shiny(b) for b in data[bag])

    return sum(has_shiny(bag) for bag in data)

def part2(data):

    def count(bag):
        return sum(count(b) * x for b, x in data[bag].items()) + 1

    return count('shiny gold') -1


if __name__ == '__main__':
    data = parse_data()

    print(f'{part1(data) or "skipped"}')
    print(f'{part2(data) or "skipped"}')