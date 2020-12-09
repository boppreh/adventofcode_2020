import re
numbers = [int(n) for n in re.findall(r'\d+', open('9.txt').read())]

for i in range(25, len(numbers)):
    previous = numbers[i-25:i]
    if numbers[i] not in [a+b for a in previous for b in previous]:
        first_invalid = numbers[i]
        print(first_invalid)
        break

slice = []
for n in numbers:
    slice.append(n)
    while sum(slice) > first_invalid:
        slice.pop(0)
    if len(slice) > 1 and sum(slice) == first_invalid:
        print(sum(slice), len(slice), min(slice) + max(slice))