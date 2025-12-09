from dataclasses import dataclass
from functools import reduce
import math
import operator
from inp import INPUT

@dataclass(frozen=True)
class Box:
    id: int
    x: int
    y: int
    z: int

MAGIC_NUMBER = 1000
box_data = [tuple(map(int, line.split(","))) for line in INPUT.split("\n")]
n_boxes = len(box_data)

def all_the_edges():
    edges = []
    for m in range(n_boxes):
        for n in range(m + 1, n_boxes):
            (x1, y1, z1) = box_data[m]
            (x2, y2, z2) = box_data[n]
            dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
            edges.append((Box(m, x1, y1, z1), Box(n, x2, y2, z2), dist))
    # sort them by size
    edges.sort(key=lambda x: x[2])
    return edges

def part_one(edges):
    # build the circuits
    circuits = []
    for _ in range(MAGIC_NUMBER):
        # grab the best pair of boxes
        best_start, best_end, _best_dist = edges.pop(0)
        new_circuit = set([best_start, best_end])
        # if any sets contain the chosen boxes we merge them
        to_merge = [c for c in circuits if c & new_circuit]
        for c in to_merge:
            new_circuit |= c
            circuits.remove(c)
        circuits.append(new_circuit)

    top_three = sorted(map(len, circuits), reverse=True)[:3]
    print(reduce(operator.mul, top_three))

def part_two(edges):
    circuits = []
    # as part one, but just keep going until we have one big set
    while edges:
        # grab the best pair of boxes
        best_start, best_end, _best_dist = edges.pop(0)
        new_circuit = set([best_start, best_end])
        # if any sets contain the chosen boxes we merge them
        to_merge = [c for c in circuits if c & new_circuit]
        for c in to_merge:
            new_circuit |= c
            circuits.remove(c)
        circuits.append(new_circuit)
        if any(len(c) == MAGIC_NUMBER for c in circuits):
            return best_start.x * best_end.x

edges = all_the_edges()
print(part_one(edges[:]))
print(part_two(edges[:]))
