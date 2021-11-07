
import re

HYPERNET = r'\[(\w+)\]'
ABBA = r'(\w)(?!\1)(\w)\2\1'
ABA = r'(\w)(?!\1)(\w)\1'

def parse_address(code):
    hypernet = re.findall(HYPERNET, code)
    hypernet = '-'.join(hypernet)
    code = re.sub(HYPERNET, '-', code)
    return code, hypernet

def has_abba(code):
    return re.search(ABBA, code)

def has_tls(code):
    code, hypernet = parse_address(code)
    if has_abba(hypernet):
        return False
    if has_abba(code):
        return True
    return False

def has_ssl(code):
    code, hypernet = parse_address(code)
    for i, a in enumerate(code[:-2]):
        b = code[i+1]
        bab = b + a + b
        if (
            a == code[i+2]
            and a != b
            and not '-' in bab
            and hypernet.find(bab) >= 0
        ):
            return True
    return False


if __name__ == '__main__':
    print(sum(map(has_tls, open('input.txt'))))
    print(sum(map(has_ssl, open('input.txt'))))
