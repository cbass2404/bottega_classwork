# sentence = 'The quick brown fox jumped'
# sentence -> variable
# 'The quick brown fox jumped' -> string
# = -> assignment

# sentence = 'The quick brown fox jumped'
# sentence_two = sentence.upper()

# print(sentence)
# print(sentence_two)

# sentence = 'the quick brown fox jumped'.capitalize()

# print(sentence)

# sentence = 'the quick brown fox jumped'.title()

# print(sentence)

# sentence = 'THE QUICK BROWN FOX JUMPED'.lower()

# print(sentence)

# Pull a part out of a variable
# The quick brown fox jumps over the lazy dog
# Index start of zero

# starter_sentence = 'The quick brown fox jumps over the lazy dog'
# print(starter_sentence[4])

# starter_sentence = 'The quick brown fox jumps over the lazy dog'
# first = starter_sentence[0]
# second = starter_sentence[1]
# third = starter_sentence[2]
# new_sentence = first + second + third
# print(new_sentence)

# starter_sentence = 'The quick brown fox jumps over the lazy dog'
# first_word = starter_sentence[0:2]
# new_sentence = first_word
# print(new_sentence)

# starter_sentence = 'The quick brown fox jumps over the lazy dog'

# new_sentence = 'Thy' + starter_sentence[3:]
# print(new_sentence)

# Heredocs

# content = """
# Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

# Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

# Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
# """.strip() # .strip() cleans up any extra lines in content

# print(content)

# Heredoc

# content = """
# Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

# Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

# Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
# """
# print(repr(content))

# content = """
# Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

# Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

# Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
# """

# print(repr(content))

# long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'

# print(long_string)

# String Interpolation

# name = 'Kristine'
# greeting = f'Hi {name}' # f stands for format flag to set string format
# print(greeting)

# name = 'Kristine'
# greeting = f'This is my {{bracket}} blog post' # double brackets to show brackets in a string
# print(greeting)

# name = 'Kristine'
# product = 'Python elearning course'

# #must use f to make message formatted according to input

# email_content = f"""
# Hi {name},

# Thank you for purchasing the {product}!

# Regards,

# Super Sales Team
# """

# print(email_content)

# name = 'Kristine'
# age = 12
# product = 'Python eLearning course'

# greeting = 'Hi {0}, you are as {1} years old and you have purchased: {2}... -{3}'.format(name, age, product, 'Cory')

# # .format is used to fill in the index of the called items to the string

# print(greeting)

# how to find items in a variable

# sentence = 'The quick brown fox jumps over the lazy dog.'

# query = sentence.find('quick') # .find returns -1 if no value found

# print(query) #returns the index of the first letter of the search

# sentence = 'The quick brown fox jumps over the lazy dog.'

# query = sentence.index('brown') # .index returns error if no value found, stops all code from functioning

# print(query)

# sentence = 'The quick brown fox jumps over the lazy dog.'

# query_one = 'oops' in sentence # in query returns boolean as result only
# query_two = 'lazy' in sentence

# print(query_one)
# print(query_two)

# sentence = 'The quick brown fox jumps over the lazy dog.'

# sentence = sentence.replace('quick', 'slow') # takes two arguments, the word to find and the word to replace it with

# print(sentence)

# sentence = 'The quick brown fox jumps over the lazy dog.'

# print(sentence[-1::-3])

# url = 'https://google.com'

# # print(url.strip('https://'))

# url = url.lstrip('https://')
# url = url.rstrip('.com')
# url = url.capitalize()  # strips and formats the content of the variable

# print(url) 

# Partition Functions

# heading = "Python: An Introduction"

# header, _, subheader = heading.partition(': ') # partition takes an argument in this case, Python is first partition, second is : , third is An Introduction. This is called a tuple string, where you break a string into multiple elements. _ is used to label a partition you want no name for. This is best practice 

# print(header + _)
# print(subheader)

# split funtion

# tags = 'python,coding,programming,development'

# list_of_tags = tags.split(',')

# print(list_of_tags)

# list_of_tags = tags.split() #with no arguments it splits into a single split
# print(list_of_tags)

# heading = "Python: An Introduction"

# heading_list = heading.split(': ')

# print(heading_list)

# check string as alphanumeric or numbers

# api_data = '5'
# greeting = 'Hi'

# # print(api_data.isalpha())
# # print(greeting.isalpha()) # can return false if a space is present

# print(api_data.isnumeric())
# print(greeting.isnumeric()) # always returns a accurate response

# product_i = '123abc' # string
# product_id = 123 # integer
# sale_price = 14.99 #float
# tip_percentage = 1/5 #percentages
# new_product = 150 #integer

# # print(sale_price + new_product)
# print(product_id + new_product)

# Mathematical operators

# print('Addition')
# print(100 + 42)
# print('---')
# print('Subtraction')
# print(100 - 42)
# print('---')
# print('Division')
# print(100 / 42)
# print(100 / 38)
# print('---')
# print('Floor Division')
# print(100 // 42)
# print(100 // 38)
# print('---')
# print('Multiplication')
# print(100 * 42)
# print('---')
# print('Modulus')
# print(100 % 42)
# print('---')
# print('Exponents')
# print(100 ** 42)

# Assignment Operators

# total = 100
# total -+ 10
# total *= 2
# total /= 2
# total //= 1.3
# total **= 2
# total %= 3

# Decimal vs Float in python, best to use decimal in anything needing precision

# from decimal import Decimal

# # product_cost = 88.40
# # commission_rate = 0.08
# # qty = 450

# # product_cost += (commission_rate * product_cost)
# # print(product_cost * qty) # 42962.4

# product_cost = Decimal(88.40)
# commission_rate = Decimal(0.08)
# qty = 450

# product_cost += (commission_rate * product_cost)
# print(product_cost * qty) # 42962.40000000000282883716451

# # Use of complex numbers for scientific calculations

# from decimal import Decimal

# product_cost = 88.80
# commission_rate = 0.08
# qty = 450

# print(int(product_cost))
# print(Decimal(product_cost))
# print(complex(commission_rate))

# Absolute value of numbers

# loss = -20.25
# product_cost = 89.99

# print(abs(loss))

# # Import math functions and examples

# import math

# loss = -20.25
# product_cost = 89.99

# print(math.floor(product_cost))
# print(math.ceil(product_cost))
# print(loss)
# print(math.floor(loss))
# print(math.ceil(loss))
# print(abs(math.floor(loss) - math.ceil(loss)))
# print(round(product_cost))
# print(math.sqrt(product_cost))
# print(math.pow(5, 2)) # pow is the same as using **, however pow is more accurate