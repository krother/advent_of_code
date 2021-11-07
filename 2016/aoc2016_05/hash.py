
import hashlib
from os import get_exec_path

def get_next_index(code, i, seventh=False):
    result = None
    while not result:
        i += 1
        s = (code + str(i)).encode()
        md5 = hashlib.md5(s).hexdigest()
        if md5.startswith('00000'):
            if seventh:
                return i, md5[5], md5[6]
            else:
                return i, md5[5]

def get_password(code):
    i = 0
    result = ''
    for _ in range(8):
        i, char = get_next_index(code, i)
        result += char

    return result

def get_password2(code):
    i = 0
    result = ['-'] * 8
    while result.count('-') > 0:
        i, pos, char = get_next_index(code, i, True)
        print(''.join(result), i, pos, char)
        if pos in '01234567' and result[int(pos)] == '-':
            result[int(pos)] = char

    return ''.join(result)


if __name__ == '__main__':
    print(get_password('ffykfhsq'))
    print(get_password2('ffykfhsq'))