inp = "aoc_day8_input.txt"

with open(inp, 'r') as f:
    grid = []
    letter_to_location = {}
    for l in f:
        clean_line = l.strip()
        grid.append([charr for charr in clean_line])
        row_num = len(grid) - 1
        for col_num, charr in enumerate(grid[-1]):
            if charr == ".":
                continue
            if charr in letter_to_location:
                letter_to_location[charr].append((row_num, col_num))
            else:
                letter_to_location[charr] = [(row_num, col_num)]

max_row = len(grid)
max_col = len(grid[-1])
def in_bounds(point):
    row_valid = point[0] >= 0 and point[0] < max_row
    col_valid = point[1] >= 0 and point[1] < max_col
    return row_valid and col_valid

# set of node locations: tuple of x,y coordinate = row,col coordinate
antinodes = set()

def make_candidates(start_node, dir_sign, slope_x, slope_y):
    mult = 1
    while True:
        new_candid = (start_node[0] + mult * dir_sign * slope_x, start_node[1] + mult * dir_sign * slope_y)
        if in_bounds(new_candid):
            antinodes.add(new_candid)
        else:
            break
        mult+=1 

for freq, locs in letter_to_location.items():
    for i in range(len(locs)):
        for j in range(i+1, len(locs)):
            node_1 = locs[i]
            node_2 = locs[j]

            # direction matters, so keep sign
            # Vector going from node 2 to node 1
            slope_x = node_1[0] - node_2[0]
            slope_y = node_1[1] - node_2[1]

            antinodes.add((node_1[0], node_1[1]))
            antinodes.add((node_2[0], node_2[1]))

            # antinode location candidates
            # Create candidates along the vectors until it goes out of bound 
            make_candidates(node_1, 1, slope_x, slope_y)
            make_candidates(node_2, -1, slope_x, slope_y)

print("Num antinodes: ", len(antinodes))
# antinode: perfectly in line with two iantenas of the same frequency
# but only when one antenna is twice as far away as the other antenna
# for any pair of same freq antennas, one on either side
# wont add antennas off the map

# slope = rise over run 
# x and y distance between the pair

# need to enumerate every pair 






