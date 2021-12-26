import re

data = open('input_data.txt').read()

pattern = r"""inp w\nmul x 0\nadd x z\nmod x 26\ndiv z (-?\d+)\nadd x (-?\d+)\neql x w\neql x 0\nmul y 0\nadd y 25\nmul y x\nadd y 1\nmul z y\nmul y 0\nadd y w\nadd y (-?\d+)\nmul y x\nadd z y"""

m = re.findall(pattern, data)
print(len(m))
print(m)