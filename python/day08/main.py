import re



def part1():
    instructions = []
    with open("C:\\Dev\\projects\\advent-of-code\\python\\day08\\input.txt") as f:
        for line in f:
            instructions.append(line.strip())
    accu = 0
    count = 0
    list = []
    while count < len(instructions):
        if count not in list:
            list.append(count)
        else:
            print(accu)
            break
        instruction = instructions[count].split(' ')
        operation = instruction[0]
        operand = int(instruction[1])

        if operation == 'acc':
            accu += operand
            count += 1
        if operation == 'jmp':
            count += operand
        if operation == 'nop':
            count += 1


def part2():
    f = open("C:\\Dev\\projects\\advent-of-code\\python\\day08\\input.txt")
    lines = []

    for line in f:
        lines.append(line.strip())
    f.close()

    nop = []
    jmp = []

    for i in range(len(lines)):
        line = lines[i]
        x = line.split()
        command = x[0]
        if command == "nop":
            nop.append(i)
        elif command == "jmp":
            jmp.append(i)

    for index in jmp:
        visited = []

        current = 0
        accu = 0

        while(current not in visited) and (current < len(lines)):
            visited.append(current)
            instr = lines[current]
            instr_split = instr.split()
            command = instr_split[0]
            num = int(float(instr_split[1]))
            if (command == "nop") or (current == index):
                current += 1
            elif command == "acc":
                accu += num
                current += 1
            else: # jmp
                current += num
            if current == len(lines):
                print(accu)





if __name__ == '__main__':

    part1()
    part2()