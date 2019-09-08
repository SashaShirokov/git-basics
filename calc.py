def add(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)


def mult(a, b):
    print(a * b)


def div(a, b):
    print(a / b)


add(4, 8)
sub(7, 11)
mult(5, 8)
div(10, 2)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []
for i in nums:
    my_list.append(i)
print(my_list[::-1])

my_list = [i for i in nums]
print(my_list)


l = [n * n for n in nums]
print(l)
