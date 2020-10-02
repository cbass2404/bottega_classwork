# answer = False
#
# if answer == False:
#     answer = True
#
# print(answer)

# def watermelonparty(watermelons):
#     if watermelons > 50:
#         print(True)
#     else:
#         print(False)
#
#
# watermelonparty(51)

# def kid(age):
#     if age > 15:
#         print('You can get a license')
#     elif age == 15:
#         print("You can get a permit, but can't get a license")
#     else:
#         print("You are not old enough for a permit or license.")
#
# kid(14)
# kid(15)
# kid(16)

# role = 'guest'
#
# auth = 'can access' if role == 'admin' else 'cannot access'
#
# # if role == 'admin':
# #     auth = 'can access'
# # else:
# #     auth = 'cannot access'
#
# print(auth)

# def ageverification(age):
#     if age > 25:
#         print('can rent a car')
#     else:
#         print("can't rent a car")

# def ageverification(age):
#     print("Can rent a car") if age > 25 else print("Can't rent a car")
#
#
# ageverification(26)
# ageverification(25)

# checking if a value is in a string or list

# sentence = 'The quick brown fox jumped over the lazy Dog'
# word = 'dog'
#
# if word.lower() in sentence.lower():
#   print('The word is in the sentence')
# else:
#   print('The word is not in the sentence')
#
#
# nums = [1, 2, 3, 4]
#
# if 3 in nums:
#   print('The number was found')
# else:
#   print('The number was not found')

# sentence = 'Python is the best!'
#
# def word_finder(word, variable):
#     if word in variable:
#         print('The word is in the sentence')
#     else:
#         print('The word is not in the sentence')
#
#
# word_finder('Python', sentence)
# word_finder('Balloon', sentence)

# nums = [1, 2, 3, 4]
#
# def item_finder(num, list_name):
#     if num in list_name:
#         print(f"{num} found.")
#     else:
#         print(f"{num} not found")
#
#
# item_finder(2, nums)
# item_finder(0, nums)

# compound conditionals in python

# username = 'jonsnow'
# email = 'jon@snow.com'
# password = 'thenorth'
#
# if username == 'jonsnow' and password == 'thenorth':
#   print('Access permitted')
# else:
#   print('Not allowed')
#
#
# if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
#   print('Access permitted')
# else:
#   print('Not allowed')
#
#
# if username == 'jonsnow' or password == 'thenorth':
#   print('Access permitted')
# else:
#   print('Not allowed')
#
#
# logged_in = True
# standard_user = False
#
# if logged_in and not standard_user:
#   print('You can access the admin dashboard')
# else:
#   print('You can only access the standard dashboard')

# a = 200
# b = 33
# c = 500
# if a > b and a < c:
#     print("Both conditions are True")
#
# if a > b or a > c:
#     print("At least one of the conditions are True")
