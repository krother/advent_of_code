
def check_triangle(a, b, c):
    a, b, c = sorted((a, b, c))
    if a + b > c:
        return True
    return False


def count_correct_triangles(triangles):
    return sum([check_triangle(*tri) for tri in triangles])


def parse_line(line):
    return [int(val) for val in line.strip().split()]


def get_triplets(lines):
    for i in range(0, len(lines), 3):
        yield lines[i], lines[i+1], lines[i+2]


def transpose(triplet):
    return list(zip(*triplet))


def read_triangles_vertical(lines):
    result = []
    lines = [parse_line(li) for li in lines]
    for triplet in get_triplets(lines):
        result += transpose(triplet)
    return result 



if __name__ == "__main__":
    # part 1
    triangles = [parse_line(line) for line in open('input.txt')]
    print(len(triangles), count_correct_triangles(triangles))

    # part 2
    triangles = read_triangles_vertical(open('input.txt'))
    print(len(triangles), count_correct_triangles(triangles))