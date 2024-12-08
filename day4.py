inp = "aoc_day4_input.txt"

DESIRED_WORD = "XMAS"
REV_WORD = "SAMX"
ll = len(DESIRED_WORD)

def passes(maybe_word):
    word = maybe_word
    if isinstance(maybe_word, list):
        word = ""
        for ww in maybe_word:
            word+=ww
    assert len(word) == ll, f"failed {word}"
    return word == DESIRED_WORD or word == REV_WORD

# for a list, doing my_list[0:3] is [inclusive:exclusive]
# input is row, col. or index 1, index 2
def check_index(grid, start_row, start_col):
    # horizontal, vertical, diagonal, written backwards, or even overlapping other words
    count = 0
    row = grid[start_row]
    col_count = len(row)
    print("Checking: ", start_row, start_col)
    row_count = len(grid)

    # check horizontal to the right, unless were on the rightmost edge, in which case we will 
    # go left.
    if start_col + ll <= col_count:
        print("case 0: right")
        if passes(row[start_col:start_col+ll]): count+=1 
    if start_col - ll + 1 >= 0:
        print("case 1: left ",start_col-ll+1,start_col+1)
        if passes(row[start_col-ll+1:start_col+1]): count+=1

    # check vertical
    if start_row + ll <= row_count:
        word = ""
        for new_row in range(start_row, start_row+ll):
            word += grid[new_row][start_col]
        print("case 2: down")
        if passes(word): count+=1
    if start_row - ll + 1 >= 0:
        word = ""
        for new_row in range(start_row-ll+1, start_row+1):
            word += grid[new_row][start_col]
        print("case 3: up ", start_row-ll+1, start_row+1)
        if passes(word): count+=1

    # check diagonals
    # check down right 
    if start_col + ll <= col_count and start_row + ll <= row_count:
        down_right_word = ""
        for i in range(ll):
            down_right_word += grid[start_row+i][start_col+i]
        print("case 4: down right")
        if passes(down_right_word): count+=1
            
    # check up right diag
    if start_col + ll <= col_count and start_row - ll + 1 >= 0:
        up_right_word = ""
        for i in range(ll):
            up_right_word += grid[start_row-i][start_col+i]
        print("case 5: up right")
        if passes(up_right_word): count+=1

    # check up left
    if start_row - ll + 1 >= 0  and start_col - ll + 1 >= 0:
        up_left_word = ""
        for i in range(ll):
            up_left_word += grid[start_row-i][start_col-i]
        print("case 6: up left ", up_left_word)
        if passes(up_left_word): count+=1 
    
    # check down left
    if start_row + ll <= row_count and start_col - ll + 1>= 0:
        down_left_word = ""
        for i in range(ll):
            down_left_word += grid[start_row+i][start_col-i]
        print("case 7: down left")
        if passes(down_left_word): count+=1 
    print("resulting in ", count)
    if count == 1:
        print("THIS OMNE!")
    return count

with open(inp, 'r') as f:
    grid = []
    for l in f:
        clean_line = l.strip()
        grid.append([charr for charr in clean_line])


# first index is the row
# second index is the col
count_total = 0
import copy
new_grid = copy.deepcopy(grid)
num_xs = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):

        # only check from x-values onward
        if grid[row][col] != "X":
            continue
        num_xs +=1
        # and check everything
        new_count = check_index(grid, row, col)
        count_total+=new_count
print(num_xs)
print("count of christmas", count_total)

def check_for_x_mas(grid, start_row, start_col):
    # needs two m's and two s's in neighboring spots. 
    # so just go in order and confirm there's an "ss" or "mm" in the final list
    # and there should only be 2 m's and 2 s's exactly
    final_list = []
    # top left
    final_list.append(grid[start_row-1][start_col-1])
    final_list.append(grid[start_row+1][start_col-1])
    final_list.append(grid[start_row+1][start_col+1])
    final_list.append(grid[start_row-1][start_col+1])
    
    word = ""
    for char in final_list:
        word+=char
    
    if ("MM" in word or "SS" in word) and word.count("M") == 2 and word.count("S") == 2:
        return True
    return False

mas_count = 0
num_as = 0
for row in range(1,len(grid)-1):
    for col in range(1,len(grid[row])-1):
        # only check from x-values onward
        if grid[row][col] != "A":
            continue
        num_as +=1
        # and check everything
        new_count = check_for_x_mas(grid, row, col)
        mas_count+=new_count

print(num_as)
print("count of MAS x's", mas_count)