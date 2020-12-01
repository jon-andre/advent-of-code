import fileinput

def find_two_integers(input_as_list, target_value):
    dictionary = create_dictionary(input_as_list)
    for i in input_as_list:
        search_for = target_value - i
        if dictionary.get(search_for):
            return i * input_as_list[dictionary.get(search_for)]

def find_three_integers(input_as_list, target_value):
    for item in input_as_list:
        # If the main target is 2020 and the current item is 1000,
        # search for the sub target 1020 (2020-1000)
        new_target_value = target_value-item
        if find_two_integers(input_as_list, new_target_value) != None:
            return(item * find_two_integers(input_as_list, new_target_value))

def create_dictionary(input_as_list):
    dictionary = {}
    # The item is the dictionary key, while the index is the value.
    # We want to search for the item, not the index. 
    for idx,item in enumerate(input_as_list):
        dictionary[item] = idx
    return dictionary

def create_list():
    input_list = []
    f = fileinput.input('input.txt')
    for line in f:
        input_list.append(int(line.strip()))
    return input_list

input_list = create_list()
print(find_two_integers(input_list, 2020))
print(find_three_integers(input_list, 2020))