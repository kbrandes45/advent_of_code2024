

# waves of iterations of applying all rules at once stone by stone 
# while true: for stone in stones


def rule1(stone):
    if stone == 0:
        return [1], True
    return [stone], False

def rule2(stone):
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        halway = len(str_stone) // 2
        return [int(str_stone[:halway]), int(str_stone[halway:])], True
    return [stone], False

def rule3(stone):
    return [stone * 2024], True


# brute force
blink_length = 25
stones = [0, 7, 6618216, 26481, 885, 42, 202642, 8791]
for i in range(blink_length):
    new_stones = []
    for stone in stones:
        out, rule1worked = rule1(stone)
        if rule1worked:
            new_stones.extend(out)
            continue
        out, rule2worked = rule2(stone)
        if rule2worked:
            new_stones.extend(out)
            continue
        out, _ = rule3(stone)
        new_stones.extend(out)
    stones = new_stones
    # print("After iter ", i, " stones are: ", stones)

print("num stones ", len(stones))

# less terrible solution
blink_length = 75
stones_dict = {}
stones = [0, 7, 6618216, 26481, 885, 42, 202642, 8791]
for stone in stones:
    stones_dict[stone] = stones_dict.get(stone, 0) + 1

for i in range(blink_length):
    new_stones_dict = {}
    for stone, quantity in stones_dict.items():
        out, rule1worked = rule1(stone)
        if rule1worked:
            for new_stone in out:
                new_stones_dict[new_stone] = new_stones_dict.get(new_stone, 0) + quantity
            continue
        out, rule2worked = rule2(stone)
        if rule2worked:
            for new_stone in out:
                new_stones_dict[new_stone] = new_stones_dict.get(new_stone, 0) + quantity
            continue
        out, _ = rule3(stone)
        for new_stone in out:
            new_stones_dict[new_stone] = new_stones_dict.get(new_stone, 0) + quantity

    stones_dict = new_stones_dict
    # print("New stones: ", new_stones_dict, "i ", i)

stone_sum = 0
for stone, quantity in stones_dict.items():
    stone_sum+= quantity
print("number of stones: ", stone_sum)