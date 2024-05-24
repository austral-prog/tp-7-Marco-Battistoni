def index_of_by_index(word, list, index):
    appearance = 0 
    for i, item in enumerate(list):
        if item == word:
            appearance += 1
            if appearance == index:
                return i
    return -1

def index_of_empty(list):
    index = 0
    if "" in list:
        while index < len(list):
            if list[index] == "":
                return(index)
            else:
                index += 1
    else:
        return(-1)


def index_of(word, list):
    index = 0
    if word in list:
        while index < len(list):
            if list[index] == word:
                return(index)
            else:
                index += 1
    else:
        return(-1)


def put(word, list):
    index = 0
    if "" in list:
        while index < len(list):
            if list[index] == "":
                list.insert(index,word)
                return(index)
            else:
                index += 1
    else:
        return(-1)


def remove(word, list):
    index = 0
    eliminations = 0
    if word in list:
        while index < len(list):
            if list[index] == word:
                list.replace(word)
                eliminations += 1
        return eliminations
    else:
        return(0)
