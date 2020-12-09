def isValid(l, index, pre):
    for i in range(index - pre, index - 1):
        for j in range(i + 1, index):
            if l[i] + l[j] == l[index]:
                return True
    return False

data = []
with open("C:\\Dev\\projects\\advent-of-code\\python\\day09\\input.txt") as f:
    data = [int(x) for x in f.readlines()]

index = 225
while isValid(data, index, 25) == True:
    index += 1
search = data[index]
print(str(search))

for low in range(0, len(data)):
    value = data[low]
    for high in range(low + 1, len(data)):
        value += data[high]
        if value == search:
            low_v = min(data[low:high+1])
            high_v = max(data[low:high+1])
            print(str(low_v + high_v))