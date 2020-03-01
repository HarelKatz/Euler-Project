import itertools


before, after = 1, 1
for idx in itertools.count(1):
    if len(str(before)) == 1000:
        print(before)
        print(idx)
        break
    before, after = after, before + after
