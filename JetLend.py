list_of_dickts = [{"key1": "value1"},
                 {"k1": "v1", "k2": "v2", "k3": "v3"},
                   {}, 
                   {}, 
                   {"key1": "value1"}, 
                   {"key1": "value1"}, 
                   {"key2": "value2"}]


def delete_dublicats(obj):
    new_list = []
    new_dict = {}
    total_dict = {}
    counter_list = []
    for i in obj:
        counter = 0
        for b, c in i.items():
            new_dict[b] = c
            counter += 1
        counter_list.append(counter)

    for i in counter_list:
        total_dict = {}
        for b in range(i):
            if new_dict != {}:
                item = new_dict.popitem()
                total_dict[item[0]] = item[1]    
        if total_dict != {}:
            new_list.append(total_dict)
    return new_list

result = delete_dublicats(list_of_dickts)
print(result)