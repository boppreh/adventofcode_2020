terrain = [[char == '#' for char in line] for line in open('3.txt').read().split('\n') if line]
max_heigth = len(terrain)
max_width = len(terrain[0])

def check_trees(slope_x=3, slope_y=1):
    x = 0
    y = 0
    trees_encountered = 0
    while True:
        x = (x + slope_x) % max_width
        y += slope_y
        if y >= max_heigth:
            break
        trees_encountered += terrain[y][x]
    return trees_encountered

print('Default slope:', check_trees())
print(check_trees(1, 1) * check_trees(3, 1) * check_trees(5, 1) * check_trees(7, 1) * check_trees(1, 2))