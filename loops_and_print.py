def enumerate_list(list):
    list.remove("")
    new_list=[]
    for index, color in enumerate(list):
        new_list.append(f"{index}. {color}")
    return new_list


def enumerate_backwards(list):
    list.remove("")
    new_list=[]
    for index, color in enumerate(list):
        color = color[::-1]
        new_list.append(f"{index}. {color}")
    return new_list
