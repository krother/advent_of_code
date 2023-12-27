# determine intercepts for part 2
# requires having all three slopes

from util import parse

mrx, mry, mrz = -110, -135, 299

data = open("input_data.txt").read()
stones = parse(data)

bsx1, bsy1, bsz1, msx1, msy1, msz1 = stones[0]
for s in stones[1:]:
    print()
    bsx2, bsy2, bsz2, msx2, msy2, msz2 = s

    alpha = (mry - msy1) / (mrx - msx1)
    beta = (mry - msy2) / (mrx - msx2)
    print(alpha, beta)

    brx = (bsy1 - bsy2 - alpha * bsx1 + beta * bsx2) / (beta - alpha)
    print(brx, "has to be rounded for binary imprecision")
    brx = round(brx)
    # brx = 335849990884055 also can be found by looking in the input data
    # there is one point with msx = brx so it has to be hit at t=0 !

    bry = bsy1 - (bsx1 - brx) * (mry - msy1) / (mrx - msx1)
    brz = bsz1 - (bsx1 - brx) * (mrz - msz1) / (mrx - msx1)

    print(brx, bry, brz)
    solution_part_two = sum([brx, bry, brz])
    print("sum of intercepts: ", solution_part_two)
    assert solution_part_two == 828418331313365
