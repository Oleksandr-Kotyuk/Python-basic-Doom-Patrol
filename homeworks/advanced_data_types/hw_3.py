#1
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a))
#9790720
print(id(str_b))
#140644059073328
print(id(set_c))
#140644059040000
print(id(lst_d))
#140644059942656
print(id(dict_e))
#140644059894464

#2
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
#140069889015552

#3
print(type(int_a))
#<class 'int'>
print(type(str_b))
#<class 'str'>
print(type(set_c))
#<class 'set'>
print(type(lst_d))
#<class 'list'>
print(type(dict_e))
#<class 'dict'>

#4
print(isinstance(int_a, int))
#True
print(isinstance(str_b, str))
#True
print(isinstance(set_c, set))
#True
print(isinstance(lst_d, list))
#True
print(isinstance(dict_e, dict))
#True

#5
print("Anna has {} apples and {} peaches.".format(4, 6))
#Anna has 4 apples and 6 peaches.
#6
print("Anna has {0} apples and {1} peaches.".format("four", "six"))
#Anna has four apples and six peaches.
#7
print("Anna has {0} apples and {sx} peaches.".format("four", sx="six"))
#Anna has four apples and six peaches.
#8
print("Anna has {0:4} apples and {1:3} peaches.".format(4, "six"))
#Anna has    4 apples and six peaches.

#9
app = 7
peach = 13
print(f"Anna has {app} apples and {peach} peaches.")
#Anna has 7 apples and 13 peaches.

#10
app = 5
peach = 9
print("Anna has %d apples and %d peaches." % (app, peach))
#Anna has 5 apples and 9 peaches.

#11
app = 3
peach = 8
data_dict = {"ap": app, "pea": peach}
print("Anna has %(ap)d apples and %(pea)d peaches." % data_dict)
#Anna has 3 apples and 8 peaches.

#12
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
#[0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

#13
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
#[0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

#14
dict_comprehension = {d: d ** 2 for d in range(1, 11) if d % 2 == 1}
print(dict_comprehension)
#{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

#15
dict_comprehension = {d: d ** 2 if d % 2 == 1 else d // 0.5 for d in range (1, 11)}
print(dict_comprehension)
#{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

#16
x = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        x[num] = num ** 3
print(x)
#{0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

#17
x = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        x[num] = num ** 3
    else:
        x[num] = num
print(x)
#{0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

#18
foo = lambda x, y: x if x < y else y
print(foo(5, 7))
#5

#19
def foo(x, y, z):
    if x < y and x > z:
        return z
    else:
        return y
print(foo(3, 5, 7))
#5

#20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
#[1, 5, 13, 15, 18, 24, 33, 55]

#21
print(sorted(lst_to_sort, reverse=True))
#[55, 33, 24, 18, 15, 13, 5, 1]

#22
new_lst_to_sort=list(map(lambda x: x * 2, lst_to_sort))
print(new_lst_to_sort)
#[10, 36, 2, 48, 66, 30, 26, 110]

#23
def power(list_A, List_B):
    return [ list_A[x]**list_B[x] for x in range(0, 3)]
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(power(list_A, list_B))
#[32, 729, 16384]

#24
import functools

fo = lambda a, b: a + b
foo = functools.reduce(fo, lst_to_sort)
print(foo)
#164

#25
new_list = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(new_list)
#[5, 1, 33, 15, 13, 55]

#26
lst_neg=list(filter(lambda x: x<0, range(-10, 10)))
print(lst_neg)
#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

#27
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_3 = list(filter(lambda x: x in list_1, list_2))
print(list_3)
#[2, 3, 5, 7]