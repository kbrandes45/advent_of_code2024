inp = "aoc_day1_input.txt"

left_list = []
right_list = []
with open(inp, 'r') as f:
    for l in f:
        clean_line = l.strip().split("   ")
        left_list.append(int(clean_line[0]))
        right_list.append(int(clean_line[1]))


left_list = sorted(left_list)
right_list = sorted(right_list)
assert len(left_list) == len(right_list)

total_distance = 0
for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])
print(total_distance)

similarity_score = 0
for i in range(len(left_list)):
    similarity_score += left_list[i] * right_list.count(left_list[i])

print(similarity_score)