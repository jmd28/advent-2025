from inp import INPUT

ROLL = '@'
EMPTY = '.'

grid = list(map(list, INPUT.split("\n")))
y_bounds = range(len(grid))
x_bounds = range(len(grid[0]))

def is_roll(x, y):
    if x not in x_bounds: return False
    if y not in y_bounds: return False
    return grid[y][x] == ROLL

def is_accessible(x, y):
    neighbours = [(x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (not(dx == 0 and dy == 0))]
    roll_neighbours = sum(int(is_roll(_x, _y)) for (_x, _y) in neighbours)
    return roll_neighbours < 4

# part one
accessible = 0
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == ROLL and is_accessible(x, y):
            accessible += 1
print(accessible)

# part two
removed = 0
while True:
    grid_modified = False
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == ROLL and is_accessible(x, y):
                grid[y][x] = EMPTY
                removed += 1
                grid_modified = True
    if not grid_modified:
        break
print(removed)
