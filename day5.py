inp = "aoc_day5_input.txt"

rules = []
updates = []
with open(inp, 'r') as f:
    in_rules = True
    for l in f:
        clean_line = l.strip()
        if clean_line == "":
            in_rules = False
            continue
        if in_rules:
            clean_line = clean_line.split("|")
            rules.append([int(clean_line[0]), int(clean_line[1])])
        else:
            clean_line = clean_line.split(",")
            print(clean_line)
            updates.append([int(y) for y in clean_line])

import math, copy

def get_middle_index(update):
    return int(math.floor(len(update) / 2)) + int(len(update) % 2) - 1
        
def check_an_update(update, rules):
    for rule in rules:
        if update.count(rule[0]) != 1 or update.count(rule[1]) != 1:
            continue
        # valid rule 
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    return True

def sort_me_brutally(update, rules):
    while not check_an_update(update, rules):
        for i in range(len(update)):
            for j in range(i+1, len(update)):
                # take i and put it at position j
                # do a full swap if both pages are in the rules somewhere
                pg1 = update[i]
                pg2 = update[j]
                if [pg2, pg1] in rules:
                    # flip them so it matches the rules
                    update[i], update[j] = pg2, pg1
    return update[get_middle_index(update)]

center_sum = 0
incorrect_center_sums = 0
for update in updates:
    # check all rules
    # skip rules where numbers aren't present 
    if check_an_update(update, rules):
        # get middle page number 
        center_sum += update[get_middle_index(update)]
    else:
        # fix the invalid ones with bubble sort
        incorrect_center_sums += sort_me_brutally(update, rules)
        pass
print("Center sum ", center_sum)
print("other ", incorrect_center_sums)