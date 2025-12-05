from inp import INPUT
from dataclasses import dataclass

@dataclass
class Range:
    start: int
    end: int

    def contains(self, number: int) -> bool:
        return self.start <= number and number <= self.end

    def __len__(self):
        return self.end - self.start + 1

def parse_range(line) -> Range:
    start, end = map(int, line.split("-"))
    return Range(start, end)

range_data, id_data = [it.split("\n") for it in INPUT.split("\n\n")]
ranges = [parse_range(line) for line in range_data]

# part one
def is_fresh(id):
    return any(r.contains(id) for r in ranges)

ids = list(map(int, id_data))
print(len([id for id in ids if is_fresh(id)]))

# part two
# first order them
ranges.sort(key=lambda r: r.start)
# merge
merged_ranges = [ranges.pop(0)]
while ranges:
    current = merged_ranges[-1]
    next = ranges.pop(0)
    # overlap case
    if next.start <= current.end and next.end > current.end:
        # update current, discard this range
        current.end = next.end
        continue
    # contains case
    if current.start <= next.start and next.end <= current.end:
        # discard this range
        continue
    # no overlap, both ranges needed
    merged_ranges.append(next)

print(sum(map(len, merged_ranges)))
