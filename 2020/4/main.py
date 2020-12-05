import fileinput

def create_list():
    input_string = ""
    entries = []
    f = fileinput.input('input.txt')
    for line in f:
       input_string += line
    tmp_entries = input_string.split('\n\n')
    for tmp_entry in tmp_entries:
        entries.append(tmp_entry.replace('\n', ' '))
    return entries

def convert_to_dict(documents):
    dicts = []
    for document in documents:
        dict_tmp = {}
        key_vals = document.split(' ')
        for key_val in key_vals:
            dict_tmp.update({key_val.split(':')[0] : key_val.split(':')[1]})
        dicts.append(dict_tmp)
    return dicts

def valid_documents(list_of_docs):
    valid_docs = []
    for doc in list_of_docs:
        if "hcl" in doc and "eyr" in doc and "pid" in doc and "iyr" in doc and "ecl" in doc and "hgt" in doc and "byr" in doc:
            valid_docs.append(doc)
    return valid_docs

def valid_hgt(height):
    suffix = height[len(height)-2:]
    measure = height[:len(height)-2]
    if suffix == 'cm' and (int(measure) >= 150 and int(measure) <= 193 ):
        return True
    if suffix == 'in' and (int(measure) >= 59 and int(measure) <= 76 ): 
        return True
    return False

def valid_hcl(haircolor):
    if haircolor[0] != '#' : return False
    if not int(haircolor[1:],16) : return False
    return True

def valid_ecl(eyecolor):
    if eyecolor=='amb' or eyecolor=='blu' or eyecolor=='brn' or eyecolor=='gry' or eyecolor=='grn' or eyecolor=='hzl' or eyecolor=='oth': 
        return True
    return False

def valid_pid(passportid):
    if len(passportid) == 9 and int(passportid) : 
        return True
    return False

def count_valid_data(list_of_docs):
    valid_docs = []
    for doc in list_of_docs:
        if int(doc['byr']) < 1920 or int(doc['byr']) > 2002  : continue
        if int(doc['iyr']) < 2010 or int(doc['iyr']) > 2020  : continue
        if int(doc['eyr']) < 2020 or int(doc['eyr']) > 2030  : continue
        if valid_hgt(doc['hgt']) == False : continue
        if valid_hcl(doc['hcl']) == False : continue
        if valid_ecl(doc['ecl']) == False : continue
        if valid_pid(doc['pid']) == False : continue
        valid_docs.append(doc)
    return valid_docs

documents = create_list() 
dictionaries = convert_to_dict(documents)
valid_docs = valid_documents(dictionaries)
print(len(count_valid_data(valid_docs)))
