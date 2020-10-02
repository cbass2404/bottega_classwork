# """
# User Database Query
# Kristine
# Tiffany
# Jordan
# """

# # lists

# users = ['Kristine', 'Tiffany', 'Jordan']

# users.insert(1, 'Cory')

# users.insert(5, 'Kristine')

# users.append('Dan')

# print(users)
            
    
        

# find_index(users, 'Kristine', 0)

# # pop method, returns value to be reused

# users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

# print(users)

# users.remove('Jordan')

# print(users)

# popped_user = users.pop()

# print(popped_user)
# print(users)

# del users[0]

# print(users)

# # nested lists and multiple data types in lists

# users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

# ids = [1, 2, 3, 4]

# mixed_list = [42, 10.3, 'Altuve', users]

# print(mixed_list)

# user_list = mixed_list.pop()

# print(user_list)
# print(mixed_list)

# nested_lists = [[123], [234], [345]]

# search through negative indexes

# tags = ['python', 'development', 'tutorials', 'code']

# number_of_tags = len(tags)
# last_item = tags[-1]
# index_of_last_item = tags.index(last_item)

# print(number_of_tags)
# print(last_item)
# print(index_of_last_item)

# Sorting lists in Python

# tags = ['python', 'development', 'tutorials', 'code']

# print(tags)

# tags.sort()

# print(tags)

# tags.sort(reverse=True)

# print(tags)

# totals = [234, 1, 543, 2345]

# totals.sort(reverse=True)

# print(totals)

# Search queries in urls

# https://www.google.com/search?q=python+development+tutorial

# https://www.google.com/search?q=python+development+tutorial

# uri = 'https://www.google.com/search?q='
# tags = ['python', 'development', 'tutorial']
# formatted_tags = '+'.join(tags)
# query_uri = f'{uri}{formatted_tags}'

# print(query_uri)

# tags = ['python', 'development', 'tutorials', 'code']

# tag_range = tags[2:]
# tag_range = tags[0:2]
# tag_range = tags[:2]
# tag_range = tags[0:-1]

# print(tag_range)

# # Implementing Ranges and slices in python

# tags = [
#   'python',
#   'development',
#   'tutorials',
#   'code',
#   'programming',
#   'computer science'
# ]

# tag_range = tags[1:-1:2]
# tag_range = tags[::-1]

# print(tag_range)

# tags.sort(reverse=True)

# print(tags)

# guide to sorted function in Python

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices, reverse=True)

print(sorted_list)