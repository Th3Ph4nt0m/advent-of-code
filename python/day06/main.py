with open("C:\\Dev\\projects\\advent-of-code\\python\\day06\\input.txt") as f:
    string = ""
    all = 0
    total = 0
    totalAll = 0
    for line in f.read().split("\n"):
        if line != "":
            string += line
            all += 1
        else:
            letters = [0] * 26
            for char in string:
                letters[ord(char) - ord("a")] += 1
            for letter in letters:
                total += (letter > 0)
                totalAll += (all == letter)
            string = ""
            all = 0

print(total)
print(totalAll)