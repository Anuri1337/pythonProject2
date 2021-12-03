#переменные для ввода
"""
3
f a 44
g r 56

d a 90
f g 78
p o 67

t y 54
"""
def fill_set():
    _set = dict()
    str = input()
    while str!='':
        _str = str.split()
        _set[_str[0] +" "+ _str[1]] = int(_str[2])
        str = input()
    return _set

count = int(input())
list_dict = [0] * count
for i in range (count):
    list_dict[i]=fill_set()

#_m=fill_set()
#_p=fill_set()
#_i=fill_set()

print(list_dict)