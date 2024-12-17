# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

def is_int(inval):
    return inval == int(inval)

def parse_input(ba, bb, bp, is_part_two=False):
    start = ba.split("X+")[-1].split(",")
    a_x = int(start[0])
    a_y = int(start[-1].split("Y+")[-1])
    start = bb.split("X+")[-1].split(",")
    b_x = int(start[0])
    b_y = int(start[-1].split("Y+")[-1])
    start = bp.split("X=")[-1].split(",")
    g_x = int(start[0])
    g_y = int(start[-1].split("Y=")[-1])
    if is_part_two:
        g_x += 10000000000000
        g_y += 10000000000000

    b_push = (a_y * g_x - a_x * g_y) / (a_y * b_x - a_x * b_y)
    a_push = g_x / a_x - (b_x/a_x) * b_push 

    if abs(b_push - round(b_push)) < 1e-3:
        b_push = round(b_push)
    if abs(a_push - round(a_push)) < 1e-3:
        a_push = round(a_push)
    print(b_push, a_push)
    if is_int(a_push) and is_int(b_push):
        return 3*a_push + b_push
    return None

inp = "aoc_day13_input.txt"
total_tokens = 0
is_part_two = True
with open(inp, 'r') as f:
    setoflines = []
    for l in f:
        clean_line = l.strip()
        if clean_line == "":
            print(setoflines)
            tokens = parse_input(*setoflines, is_part_two=is_part_two)
            if tokens is not None:
                total_tokens+=tokens
            setoflines = []
            continue
        setoflines.append(clean_line)

    if len(setoflines) > 0:
        print(setoflines)
        tokens = parse_input(*setoflines, is_part_two=is_part_two)
        if tokens is not None:
            total_tokens+=tokens

print(total_tokens)
# print("a: ", a_push, " b: ", b_push)
# cost = 3 * a_push + 1 * b_push

