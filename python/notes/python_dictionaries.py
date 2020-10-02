# dictionaries are defined by curly braces and not brackets. Best practice is to place on multiple lines as below:

# players = {
#     "ss": "Correa",
#     "2b": "Altuve",
#     "3b": "Bregman",
#     "DH": "Gattis",
#     "OF": "Springer",
# }

# second_base = players['2b']
# designated_hitter = players['DH']

# print(designated_hitter)

# nested collections in dictionaries

# teams = {
#     "astros": ["Altuve", "Correa", "Bregman"],
#     "angels": ["Trout", "Pujos"],
#     "yankees": ["Judge", "Stanton"],
# }

# astros = teams['astros']

# print(astros)
# print(teams['angels'])
# print(teams['yankees'])

# adding to dictionaries in python

# teams = {
#     "astros": ["Altuve", "Correa", "Bregman"],
#     "angels": ["Trout", "Pujos"],
#     "yankees": ["Judge", "Stanton"],
# }

# teams['red sox'] = ['Price', 'Betts']

# print(teams)

# Daniels example:

# person = {
#     "name": "Daniel",
#     "age": 36,
#     "dead": False,
#     "fav_numbers": [1, 2, 3, 4],
#     "class_mates": [
#         {"name": "Cory"},
#         {"name": "Zac"},
#         {"name": "Boli"},
#         {"name": "Eva"},
#         {"name": "Jayden"},
#     ]
# }

# person["state"] = "Utah"

# person["class_mates"].append({"name":"Sally"})

# print(person)

# players = {
#     "ss": "Correa",
#     "2b": "Altuve",
#     "3b": "Bregman",
#     "DH": "Gattis",
#     "OF": "Springer",
# }

# player_names = list(players.copy().values())

# print(player_names)

# teams = {
#     "astros": ["Altuve", "Correa", "Bregman"],
#     "angels": ["Trout", "Pujos"],
#     "yankees": ["Judge", "Stanton"],
#     "red sox": ["Price", "Betts"],
# }

# team_groupings = teams.items()

# print(type(team_groupings))
# print(len(team_groupings))
# print(team_groupings)
# print(list(team_groupings)[1][1][0])

# dishes = {
#     'eggs': 2,
#     'sausage': 1,
#     'bacon': 3,
# }

# dish = list(dishes)

# print(dishes.keys())
# print(dishes.values())
# print(dishes.items())
# print(dishes.keys())

# teams = {
#     "astros": ["Altuve", "Correa", "Bregman"],
#     "angels": ["Trout", "Pujos"],
#     "yankees": ["Judge", "Stanton"],
#     "red sox": ["Price", "Betts"],
# }

# removed_team = teams.pop('yankees', 'No team found by that name')

# print(teams)
# print(removed_team)

# teams = [
#     {
#         'astros': {
#             '2B': 'Altuve',
#             'SS': 'Correa',
#             '3B': 'Bregman',
#         }
#     },
#     {
#         'angels': {
#             'OF': 'Trout',
#             'DH': 'Pujols',
#         }
#     }
# ]

# # print(teams[0])

# angels = teams[1].get('angels', 'Team not found')

# print(list(angels.values())[1])

