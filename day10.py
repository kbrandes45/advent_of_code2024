inp = "aoc_day10_input.txt"

zeroes = []
with open(inp, 'r') as f:
    grid = []
    for l in f:
        clean_line = l.strip()
        grid.append([])
        for i, char in enumerate(clean_line):
            if char ==  "0":
                zeroes.append((len(grid) - 1, i))
            if char == ".":
                char = 100
            grid[-1].append(int(char))

# dfs from every zero 
changes = [(0,1), (0, -1), (1, 0), (-1, 0)]
all_zeros = 0
ratings = 0
for zero in zeroes:
    distinct_full_paths = 0
    queue_locs = [(zero, 0)]
    unique_reachable_nines = set()
    while len(queue_locs) > 0:
        (loc, state) = queue_locs.pop(0)
        for change in changes:
            new_loc = (loc[0]+change[0], loc[1]+change[1])
            if new_loc[0] < 0 or new_loc[0] >= len(grid):
                continue
            if new_loc[1] < 0 or new_loc[1] >= len(grid[-1]):
                continue


            new_state = grid[new_loc[0]][new_loc[1]]
            if new_state == 9 and state == 8:
                unique_reachable_nines.add(new_loc)
                distinct_full_paths += 1
                continue

            if state + 1 != new_state:
                continue

            # not tracking visited atm because the incrementing counter should keep out 
            # any seen states. 
            queue_locs.append((new_loc, new_state))
    print("trailhead ", len(unique_reachable_nines), " rating ", distinct_full_paths)
    all_zeros += len(unique_reachable_nines)
    ratings += distinct_full_paths

print("all pathes: ", all_zeros," and ratings: ", ratings)