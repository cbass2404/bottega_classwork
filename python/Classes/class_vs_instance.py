"""
class attribute is hard coded and belongs to all instances
instance attribute is soft coded and are specific to each instance
"""

# class Website:
#     def __init__(self, title):
#         self.title = title
#
#
# ws = Website('My Website Title')
# print(ws.__dict__)
#
# ws_two = Website('Second Title')
# print(ws_two.__dict__)


class DifferentWebsite:
    title = 'My Class Title'


dw = DifferentWebsite()
# print(dw.__dict__)
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)
