with open('C:\\Dev\\projects\\advent-of-code\\python\\day11\\input.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    return [list(line) for line in data.split('\n')]


def get_state():
    occupied, empty = set(), set()
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '#':
                occupied.add((i, j))
            if grid[i][j] == 'L':
                empty.add((i, j))
    return occupied, empty


def check_seat_one(seat_pos, occupied):
    x, y = seat_pos
    count = 0
    for dx, dy in [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, 1), (0, -1), (-1, -1), (1, -1)]:
        if (x+dx, y+dy) in occupied:
            count += 1
    return count


def part1():
    occupied, empty = occ.copy(), emp.copy()
    while True:
        occupy, deoccupy = set(), set()
        for seat in empty:
            if check_seat_one(seat, occupied) == 0:
                occupy.add(seat)
        for seat in occupied:
            if check_seat_one(seat, occupied) >= 4:
                deoccupy.add(seat)
        if not occupy and not deoccupy:
            break
        occupied = (occupied - deoccupy) | occupy
        empty = (empty - occupy) | deoccupy
    print(len(occupied))


def check_seat_two(seat_pos, occupied):
    x, y = seat_pos
    count = 0
    for dx, dy in [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, 1), (0, -1), (-1, -1), (1, -1)]:
        cur_x, cur_y = x+dx, y+dy
        while 0 <= cur_x < r and 0 <= cur_y < c and grid[cur_x][cur_y] == '.':
            cur_x += dx
            cur_y += dy
        if (cur_x, cur_y) in occupied:
            count += 1
    return count


def part2():
    occupied, empty = occ.copy(), emp.copy()
    while True:
        occupy, deoccupy = set(), set()
        for seat in empty:
            if check_seat_two(seat, occupied) == 0:
                occupy.add(seat)
        for seat in occupied:
            if check_seat_two(seat, occupied) >= 5:
                deoccupy.add(seat)
        if not occupy and not deoccupy:
            break
        occupied = (occupied - deoccupy) | occupy
        empty = (empty - occupy) | deoccupy
    print(len(occupied))


grid = parse_input(data)
r, c = len(grid), len(grid[0])
occ, emp = get_state()

part1()
part2()