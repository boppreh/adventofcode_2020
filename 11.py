input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split('\n')
input = open('11.txt')
matrix = [[char for char in line.strip()] for line in input]
print(matrix)
next_matrix = []
def get_one(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        yield matrix[row][col]
def get_neighbors(row, col):
    for drow in (-1, 0, 1):
        for dcol in (-1, 0, 1):
            if drow != 0 or dcol != 0:
                yield from get_one(row+drow, col+dcol)
def count_occupied_neighbors(row, col):
    return len([pos for pos in get_neighbors(row, col) if pos == '#'])
def count_all_occupied():
    return sum(matrix[row][col] == '#' for row in range(len(matrix)) for col in range(len(matrix[0])))

def print_matrix():
    for row in range(len(matrix)):
        print(''.join(matrix[row]))
def step():
    next_matrix = [[matrix[row][col] for col in range(len(matrix[0]))] for row in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == '.': continue
            if matrix[row][col] == 'L' and count_occupied_neighbors(row, col) == 0:
                next_matrix[row][col] = '#'
            elif matrix[row][col] == '#' and count_occupied_neighbors(row, col) >= 4:
                next_matrix[row][col] = 'L'
    matrix[:] = next_matrix[:]

print_matrix()
for i in range(100):
    step()
    print_matrix()
    print(count_all_occupied()) # 2338