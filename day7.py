inp = "aoc_day7_input.txt"

calib_instructions = []
with open(inp, 'r') as f:
    for l in f:
        calib_instructions.append(l.strip())

# 21037: 9 7 18 13
import copy
# bfs search down operators 
# just need to track current state and then try new operators
def handle_calib_instruction(calib_string):
    split_str = calib_string.strip().split(": ")
    target_value = int(split_str[0])
    right_hand_sides = [(int(val), i) for i, val in enumerate(split_str[1].split(" "))] # tuples of (value, position in equation)
    total_nums = len(right_hand_sides)
    left_hand_sides = [copy.deepcopy(right_hand_sides[0])]
    while len(left_hand_sides) > 0:
        # iterate until operators remain
        # break early if we get the full result?
        (curr_lhs, pos_in_equ) = left_hand_sides.pop(0)
        if pos_in_equ == total_nums - 1:
            # confirm this is the right condition
            # check that it's equal
            if curr_lhs == target_value:
                return True, target_value
            continue
        elif curr_lhs > target_value:
            # already exceeded the value, so just bail early 
            continue
        next_candidate = right_hand_sides[pos_in_equ + 1][0]
        left_hand_sides.append((curr_lhs + next_candidate, pos_in_equ+1))
        left_hand_sides.append((curr_lhs * next_candidate, pos_in_equ+1))
        # concat operation
        left_hand_sides.append((int(str(curr_lhs)+str(next_candidate)), pos_in_equ+1))
    return False, None

total_calib_res = 0
for instru in calib_instructions:
    worked, target = handle_calib_instruction(instru)
    if worked:
        total_calib_res += target
print("total: ", total_calib_res)