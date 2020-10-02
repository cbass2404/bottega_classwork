"""
remove_first_and_last(list_to_clean)
html = ['<h1', 'Some content', '<h1>']

remove_first_and_last(html)
=> 'some content'

html_2 = ['<h1', 'Some content', 'more', '<h1>']

remove_first_and_last(html_2)
=> ['some content', 'more']
"""

# popsicle_flavor = ['cherry', 'watermelon', 'apple', 'pineapple', 'strawberry', 'banana']
#
#
# def remove_first_last(target):
#     target = target[1:-1]
#     print(target)
#
# remove_first_last(popsicle_flavor)

# popsicle_flavor = ['cherry', 'watermelon', 'apple', 'pineapple', 'strawberry', 'banana']
#
# new_list = []
#
#
# def remove_first_last(target, new_target):
#     new_target.append(target.pop(0))
#     new_target.append(target.pop(-1))
#     print(target)
#     print(new_target)
#
#
# remove_first_last(popsicle_flavor, new_list)

# popsicle_flavor = ['cherry', 'watermelon', 'apple', 'pineapple', 'strawberry', 'banana']
#
#
# def remove_first_last(target, new_target):
#     new_target.append(target.pop(0))
#     new_target.append(target.pop(-1))
#     print(target)
#     print(new_target)

popsicle_flavor = ['cherry', 'watermelon', 'apple', 'pineapple', 'strawberry', 'banana']


def remove_first_last(target):
    if len(target) > 2:
        _, *target, _ = target
        return target
    else:
        print('Not long enough')


remove_first_last(popsicle_flavor)

# Jordans solution
# best practice is to use _ for variables not to be reused

# def remove_first_and_last(list_to_clean):
#     _, *content, _ = list_to_clean
#     return content
