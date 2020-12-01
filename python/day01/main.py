numbers = []

with open("C:\\Dev\\projects\\advent-of-code\\java\\src\\day01\\input.txt") as f:
    numbers = list(map(int, f.readlines()))
# part 1
for i in numbers:
    for j in numbers:
        if i+j == 2020:
            print(i*j)

# part 2
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i+j+k == 2020:
                print(i*j*k)