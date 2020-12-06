import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def check_fields_batch(documents):
    return [all(field + ':' in document for field in required_fields) for document in documents]

def validate_height(value):
    if match := re.fullmatch(r'(\d+)cm', value):
        return 150 <= int(match[1]) <= 193
    elif match := re.fullmatch(r'(\d+)in', value):
        return 59 <= int(match[1]) <= 76
    else:
        return False
field_validators = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': validate_height,
    'hcl': lambda v: re.fullmatch(r'#[0-9a-f]{6}', v),
    'ecl': {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}.__contains__,
    'pid': lambda v: re.fullmatch(r'\d{9}', v),
    'cid': lambda v: True
}
def check_validators_batch(documents):
    return [all(field + ':' in document for field in required_fields) and all(field_validators[field](value) for field, value in re.findall(r'(\w+):(\S+)', document)) for document in documents]

print(sum(check_fields_batch(open('4.txt').read().split("\n\n"))))
print(sum(check_validators_batch(open('4.txt').read().split("\n\n"))))
