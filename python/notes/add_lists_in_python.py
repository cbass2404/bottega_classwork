tags = ['python', 'development', 'tutorials', 'code']

# Nope

# tags[-1] = 'Programming'

# extend is used to add to a pre-existing list, can not be used in a new variable

# tags.extend('Programming') #adds each part of a string to the list as individual items

# tags.extend(['Programming']) #adds the element as a single whole

# new_tags = tags + 'Programming' # can not be used like this, python will not combine data types

new_tags = tags + ['Programming']

print(new_tags)