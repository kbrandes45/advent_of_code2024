# AAAA
# BBCD
# BBCC
# EEEC

# find area and perimeter
# count islands and their area by doing dfs search from each found instance
# need to mark visited so that each independent island is unique 

# from an island set, can just count how many neighbors each pixel has and then 
# go from that to get perimeter
import copy 

inp = "aoc_day12_input.txt"

with open(inp, 'r') as f:
    grid = []
    for l in f:
        clean_line = l.strip()
        grid.append([char for char in clean_line])


grand_visited = set()
changes = [(0,1), (0, -1), (1, 0), (-1, 0)]

islands = []
for row in range(len(grid)):
    for col in range(len(grid[-1])):
        if (row, col) in grand_visited:
            continue
        
        new_island_seed = grid[row][col]
        queue_island = [(row, col)]
        island_land = set()
        island_visited = set()
        while len(queue_island) > 0:
            current_island = queue_island.pop(0)
            island_land.add(current_island)
            for change in changes:
                new_loc = (current_island[0]+change[0], current_island[1]+change[1])
                if new_loc[0] < 0 or new_loc[0] >= len(grid):
                    continue
                if new_loc[1] < 0 or new_loc[1] >= len(grid[-1]):
                    continue
                if new_loc in island_visited:
                    continue

                new_loc_value = grid[new_loc[0]][new_loc[1]]
                if new_loc_value == new_island_seed:
                    queue_island.append(new_loc)

                island_visited.add(new_loc)

        islands.append(island_land)
        for pt in island_land:
            grand_visited.add(pt)

fence_cost = 0
discount_cost = 0
for island in islands:
    area = len(island)
    perimeter = 0
    sides = set()
    for point in island:
        no_neighbor_count = 0
        bulk_discounts = 0
        for change in changes:
            new_loc = (point[0]+change[0], point[1]+change[1])
            if new_loc not in island: 
                no_neighbor_count += 1

                # if we found a no side, lets explore this direction fully to get a side length. 
                iter_changer = (0,1)
                if change in {(0,1), (0, -1)}:
                    # left right change
                    iter_changer = (1, 0)

                # go both positive and negative directions
                def check_points(incoming, dir, iter_changer, change, island):
                    count = 0
                    start = copy.deepcopy(incoming)
                    members = {start}
                    while True:
                        start = (start[0]+dir * iter_changer[0], start[1]+ dir * iter_changer[1])
                        if start not in island:
                            return count, members
                        # have to check the point in original change dir is still not there to continue in this dir
                        new_check_loc = (start[0]+change[0], start[1]+change[1])
                        if new_check_loc not in island: 
                            count += 1
                            members.add(start)
                        else:
                            return count, members
                
                up, members = check_points(point, 1, iter_changer, change, island)
                down, dmembers = check_points(point, -1, iter_changer, change, island)
                expanded_side = set()
                for mm in members: expanded_side.add(mm)
                for mm in dmembers: expanded_side.add(mm)
                sides.add((frozenset(expanded_side), change))

        perimeter += no_neighbor_count
    num_sides = len(sides)
    discount_cost += (num_sides * area)
    fence_cost += (perimeter * area)

print("fence cost: ", fence_cost)
print("discount cost: ", discount_cost)