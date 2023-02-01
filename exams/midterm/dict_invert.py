def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    tmp = {}

    for k,v in d.items():
        nk = v
        tmp.update({nk:[]})

    list_of_initial_keys = [j for j in d]
    list_of_initial_keys.sort()
    
    for key in tmp:
        for item in list_of_initial_keys:
            if d[item] == key:
                tmp[key].append(item)

    return tmp


d = {4: True, 2: True, 0: True}
g = {1:10, 2:20, 3:30, 4:30}
print(dict_invert(d))
print(dict_invert(g))