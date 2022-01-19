# 1. Double_result
def double_result(func):
    def inner(a, b):
        return 2 * func(a, b)

    return inner


def add(a, b):
    return a + b


@double_result
def add(a, b):
    return a + b


print(add(5, 5))


# 2. Only_odd_parameters
def only_odd_parameters(func):
    def inner(*args):
        result = func(*args)
        for i in args:
            if i % 2 == 0:
                print("Please use only odd numbers!")
                break
            else:
                return result

    return inner


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10
add(4, 4)  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


multiply(2, 3, 4, 5, 6)


# 3. * Logged
def logged(func):
    def inner(*args):
        print(f'you called func {args}')
        result = func(*args)
        print(f'it returned {result}')
        return result

    return inner


@logged
def func(*args):
    return 3 + len(args)


func(4, 4, 4)


# you called func (4, 4, 4)
# it returned 6

# 4. Type_check
def type_check(correct_type):
    def inner(func):
        def wrapper(*args):
            if isinstance(*args, correct_type):
                return func(*args)
            else:
                print(f"Wrong Type: {type(*args)}")

        return wrapper

    return inner


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
