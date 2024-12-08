inp = "aoc_day2_input.txt"

def is_safe_ordering_check(levels):
    is_increasing = False
    MAX_DIFFER = 3
    for i in range(len(levels) - 1):
        if i == 0:
            if levels[i] < levels[i+1]:
                is_increasing = True
            elif levels[i] > levels[i+1]:
                is_increasing = False
            else:
                # values are equal
                return False
        if is_increasing and levels[i] >= levels[i+1]:
            return False
        if is_increasing and levels[i] + MAX_DIFFER < levels[i+1]:
            return False
        if not is_increasing and levels[i] <= levels[i+1]:
            return False
        if not is_increasing and levels[i] > levels[i+1] + MAX_DIFFER:
            return False
    return True

def do_indices_pass(is_increasing, ind0, ind1, levels):
    MAX_DIFFER = 3
    # print("Checking ", levels[ind0], levels[ind1])
    if is_increasing and levels[ind0] >= levels[ind1]:
        return False
    if is_increasing and levels[ind0] + MAX_DIFFER < levels[ind1]:
        return False
    if not is_increasing and levels[ind0] <= levels[ind1]:
        return False
    if not is_increasing and levels[ind0] > levels[ind1] + MAX_DIFFER:
        return False
    # print("PASSED!")
    return True

def is_safe_ordering_check_ret_i(levels):
    is_increasing = False
    MAX_DIFFER = 3
    is_increasing = levels[0] < levels[-1]
    for i in range(len(levels) - 1):
        # for every pair of values, check if it's greater than or less than the neighbors
        # then need them all true or all false
        found_error = not do_indices_pass(is_increasing, i, i+1, levels)
        if found_error:
            return i
    return None

# if we find it fails, then remove the level it failed at and recheck 
def is_safe_ordering_check_with_damper(levels):
    err_i = is_safe_ordering_check_ret_i(levels)
    if err_i is None:
        return True
    # it failed, so just try all and see if any one passes where the number is removed
    for i in range(len(levels)):
        new_level = levels[:i] + levels[i+1:]
        if is_safe_ordering_check_ret_i(new_level) is None:
            return True
    return False


good = [85, 84, 82, 80, 78, 76, 76, 70]
bad = [35, 30, 29, 28, 26]
print(is_safe_ordering_check_with_damper(bad))
# assert False
with open(inp, 'r') as f:
    num_safe_reports = 0
    num_safe_damped_reports = 0
    for l in f:
        clean_line = l.strip().split(" ")
        report = [int(ll) for ll in clean_line]
        num_safe_reports += int(is_safe_ordering_check(report))
        num_safe_damped_reports+=int(is_safe_ordering_check_with_damper(report))

print(num_safe_reports)
print(num_safe_damped_reports)