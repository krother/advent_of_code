
import re
import numpy as np
import pandas as pd

data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".split('\n')

def parse(f):
    entries = []
    for line in f:
        ing, allergens = line.strip().split(' (contains ')
        ing = ing.split()
        allergens = allergens.replace(')', '').split(', ')
        entries.append((ing, allergens))
    return entries

data = open('input_big.txt')
entries = parse(data)

ing, alg = [], []
for i, a in entries:
    ing += i
    alg += a

ing, alg = set(ing), set(alg)

# Each allergen is found in exactly one ingredient.         
possible = np.ones((len(ing), len(alg)), dtype=np.uint8)
df = pd.DataFrame(possible, columns=alg, index=ing)

# mark ingredients that cannot contain that allergen
for i, a in entries:
    for allergen in a:
        # has to be in one of the ingredients listed
        for ingredient in ing:
            if ingredient not in i:
                df.loc[ingredient, allergen] = 0

zero = df.sum(axis=1)
zero = zero[zero == 0]

count = 0
for i, a in entries:
    for ingredient in i:
        if ingredient in zero.index:
            count += 1
print(count) # 5 and 2230


# part II
nonzero = df.sum(axis=1)
nonzero = df[nonzero > 0].copy()

assigned = {}
while len(assigned) < len(alg):
    print(assigned)
    s = nonzero.sum(axis=0)
    u = s[s==1]
    for ingredient in u.index:
        hit = nonzero[ingredient] == 1
        m = nonzero.loc[hit][ingredient].index[0]
        assigned[ingredient] = m
        nonzero[ingredient] = 0
        nonzero.loc[m] = 0
        
sol = []
for a in sorted(assigned):
    sol.append(assigned[a])
print(','.join(sol))