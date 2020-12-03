import fileinput

def create_list():
    input_list = []
    f = fileinput.input('input.txt')
    for line in f:
        input_list.append(line.strip())
    return input_list

# Interesting to see if this step
# could be done with a cycle
def move(input_map, y_move, x_move):
    x_pos, trees = 0, 0
    for i in range(0, len(input_map), y_move):
        if input_map[i][x_pos % len(input_map[0])] == '#' : trees += 1
        x_pos += x_move
    return trees

input_list = create_list()
trees_1 = move(input_list,1,3)
trees_2 = move(input_list,1,1) * move(input_list,1,3) * move(input_list,1,5) * move(input_list,1,7) * move(input_list,2,1)
print("Solution part 1", trees_1)
print("Solution part 2", trees_2)