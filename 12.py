import re
input = """
F10
N3
F7
R90
F11
""".split()
input = open('12.txt')
instructions = [(line[0], int(line[1:])) for line in input]
directions_clockwise = ['N', 'E', 'S', 'W'] * 4
deltas = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}

current_direction = 'E'
x = 0
y = 0
for direction, amount in instructions:
    #print(f'{direction}{amount}', 'North', -y, ', East', x, ', Facing', current_direction)
    if direction in ('L', 'R'):
        current_index = directions_clockwise.index(current_direction, 4)
        new_index = current_index + amount//90 * (1 if direction == 'R' else -1)
        current_direction = directions_clockwise[new_index]
    else:
        if direction == 'F':
            direction = current_direction
        dx, dy = deltas[direction]
        x += dx * amount
        y += dy * amount
    #print('North', -y, ', East', x, ', Facing', current_direction)
    #print()
    

print(x, y)
print(abs(x) + abs(y))

waypoint_x = 10
waypoint_y = -1
x = 0
y = 0
for direction, amount in instructions:
    print(f'{direction}{amount}', 'North', -y, ', East', x)
    print(waypoint_x, waypoint_y)
    if direction == 'F':
        x += waypoint_x * amount
        y += waypoint_y * amount
    elif direction in deltas:
        dx, dy = deltas[direction]
        waypoint_x += dx * amount
        waypoint_y += dy * amount
    else:
        if direction == 'L':
            amount = 360 - amount
        for i in range(amount // 90):
            waypoint_x, waypoint_y = -waypoint_y, waypoint_x
    print('North', -y, ', East', x)
    print(waypoint_x, waypoint_y)
    print()
    

print(x, y)
print(abs(x) + abs(y))