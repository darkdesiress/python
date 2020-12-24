import math, ipaddress, random


def exercise1(a, b):
    return tuple((a + b, a * b))


def exercise2(a, b):
    return math.sqrt(a + math.sqrt(b))


def exercise3():
    numbers = []
    for i in range(1000, 4250):
        if (i % 5 == 0) and (i % 3 != 0):
            numbers.append(i)
    print(numbers)


def exercise4(x):
    if x in range(3, 6):
        x -= 13
    elif x in range(8, 41):
        x -= 50
    elif 0 > x > 2000:
        x = x * x * x * x
    else:
        x = 0
        return x


def exercise5(x):
    return (x * 1.8) + 32


def exercise6(money, percent):
    final = 0
    for i in range(5):
        final += money
        m = (final * percent) / 100
        final += m

        print(final)


def exercise7(week, month, year):
    days = week * 7 \
           + month * 30 \
           + year * 360
    return days


def exercise8(x):
    i = 2
    nums_list = []
    while i * i <= x:
        if x % i:
            i += 1
        else:
            x //= i
            nums_list.append(i)
    if x > 1:
        nums_list.append(i)
        return nums_list


def exercise9(x):
    nums_list = []
    for i in range(1, x + 1):
        if x % i == 0:
            nums_list.append(i)
    return nums_list


print(exercise9(36))


def exercise10(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


print(exercise10(0, 0, 1, 1))


def exercise11(x):
    array = []
    num = 0
    y = 0
    while num < x:
        num = y ** 2
        if num < x:
            array.append(num)
            y += 1
        else:
            break
    return array


def exercise12(nums_list, s):
    x = s[0]
    y = s[1]
    sum_elem = 0
    for i in range(x, y + 1):
        sum_elem += nums_list[i]
        return sum_elem


def exercise13(x, y):
    nums_list = []
    for i in range(x):
        nums_list.append(y)
    return nums_list


print(exercise13(6, -1))


def exercise14(arr, rem):
    return arr.remove(rem)


def exercise16(num):
    array = list(map(int, str(num)))
    flag = False
    for elem in range(len(array) - 1):
        if max(array[elem], array[elem + 1]) == array[elem]:
            flag = True
        else:
            flag = False
            break
    return flag


def exercise17(nums_list):
    return nums_list == nums_list[::-1]


def exercise19(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    else:
        return True


def exercise20(string):
    new_list = set("a = 2 + 278")
    only_digits = ""
    for digit in string:
        if digit in new_list:
            only_digits += digit
    return only_digits


def exercise21(*args):
    even = 0
    odd = 0
    for elem in args:
        if elem % 2 == 0:
            even += elem
        else:
            odd += elem
    return even / 2, odd / 2


def exercise22(array):
    return [elem for elem in array if elem != 0]


print(exercise22('[1,2,0,0,4,0]'))


def exercise23(array, integer):
    closer = 10000
    for elem in array:
        closer = min(closer, abs(elem - integer))

    for i in array:
        if abs(i - integer == closer):
            return i


def exercise24(sentence):
    vowels = set("Привет, как дела")
    string = ""
    for letter in sentence:
        if letter in vowels:
            string += letter + 'c' + letter
        else:
            string += letter

    return string


def exercise27(array):
    counter = 0
    array_m = max(array)
    for elem in array:
        if elem * 0.1 <= array_m:
            counter += 1
    return counter


def exercise29(list1, list2):
    if list1 == list2:
        return True
    else:
        return False


print(exercise29())


def exercise30(nums_list):
    new_list = []
    x = 0
    for i in nums_list:
        if i != 0:
            new_list.append(i)
        else:
            x += 1
    for i in range(x):
        new_list.append(0)
    return new_list


def exercise33(nums_list):
    new_list = []
    for i in range(len(nums_list)):
        if (i % 2) == 0:
            new_list.append(nums_list[i])
    return new_list


def exercise34(digit):
    months = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
              9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    return months.get(digit)


def exercise35(digit):
    season = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Лето", 6: "Лето", 7: "Лето", 8: "Лето",
              9: "Осень", 10: "Осень", 11: "Зима", 12: "Зима"}
    return season.get(digit)


def exercise36(list1, list2):
    return dict(zip(list1, list2))


def exercise38(arr):
    nueve = {}
    keys = list(arr.keys())
    values = list(arr.values())
    for i in range(len(arr)):
        nueve.update({values[i]: keys[i]})
    return nueve


def exercise40(num):
    dictionary = {}
    for i in range(1, num + 1):
        dictionary.update({i: i * i})
    return dictionary


def exercise54():
    prices = {
        "apple": 0.7,
        "eggs": 0.5,
        "cola": 2,
        "mango": 5
    }
    cart = {
        "apple": 2,
        "eggs": 10,
        "mango": 3
    }
    final = 0
    for price in prices:
        for products in cart:
            if price == products:
                final = final + prices[price] * cart[products]
    return final
