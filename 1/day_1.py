from inp import INPUT

def is_zero(position): return int(position == 0)

position = 50
password_part1 = 0
password_part2 = 0

for line in INPUT.split('\n'):
    amount = int(line[1:])
    direction = -1 if line[0] == 'L' else 1
    for _ in range(0, amount):
        position += direction
        position %= 100
        password_part2 += is_zero(position)
    password_part1 += is_zero(position)

print(password_part1)
print(password_part2)
