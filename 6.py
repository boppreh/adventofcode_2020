import string
questions = string.ascii_lowercase

answers_per_group = [[set(line) for line in group.split('\n')] for group in open('6.txt').read().strip().split('\n\n')]
total_anyone_yes = sum(len(set().union(*group)) for group in answers_per_group)
print(total_anyone_yes)
total_everyone_yes = sum(len([question for question in questions if all(question in answers for answers in group)]) for group in answers_per_group)
print(total_everyone_yes)