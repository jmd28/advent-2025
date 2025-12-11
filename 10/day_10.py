from collections import deque
from dataclasses import dataclass
from typing import List, Set
from inp import INPUT

ON = "#"
OFF = "."
lines = INPUT.split("\n")

def toggle(c): return ON if c== OFF else OFF

@dataclass(frozen=True)
class SearchState:
    lights: str
    buttons_pressed: Set[int]

def parse_wiring(s):
    return set(map(int, s[1:-1].split(",")))

def push_buttons(goal, wiring) -> SearchState: # type: ignore
    visited = set()
    all_buttons = set(range(len(wiring)))
    # push buttons until done
    queue = deque([SearchState(OFF * len(goal), set())])
    while queue:
        v = queue.popleft()
        visited.add(v.lights)
        if v.lights == goal:
            return v
        for button in all_buttons - v.buttons_pressed:
            new_lights = "".join([toggle(c) if i in wiring[button] else c for i, c in enumerate(v.lights)])
            next_state = SearchState(new_lights, v.buttons_pressed | {button})
            if next_state.lights not in visited:
                queue.append(next_state)
    print("nothing doing")

# run for each machine
presses = 0
for line in lines:
    lights = line[:line.index('(')].strip()[1:-1]
    wiring = list(map(parse_wiring, line[line.index('('):line.index('{')].strip().split()))
    search_result = push_buttons(lights, wiring)
    presses += len(search_result.buttons_pressed)
print(presses)

# I never got part two for today, BFS and DFS time out...
# I think it's probably a linear maths answer given how it all just sums
