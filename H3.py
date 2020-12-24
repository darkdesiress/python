myList = [4, 5, 6, 7, 8, 9, 0]


def shift(my_list, steps):
    new_list = []
    if steps < 0:
        new_list += my_list[-steps:]
        new_list += my_list[:-steps]
        return new_list
    new_list += my_list[-steps:]
    new_list += my_list[:-steps]

    return new_list


print(shift(myList, -2))


def dif(array):
    boole = True
    for i in array:
        if i % array[0] == 0:
            boole = True
        else:
            return False
    return boole


def inters(x, y, new):
    for i in x:
        for j in y:
            if i == j:
                new.append(i)
                break
    return new
