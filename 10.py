import re
from collections import Counter

numbers = [int(n) for n in re.findall(r'\d+', open('10.txt').read())]
numbers.append(max(numbers) + 3)
last_joltage = 0
diffs = Counter()
while numbers:
    next_candidates = [n for n in numbers if n <= last_joltage + 3]
    next_joltage = min(next_candidates)
    diffs[next_joltage - last_joltage] += 1
    last_joltage = next_joltage
    numbers.remove(last_joltage)

print(diffs[1] * diffs[3])

from functools import lru_cache
@lru_cache
def count_ways(current, numbers, final):
    if current == final:
        return 1
    return sum(count_ways(other, numbers, final) for other in numbers if 0 < other - current <= 3)

assert count_ways(0, (16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4, 22), 22) == 8
numbers = tuple(int(line.strip()) for line in open('10.txt'))
final = max(numbers) + 3
numbers = numbers + (final,)
print(count_ways(0, numbers, final))