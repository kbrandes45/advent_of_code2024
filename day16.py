inp = "aoc_day16_input.txt"

zeroes = []
start = None
end = None
with open(inp, 'r') as f:
    grid = []
    for l in f:
        clean_line = l.strip()
        grid.append([ww for ww in clean_line])
        for i, char in enumerate(clean_line):
            if char ==  "S":
                start = (len(grid) - 1, i)
            if char == "E":
                end = (len(grid) - 1, i)
            grid[-1].append(char)

col_max = len(grid[-1])
row_max = len(grid)

def get_options(x,y,ori, score):
    options = []
    if ori == "e":
        if y+1 < col_max and grid[x][y+1] != "#":
            options.append((x, y+1, ori, score + 1))
        options.append((x,y,"n",score+1000))
        options.append((x,y,"s",score+1000))
    if ori == "w":
        if y-1 >= 0 and grid[x][y-1] != "#":
            options.append((x, y-1, ori, score + 1))
        options.append((x,y,"n",score+1000))
        options.append((x,y,"s",score+1000))
    if ori == "n":
        if x-1 >= 0 and grid[x-1][y] != "#":
            options.append((x-1, y, ori, score + 1))
        options.append((x,y,"e",score+1000))
        options.append((x,y,"w",score+1000))
    if ori == "s":
        if x+1 < row_max and grid[x+1][y] != "#":
            options.append((x+1, y, ori, score + 1))
        options.append((x,y,"e",score+1000))
        options.append((x,y,"w",score+1000))
    return options

# track current location: (x,y,orientation, score)
queue_d = {
    (start[0], start[1], "e"): (0, [])
}
import copy
visisted = set()
ic = 0
found_paths = []
best_score = None
while len(queue_d) > 0:
    # select lowest cost
    # min_index, min_value = min(enumerate(queue), key=lambda t: t[1][-1])
    min_value, (min_score, path) = min(queue_d.items(), key=lambda t: t[1])
    visisted.add(min_value[:3])
    del queue_d[min_value]

    if min_value[0] == end[0] and min_value[1] == end[1] and (best_score is None or min_score <= best_score):
        print("found it")
        print(min_score)
        print(path)
        best_score = min_score
        found_paths.append(path)
        continue
        

    # now get new options!
    options = get_options(*min_value, min_score)
    for option in options:
        pt = option[:3]
        if pt in visisted:
            continue
        upd_path = copy.deepcopy(path)
        upd_path.append(pt)
        if pt in queue_d:
            # found a lower score way to reach that point
            if queue_d[pt][0] > option[3]:
                queue_d[pt] = (option[3], upd_path)
        else:
            queue_d[pt] = (option[3], upd_path)

    ic+=1

nodes = set()
print(found_paths)
for path in found_paths:
    for node in path:
        nodes.add(node[:2])
print("length: ", len(nodes))