"""Packet Decoder

https://adventofcode.com/2021/day/16

"""

PLUS, PROD, MIN, MAX, LITERAL, GT, LT, EQ = range(8)

SYMBOLS = {
    PLUS: '+', 
    PROD: '*',
    MIN: 'min',
    MAX: 'max',
    GT: '>',
    LT: '<',
    EQ: '=='
}

def prod(params):
    result = 1
    for p in params:
        result *= p
    return result

def greater(params):
    assert len(params) == 2
    return int(params[0] > params[1])    

def lesser(params):
    assert len(params) == 2
    return int(params[0] < params[1])    

def equal(params):
    assert len(params) == 2
    return int(params[0] == params[1])    


OPERATOR_FUNCS = {
    PLUS: sum,
    PROD: prod,
    MIN: min,
    MAX: max,
    GT: greater,
    LT: lesser,
    EQ: equal
}

class Literal:

    def __init__(self, version, value):
        self.version = version
        self.value = value

    def __repr__(self):
        return f'{self.value}'


class Operator:

    def __init__(self, version, typeid, packets):
        self.version = version
        self.operator = typeid
        self.params = packets

    def __repr__(self):
        params = ' '.join([str(p) for p in self.params])
        symbol = SYMBOLS[self.operator]
        return f'({symbol} {params})'

    def get_eval_params(self):
        params = []
        for s in self.params:
            if isinstance(s, Operator):
                params.append(s.evaluate())
            else:
                params.append(s.value)
        return params

    def evaluate(self):
        params = self.get_eval_params()
        func = OPERATOR_FUNCS[self.operator]
        return func(params)


def hex_to_bin(hex):
    return bin(int(hex, 16))[2:].zfill(len(hex)*4)


def all_bin(data):
    return "".join([hex_to_bin(c) for c in data])


def parse_literal(data, version):
    val = ''
    i = 0
    while True:
        sig = data[0]
        val += data[1:5]
        data = data[5:]
        if sig == '0': # last bit
            value = int(val, 2)
            return data, Literal(version, value)

def parse_nbit_operator(data, version, typeid):
    nbits = int(data[:15], 2)
    assert nbits > 0
    data = data[15:]
    subpackets = list(iterate_packets(data[:nbits]))
    data = data[nbits:]
    return data, Operator(version, typeid, subpackets)


def parse_nsub_operator(data, version, typeid):
    nsub = int(data[:11], 2)
    data = data[11:]
    subpackets = []
    for i in range(nsub):
        data, p = get_next_packet(data)
        subpackets.append(p)
    return data, Operator(version, typeid, subpackets)


def get_next_packet(data):
    version = int(data[:3], 2)
    typeid = int(data[3:6], 2)
    lengthtype = data[6]
    if typeid == LITERAL:
        return parse_literal(data[6:], version)
    elif lengthtype == '0': # next:length in bits
        return parse_nbit_operator(data[7:], version, typeid)
    else:
        return parse_nsub_operator(data[7:], version, typeid)


def iterate_packets(data):
    while len(data) > 8:
        data, packet = get_next_packet(data)
        yield packet


def parse(data):
    data = all_bin(data)
    result = list(iterate_packets(data))
    return result    


def recursive_version_sum(records):
    total = 0
    for r in records:
        total += r.version
        if isinstance(r, Operator):
            total += recursive_version_sum(r.params)
    return total


def solve(data):
    data = data.strip()
    records = parse(data)
    return recursive_version_sum(records)


def solve2(data):
    data = data.strip()
    records = parse(data)
    print(records)
    assert len(records) == 1
    return records[0].evaluate()


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 893

    result = solve2(input_data)
    print(f'Example 2: {result}')
    # 4358595186090
