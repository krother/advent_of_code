from util import parse


def check_collision(a, b, cmin, cmax):
    ax, ay, _, adx, ady, _ = a
    bx, by, _, bdx, bdy, _ = b
    a = ax, ay, adx, ady
    b = bx, by, bdx, bdy

    # x = ax + adx * ta
    # x = bx + bdx * tb
    # y = by + bdy * tb
    # y = ay + ady * ta
    #
    # ax + adx * ta = bx + bdx * tb
    # ay + ady * ta = by + bdy * tb
    #
    # ta = (bx + bdx * tb - ax) / adx
    # tb = (ax + adx * ta - bx) / bdx

    # ta = (bx + bdx * tb - ax) / adx
    # ay - by + ady/adx * (bx + bdx * tb - ax) = bdy * tb
    # (ay - by) + bx*ady/adx + bdx*tb*ady/adx - ax*ady/adx = bdy * tb
    # (ay - by) + bx*ady/adx - ax*ady/adx = tb * (bdy - bdx*ady/adx)
    # tb = ((ay - by) + bx*ady/adx - ax*ady/adx) / (bdy - bdx*ady/adx)
    div = bdy - bdx * ady / adx

    if div != 0:
        tb = ((ay - by) + bx * ady / adx - ax * ady / adx) / div
        ta = (bx + bdx * tb - ax) / adx

        xcoll = ax + adx * ta
        ycoll = ay + ady * ta
        # print(f"x:{xcoll:7.2f}    y:{ycoll:7.2f}    ta:{ta:5.2}    tb:{tb:5.2}")

        if cmin <= xcoll <= cmax and cmin <= ycoll <= cmax and ta > 0 and tb > 0:
            return True

    return False


def solve(data, cmin, cmax):
    print()
    stones = parse(data)
    result = 0
    for i, a in enumerate(stones):
        for b in stones[i + 1 :]:
            if check_collision(a, b, cmin, cmax):
                result += 1
    return result


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data, 200000000000000, 400000000000000)
    print(f"Example 1: {result}")  # 26657
