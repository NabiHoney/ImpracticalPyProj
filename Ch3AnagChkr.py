"""Check for anagrams"""
from itertools import permutations
import copy
pconv = []
perm = permutations([1, 2, 3, 4, 5])
for i in list(perm):
    pconv.append(i)
res = [[str(num) for num in inner_list] for inner_list in pconv]
for i, x in enumerate(res):
    for j, a in enumerate(x):
        if '1' in a:
            res[i][j] = a.replace('1', 'h')
        if '2' in a:
            res[i][j] = a.replace('2', 'e')
        if '3' in a:
            res[i][j] = a.replace('3', 'a')
        if '4' in a:
            res[i][j] = a.replace('4', 'l')
        if '5' in a:
            res[i][j] = a.replace('5', 's')
outres = copy.deepcopy(res)
for inner_list in outres:
    for element in inner_list:
        print(element, end="")
    print("")
