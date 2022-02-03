import math
import threading


def calculation(a, b, c):
    D = (b ** 2) - (4 * a * c)
    if D > 0:
        value1 = (-b - math.sqrt(D)) / (2 * a)
        value2 = (-b + math.sqrt(D)) / (2 * a)
        print(f" Solution are: {value1} and {value2}")
    elif D == 0:
        value1 = value2 = -b / (2 * a)
        print(f"Solution are one: {value1} or {value2}")
    else:
        print("Not solution!")


t1 = threading.Thread(target=calculation(3, 17, 9))
t2 = threading.Thread(target=calculation(15, 20, 10))
t1.start()
t2.start()