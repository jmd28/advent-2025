from inp import INPUT

reds = list(map(eval, INPUT.split("\n")))

def sort_points(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    left = min(x1, x2)
    top = min(y1, y2)
    right = max(x1, x2)
    bottom = max(y1, y2)
    return (left, top), (right, bottom)

def rect_area(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    w = abs(x2 - x1) + 1
    h = abs(y2 - y1) + 1
    return w * h

# part one
# get all the rectangles
rectangles = [sort_points(p1, p2) for i, p1 in enumerate(reds) for p2 in reds[i+1:]]
# sort by area
rectangles.sort(key=lambda points: rect_area(points[0], points[1]), reverse=True)
print(rect_area(*rectangles[0]))

# part two
# now we also care about the lines
# sort them to simplify the contains checking
lines = [sort_points(p1, p2) for p1, p2 in zip(reds, reds[1:] + reds[:1])]
# if we also sort the lines by size we'll find the bad rectangles faster
lines.sort(key=lambda points: rect_area(points[0], points[1]), reverse=True)

# find first valid rectangle
for (left, top), (right, bottom) in rectangles:
    invalid = False
    for (x1,y1), (x2,y2) in lines:
        # if the line starts inside the rect and ends inside the rectangle
        # its bad
        if x1 < right and y1 < bottom and x2 > left and y2 > top:
            invalid = True
            break
    if not invalid:
        print(rect_area((left,top), (right,bottom)))
        break
