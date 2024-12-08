inp = "aoc_day3_input.txt"

# mul(2,4)&mul[3,7]!^don't()_
# 2,4)&mul[3,7]!^don't()_
# vals_inside = 2,4
# vals_left = &mul[3,7]!^don't()_
import copy 

def update_enabled_state(current_state, in_str):
    do_inst = "do()"
    dont_inst = "don't()"
    chopped_str = copy.deepcopy(in_str)
    if len(in_str) < len(do_inst): 
        return current_state
    while True:
        val_of_choice = do_inst
        if current_state:
            # it is enabled
            # find the first don't instance to see if it's disabled. 
            val_of_choice = dont_inst

        found_ind = chopped_str.find(val_of_choice)
        print("is enabled ", current_state, " for ", chopped_str," ind ", found_ind)
        if found_ind == -1:
            print("Final state: ", current_state)
            return current_state
        
        chopped_str = chopped_str[found_ind+len(val_of_choice):]
        current_state = not current_state

with open(inp, 'r') as f:
    summ = 0
    is_enabled = True
    for l in f:
        incoming = l.strip()
        potential_muls = incoming.strip().split("mul(")
        print(potential_muls)
        for pm in potential_muls:
            if ")" not in pm:
                # not valid
                is_enabled= update_enabled_state(is_enabled, pm)
                continue

            mul_splitter = pm.split(")")
            vals_inside = mul_splitter[0]

            if "," not in vals_inside:
                # not valid
                is_enabled= update_enabled_state(is_enabled, pm)
                continue
            
            num_vals = vals_inside.split(",")
            if len(num_vals) != 2:
                is_enabled= update_enabled_state(is_enabled, pm)
                continue

            try:
                first = int(num_vals[0])
                second = int(num_vals[1])
            except Exception:
                is_enabled= update_enabled_state(is_enabled, pm)
                continue

            if is_enabled:
                summ += first*second

            # update after the mul is added since there wouldn't have been 
            # a do/dont before hand if the mul is right 
            is_enabled= update_enabled_state(is_enabled, pm)
            
    print(summ)