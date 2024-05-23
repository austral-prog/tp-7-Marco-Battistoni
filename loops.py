def index_of_by_index(word, list, index):
    i = 0
    if word in list:
        while i < len(list):
            if list[i] == word:
                return False
            else:
                i += 1
    else:
        return(-1)


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
