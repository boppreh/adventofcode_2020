import requests

numbers = {int(line) for line in open('1.txt').readlines()}
for number in numbers:
    if 2020 - number in numbers:
        print(number * (2020 - number))
for a in numbers:
    for b in numbers:
        if 2020 - a - b in numbers:
            print(a * b * (2020 - a - b))