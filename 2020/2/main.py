import fileinput

def create_list():
    input_list = []
    f = fileinput.input('input.txt')
    for line in f:
        input_list.append(line.strip())
    return input_list

def create_tuple(input_as_list):
    input_as_tuples = []
    for item in input_as_list:
        work_item = item.split()
        min_max = work_item[0]
        passwd_char = work_item[1]
        passwd = work_item[2]
        min_max_array = min_max.split('-')
        input_as_tuples.append((int(min_max_array[0]),
                                int(min_max_array[1]),
                                passwd_char[0],
                                passwd))
    return input_as_tuples

def check_count_validity(input_as_tuples):
    valid, invalid = 0, 0
    for item in input_as_tuples:
        min, max = item[0], item[1]
        password_char_count = item[3].count(item[2])
        if password_char_count >= min and password_char_count <= max:
            valid+=1
        else:
            invalid+=1
    print('Valid: ',valid, '\nInvalid: ', invalid)

def check_index_validity(input_as_tuples):
    valid, invalid = 0, 0
    for item in input_as_tuples:
        pos_a, pos_b = item[0] - 1, item[1] - 1
        passwd_char = item[2]
        passwd = item[3]
        if passwd[pos_a] == passwd_char and passwd[pos_b] != passwd_char:
            valid+=1
        elif passwd[pos_b] == passwd_char and passwd[pos_a] != passwd_char:
            valid+=1
        else:
            invalid+=1
    print('Valid: ',valid, '\nInvalid: ', invalid)


input_list = create_list()
input_tuples = create_tuple(input_list)
check_count_validity(input_tuples)
check_index_validity(input_tuples)