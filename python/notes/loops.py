# import random
# loops in python

# for loops run as many times as there are items in the selected variable, while loops will continue until a set parameter is met or continue indefinitely in a infinite loop

# works same for lists and tuples

# players = ['Altuve', 'Bregman', 'Correa', 'Gattis',]
# players = ('Altuve', 'Bregman', 'Correa', 'Gattis',)

# for player in players:
#    print(player)

# players = {
#    '2b': 'Altuve',
#    '3b': 'Bregman',
#    'ss': 'Correa',
#    'dh': 'Gattis',
# }

# for position, player in players.items():
#     print('Position', position)
#     print('Player name', player)

# members = ['Cory', 'Boli', 'Zachary', 'Jayden', 'Evalyn']

# for member in members:
#     print('Name', member)

# user = {
#     'username': 'Daniel',
#     'email': 'danielfloyd@bottega.tech',
#     'phone': 8888279890,
#     }

# for key, value in user.items():
#     if value == 'Daniel':
#         value = 'aDeiln'
#     if value == 8888279890:
#         random.seed()
#         value = random.randint(1000000000, 9999999999)
#     print(key, value)        

# for key, value in user.items():
#     print('Key => ' + key)
#     print('Value => ' + value)
    
# # for key, value in user.items():
# #     print('Key => ' + key)
# for key in user.keys():
#      print('Key => ' + key)

# # for key, value in user.items():
# #     print('Value => ' + value) 
# for value in user.values():
#     print('Value => ' + value)


# unsorted_string = 'ksjdvnsasdkf'
# sorted_string = unsorted_string.join((sorted(unsorted_string)))

# print(sorted_string)

# name = 'Cory'

# for char in name:
#     print(char)

# for num in range(1, 11, 3):
#     print(num)

# for number in range(6, 16):
#     print(number)
    
# for number in range(10, 31, 2):
#     print(number)

# usernames = [
#     'jon',
#     'tyrion',
#     'cersei',
#     'sansa',
# ]

# for username in usernames:
#     if username == 'cersei':
#         print(f'Sorry, {username} you are not allowed')
#         continue
#     else:
#         print(f'{username} is allowed')

# for username in usernames:
#     if username == 'cersei':
#         print(f'{username} was found at index {usernames.index(username)}')
#         break
#     print(username)

# cereals = [
#     'honey bunches of oats',
#     'cinnamon toast crunch',
#     'shredded wheat', 
#     'lucky charms',
# ]

# for cereal in cereals:
#     if cereal == 'shredded wheat':
#         print(f'{cereal} is Gross')
#         break
#     else:
#         print(f'{cereal} is delicious')

# While loops - while loops can run indefinitely & for loops only run once for each item.

# nums = list(range(1,100))

# # print(nums)
# # for num in nums:
# #     print(num)

# while len(nums) > 0 :
#     print(nums.pop())

# def guessing_game():
#     while True:
#         print('What is your guess')
#         guess = input()
        
#         if guess == '42':
#             print('You correctly guess it!')
#             return False
#         else:
#             print(f'No, {guess} is not the answer. Please try again\n')

# guessing_game()

# dog_house = ['bear', 'velvet', 'hiro', 'sugar']

# data = 0
# while data < len(dog_house):
#     print(dog_house[data])
#     data += 1

# legacy_customers = ['Alice', 'Bob',]
# new_customers = ['Tiffany', 'Kristine',]

# # raw_db = [legacy_customers, new_customers]
# # print(raw_db)

# for customers in new_customers:
#     legacy_customers.append(customers)

# print(legacy_customers)

# numbers = [1,2,3,4,5,6]
# result = []

# for number in numbers:
#     result.append(number + 1)

# print(result)

# Using list comprehension in python

# num_list = range(1, 11)
# cubed_nums = []

# for number in num_list:
#     cubed_nums.append(number ** 3)

# print(cubed_nums)

# num_list = range(1, 11)
# # cubed_nums = [num ** 3 for num in num_list]

# # print(cubed_nums)

# even_numbers = [num for num in num_list if num % 2 == 0 ]
# print(even_numbers)

# pycharm

"""
*This challenge wasn't given in class*
- Create a variable called result and use list comprehension to increment each number from your numbers list by 1
- Print the result
- Your printout should be [2, 3, 4, 5, 6, 7]
"""
numbers = [1,2,3,4,5,6]

result = [ num + 1 for num in numbers]

print(result)
