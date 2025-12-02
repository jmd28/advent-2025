# lets abuse itertools
from itertools import batched
from inp import INPUT

def is_valid_part1(id):
    # early exit for odd lengths
    if len(id) % 2 != 0: return True
    # else chop the string up
    middle = len(id) // 2
    left, right = id[:middle], id[middle:]
    return left != right

def is_valid_part2(id):
    middle = len(id) // 2
    # check all substrings that divide the string evenly
    for sub_length in range(middle, 0, -1):
        if len(id) % sub_length == 0:
            # all chunks are the same => not valid
            if len(set(batched(id, sub_length))) == 1:
                return False
    return True

ids = []
for id_range in INPUT.split(","):
    start, end = map(int, id_range.split("-"))
    ids += map(str, range(start, end + 1))

print(sum(int(id) for id in ids if not is_valid_part1(id)))
print(sum(int(id) for id in ids if not is_valid_part2(id)))
