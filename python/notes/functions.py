# functions in python

# def full_name(first, last):
#   print(f'{first} {last}')
#
#
# full_name('Kristine', 'Hudgens')
#
# def auth(email, password):
#   if email == 'kristine@hudgens.com' and password == 'secret':
#     print('You are authorized')
#   else:
#     print('You are not authorized')
#
#
# auth('kristine@hudgens.com', 'asdf')
#
# def hundred():
#   for num in range(1, 101):
#     print(num)
#
#
# hundred()
#
# def counter(max_value):
#   for num in range(1, max_value):
#     print(num)
#
#
# counter(51)

# def greeting():
#     print("Whatever you want")
#
#
# greeting()

# def greeting(name):
#     print(f"Hello, {name}")
#
#
# greeting('Daniel')

# TODO

# import operator
#
# def calc_two_numbers(op_type, first_num, second_num):
#     print(operator.(op_type)(first_num, second_num))
#
#
# calc_two_numbers(add, 2, 3)

# TODO

# returning values in functions for storage
#
# def full_name(first, last):
#     return f'{first} {last}'
#
#
# kristine = 'Kristine Hudgens'
#
# def greeting(name):
#     print(f'Hi {name}')
#
#
# greeting(kristine)

# import operator
#
# def sum_two_numbers(num_one, num_two):
#     return operator.add(num_one, num_two)
#
#
# result = sum_two_numbers(2, 8)
#
# print(result)

# nesting functions

# def greeting(first, last):
#     def full_name():
#         return f'{first} {last}'
#
#
#     print(f'Hi {full_name()}')
#
#
# greeting('Kristine', 'Hudgens')

# default arguments in functions

# def greeting(name = 'Guest'):
#     print(f'Hi {name}!')

# def some_function(collection = []):    # BAD practice to set default arguments on a list, it makes it mutable and
#     collection.append(1)               # shared between parts of programs
#     print(id(collection))
#     return collection
#
#
# print(some_function())
#
# # Other part of program
# print(some_function())

# # utilizing named function arguments in python

# def full_name(first, last):
#     print(f'{first} {last}')
#
#
# full_name(last = 'Hudgens', first = 'Kristine')

# # guide to function argument unpacking
# best practice to name unpacked arguments as arg, * makes it optional

# def greeting(time_of_day, *args):
#     print(f"Hi {''.join(args)}, I hope that you are having a good {time_of_day}")
#
#
# greeting('Morning', 'Tiffany', 'Hudgens')
# greeting('Afternoon', 'Kristine', 'M', 'Hudgens')

# keyword arguments in python functions
# makes a dictionary of key and value from arguments and keyword of argument
# kwargs = key word argument, best practice and common convention to use this word

# def greeting(**kwargs):
#     if kwargs:
#         print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a great day!")
#     else:
#         print(f"Hi Guest, have a great day!")
#
#
# greeting(first_name='Kristine', last_name='Hudgens')
# greeting()

# using all positional, *args and **kwargs in one function

# def greeting(time_of_day, *args, **kwargs):
#     print(f"Hi {' '.join(args)}, I hope that you are having a great {time_of_day}")
#
#     if kwargs:
#         print('Your tasks for the day are:')
#         for key, val in kwargs.items():
#             print(f"{key} => {val}")
#
#
# greeting('Morning',
#          'Kristine', 'Hudgens',
#          first = 'Empty dishwasher',
#          second = 'Take pup outside',
#          third = 'Math homework')

# LAMBDA in functions

# full_name = lambda first, last: f'{first} {last}'
#
# # print(full_name('Kristine', 'Hudgens'))
#
# def greeting(name):
#     print(f'Hi there {name}')
#
#
# greeting(full_name('Tiffany', 'Hudgens'))

# def sum(num_one, num_two):
#     return num_one + num_two

num_sum = lambda num_one, num_two: sum(num_one, num_two)


print(num_sum(1, 2))
