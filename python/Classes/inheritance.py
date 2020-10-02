"""
put the class name in parenthesis of another class to inherit the methods and attributes of the class
"""


class User:
    def __init__(self, email, f_name, l_name):
        self.email = email
        self.f_name = f_name
        self.l_name = l_name

    def greeting(self):
        return f'Hi {self.f_name} {self.l_name}'


class AdminUser(User):
    @staticmethod
    def active_users():
        return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.greeting())
print(tiffany.active_users())
