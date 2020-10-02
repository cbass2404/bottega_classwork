# tuples use ()

# Tuple is immutable
# List: mutable

# post = ('Python Basics', 'Intro guide to Python', 'Some cool Python content')

# # post.sort()

# title, sub_heading, content = post

# # title = post[0]
# # sub_heading = post[1]
# # content = post[2]

# print(title)
# print(sub_heading)
# print(content)

# post = ('Python Basics', 'Intro guide to Python', 'Some cool Python content')

# print(id(post))
# print(id(post))

# post += ('published',)

# print(id(post))

# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)

# post = ('Python Basics', 'Intro guide to Python', 'Some cool Python content')

# list_one = ['right', 'left', 'backwards',]

# post += (list_one,)

# print(post)

# post = ('Python Basics', 'Intro guide to Python', 'Some cool Python content')

# print(post[::2])

# post = ('Python Basics', 'Intro guide to Python', 'Some cool Python content', 'published')

# post = post[1:]

# print(post)

# removing specific element (messy/not recommended)
# post = list(post)

# post.remove('published')

# post = tuple(post)

# print(post)

# using tuples as dictionary key

# priority_index = {
#     (1, 'premier'): [1, 34, 12],
#     (1, 'mvp'): [84, 22, 24],
#     (2, 'standard'): [93, 81, 3],
# }

# print(list(priority_index.keys()))

# matrix = a set of nested functions
# zip automates this

# positions = ['2b', '3b', 'ss', 'dh']
# players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# scoreboard = zip(positions, players)

# print(list(scoreboard))

# datatype set
# only uses unique elements, will not shot duplicates of an element

# tags = {
#     'python',
#     'coding',
#     'tutorials',
#     'coding',
# }

# print(tags)

# print(tags[0]) #does not work

# query_one = 'python' in tags

# query_two = 'ruby' in tags

# # returns a boolean true or false statement

# print(query_one)
# print(query_two)

# tags_one = {
#     'python',
#     'coding',
#     'tutorials',
#     'coding',
# }

# tags_two = {
#     'ruby',
#     'coding',
#     'tutorials',
#     'development',
# }

# merging a tag

# merged_tags = tags_one | tags_two
# print(merged_tags)
# print(type(merged_tags))

# tags in tags_one but not in tags_two
# builds a "venn diagram" to show what is exclusive to the set specified

# exclusive_to_tag_one = tags_one - tags_two
# print(exclusive_to_tag_one)

# exclusive_to_tag_two = tags_two - tags_one
# print(exclusive_to_tag_two)

# shared_between_tags = tags_one & tags_two
# print(shared_between_tags)