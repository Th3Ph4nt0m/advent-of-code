def part1():
    data = []
    with open("C:\\Dev\\projects\\advent-of-code\\python\\day10\\input.txt") as f:
        data = [int(x) for x in f.readlines()]

    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    diffs = [0] * 4
    for i in range(1, len(data)):
        d = data[i] - data[i-1]
        diffs[d] += 1

    ans = diffs[1] * diffs[3]
    print(str(ans))

def part2():
    with open("C:\\Dev\\projects\\advent-of-code\\python\\day10\\input.txt") as f:
        data = [int(x) for x in f.readlines()]

    data.append(0)
    data.append(max(data) + 3)
    data.sort()

    paths = [0] * (max(data) + 1)
    paths[0] = 1

    for i in range(1, max(data) + 1):
        for x in range(1, 4):
            if (i - x) in data:
                paths[i] += paths[i - x]
    print(str(paths[-1]))

part1()
part2()