

def transform(subject, loop_size):
    value = 1
    for i in range(loop_size):
        value = value * subject
        value = value % 20201227
    return value

def decrypt(public):
    value = 1
    subject = 7
    loop = 0
    while value != public:
        value = value * subject
        value = value % 20201227
        loop += 1
    return loop, value


def solve(card_public):
    # card_public = transform(subject, card_loop)
    door_public = decrypt(card_public)
    print(door_public)


# example
card_public = 5764801
door_public = 17807724
assert decrypt(card_public) == (8, 5764801)
assert decrypt(door_public) == (11, 17807724)

key1 = transform(door_public, 8)
key2 = transform(card_public, 11)
assert key1 == key2

# main input
card_public = 9232416
door_public = 14144084
card_loop, _ = decrypt(card_public)
door_loop, _ = decrypt(door_public)
key1 = transform(door_public, card_loop)
key2 = transform(card_public, door_loop)
assert key1 == key2

