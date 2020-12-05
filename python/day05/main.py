data = []

with open("C:\\Dev\\projects\\advent-of-code\\python\\day05\\input.txt") as f:
    for line in f.readlines():
        data.append(line)

seat = 0
for i in range(0, len(data)):
    row = int(data[i][:7].replace("F", "0").replace("B", "1"), 2)
    column = int(data[i][7:].replace("L", "0").replace("R", "1"), 2)
    data[i] = (row * 8) + column
    seat = max(data[i], seat)

missing = (((max(data) + min(data)) / 2) * (len(data) + 1)) - sum(data)

print(seat)
print(missing)