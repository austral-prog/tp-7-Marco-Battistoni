def index_of_by_index(word, list, index):
    for i in range(index, len(list)):
        if list[i] == word:
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
                del list[index]
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
                del list[index]
                list.insert(index, "")
                eliminations += 1
                index += 1
            else:
                index += 1
    return eliminations