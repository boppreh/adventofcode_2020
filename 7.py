import re

rules = {base: re.findall(r'(\d+) ([\w ]+?) bags?', contents_str) for base, contents_str in re.findall(r'([\w ]+?) bags contain (.+?)\.', open('7.txt').read())}
assert len(rules) + sum(len(contents) for contents in rules.values()) == 2039
target_colors = {'shiny gold'}
for i in range(len(rules)):
    for base, contents in rules.items():
        if any(pair[1] in target_colors for pair in contents):
            target_colors.add(base)
print(len(target_colors - {'shiny gold'}))
count_required = lambda color: sum(int(n) * (1 + count_required(subcolor)) for n, subcolor in rules[color])
print(count_required('shiny gold'))