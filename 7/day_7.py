from inp import INPUT

START = 'S'
SPLITTER = '^'

input_split = INPUT.split('\n')
WIDTH = len(input_split[0])

start = input_split[0].index(START)

# part one
beams = {start}
splits = 0
for line in input_split[1:]:
    split_beams = {beam for beam in beams if line[beam] == SPLITTER}
    splits += len(split_beams)
    # split them (the splitters are never at the edge so this is safe)
    for x in split_beams:
        beams.remove(x)
        beams.add(x - 1)
        beams.add(x + 1)
print(splits)

# part two
# keep track of how many timelines lead to each position
timeline_tracker = [int(idx == start) for idx in range(WIDTH)]
for line in input_split[1:]:
    for pos, n_timelines in enumerate(timeline_tracker):
        if line[pos] == SPLITTER:
            # each timeline forks at this point
            timeline_tracker[pos - 1] += n_timelines
            timeline_tracker[pos + 1] += n_timelines
            timeline_tracker[pos] = 0
# add up all the timelines produced
print(sum(timeline_tracker))
