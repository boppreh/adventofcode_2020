pass_to_id = lambda p: int(p.translate(str.maketrans('FBLR', '0101')), base=2)
assert pass_to_id('BFFFBBFRRR') == 567
assert pass_to_id('FFFBBBFRRR') == 119
assert pass_to_id('BBFFBBFRLL') == 820

ids = [pass_to_id(p.strip()) for p in open('5.txt').readlines()]
print(max(ids))
print([i for i in range(0, max(ids)) if i not in ids])