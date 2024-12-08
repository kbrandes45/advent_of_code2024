inp = "aoc_day6_input.txt"

person = [">","<","^","v"]
person_to_new_dir = {
    ">":"v",
    "v":"<",
    "<":"^",
    "^":">"
}
dir_to_update = {
    ">":[0, 1],
    "v":[1, 0],
    "<":[0, -1],
    "^":[-1, 0]
}

with open(inp, 'r') as f:
    grid = []
    person_dir = ">"
    person_row = 0
    person_col = 0
    for l in f:
        clean_line = l.strip()
        grid.append([charr for charr in clean_line])
        for i, charr in enumerate(grid[-1]):
            if charr in person:
                # found the person
                person_dir = charr
                person_col = i
                person_row = len(grid) - 1

import copy 
def part_1(grid, person_dir, person_col, person_row):
    visited_sym = "*"
    visited_count = 0
    marked_grid = copy.deepcopy(grid)

    # count distinct positions in the map
    max_row = len(grid) 
    max_col = len(grid[0])
    print("Max dims ", max_row, max_col)
    while True:
        next_row = person_row + dir_to_update[person_dir][0]
        next_col = person_col + dir_to_update[person_dir][1]
        # print(f"Current: ({person_row}, {person_col}). Next: ({next_row}, {next_col})")

        # Guard has left the map! 
        is_out_of_row_bound = next_row < 0 or next_row >= max_row
        is_out_of_col_bound = next_col < 0 or next_col >= max_col
        if is_out_of_col_bound or is_out_of_row_bound:
            break

        # if it's an obstacle, we need to rotate the direction 
        # but don't change the index yet, just do that next cycle. 
        # also don't mark visited until we move away
        is_obstacle = marked_grid[next_row][next_col] == "#"
        if is_obstacle:
            # print("Obstacle: ", person_dir, "new dir ", person_to_new_dir[person_dir], is_obstacle)
            person_dir = person_to_new_dir[person_dir]
            continue

        # can validly move now since nothing blocking the way
        # mark as visited 
        if marked_grid[person_row][person_col] != visited_sym:
            visited_count+=1
        marked_grid[person_row][person_col] = visited_sym
        # and promote new indices
        person_row = next_row
        person_col = next_col

    print("visited_count: ", visited_count+1)


# mark places that are about to get revisted as potential loop options?
# first case: mark one over in direction of travel 


# going down and I reach a left-travelled spot, then that should be a loop

# loop is all directions travelled connected together
def is_parallel(side1, side2):
    if (side1 == ">" and side2 == "<") or (side1 == "<" and side2 == ">"):
        return True
    
    if (side1 == "^" and side2 == "v") or (side1 == "v" and side2 == "^"):
        return True

    return False

def is_perpendicular(side1, side2):
    if (side1 == ">" and side2 == "<") or (side1 == "<" and side2 == ">"):
        return True
    
    if (side1 == "^" and side2 == "v") or (side1 == "v" and side2 == "^"):
        return True

    return False

reverse_loop = {
    "<":"v",
    "v":">",
    ">":"^",
    "^":"<"
}

def is_looping(tracked_states):
    next_dir = None
    indices = [-1,-2,-3,-4]
    for i in indices:
        this_state = tracked_states[i][0]
        print("This state ", this_state, " next ", next_dir, i)
        if next_dir is not None and this_state != next_dir:
            return False
        next_dir = reverse_loop[this_state]
    return True        

# getting a loop if the last three segments are in teh right order 
# and if the current segment is exceeding the last one in parallel direction
# and the perp direction has larger than smaller segment of unobstructed travel
visited_sym = "*"
loop_count = 0
marked_grid = copy.deepcopy(grid)
new_obstacles = copy.deepcopy(grid)
max_row = len(grid) 
max_col = len(grid[0])
while True:
    next_row = person_row + dir_to_update[person_dir][0]
    next_col = person_col + dir_to_update[person_dir][1]
    next_dir = person_to_new_dir[person_dir]

    # Guard has left the map! 
    is_out_of_row_bound = next_row < 0 or next_row >= max_row
    is_out_of_col_bound = next_col < 0 or next_col >= max_col
    if is_out_of_col_bound or is_out_of_row_bound:
        break

    # mark it with the symbol before the thing rotated from an obstacle
    if isinstance(marked_grid[person_row][person_col], list):
        marked_grid[person_row][person_col].append(person_dir)
    else:
        marked_grid[person_row][person_col] = [person_dir]
    
    # if it's an obstacle, we need to rotate the direction 
    # but don't change the index yet, just do that next cycle. 
    # also don't mark visited until we move away
    is_obstacle = marked_grid[next_row][next_col] == "#"
    if is_obstacle:
        person_dir = person_to_new_dir[person_dir]
        continue

    # if we walk along the grid in the next-dir, do we hit a visited spot 
    # which was traversed in the same direction
    poss_row = person_row
    poss_col = person_col

    while True:
        poss_row += dir_to_update[next_dir][0]
        poss_col += dir_to_update[next_dir][1]

        # break if out of bounds or at an obstacle 
        new_is_out_of_row_bound = poss_row < 0 or poss_row >= max_row
        new_is_out_of_col_bound = poss_col < 0 or poss_col >= max_col
        if new_is_out_of_col_bound or new_is_out_of_row_bound:
            break
        is_obs_new = marked_grid[poss_row][poss_col] == "#"
        if is_obs_new:
            break
        
        if isinstance(marked_grid[poss_row][poss_col], list) and next_dir in marked_grid[poss_row][poss_col]:
            # found it. 
            # obstacle needs to go in the next spot
            if new_obstacles[next_row][next_col] != "0":
                loop_count += 1
            new_obstacles[next_row][next_col] = "0"
            break

    # and promote new indices
    person_row = next_row
    person_col = next_col


print(new_obstacles)
print("loop_count: ", loop_count)

# 358 too low


# if we were to put an obstacle and change direction
# does it cause you to intersect a visited point travelling in the same 
# direction that was previously traveled at that point
