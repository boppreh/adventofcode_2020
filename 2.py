import re

valid_count = 0
for line in open('2.txt').readlines():
    start_str, end_str, letter, password = re.fullmatch(r'(\d+)-(\d+) (\w+): (\w+)\n', line).groups()
    valid_count += int(start_str) <= password.count(letter) <= int(end_str)
print(valid_count)

valid_count = 0
for line in open('2.txt').readlines():
    pos1_str, pos2_str, letter, password = re.fullmatch(r'(\d+)-(\d+) (\w+): (\w+)\n', line).groups()
    valid_count += (password[int(pos1_str)-1] + password[int(pos2_str)-1]).count(letter) == 1
print(valid_count)