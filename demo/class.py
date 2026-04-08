class UserManager:
    def __init__(self):
        self.users = []

    def __str__(self):
        return f'{self.__class__.__name__}(users={self.users})'

    def add_user(self, name):
        self.users.append(name)
        return self.users

    def get_users(self):
        return self.users.copy()

    @classmethod
    def from_list(cls, users_list):
        obj = cls()
        obj.users = users_list.copy()
        return obj

    def remove_user(self, name):
        old_len = len(self.users)
        new_users = [user for user in self.users if user != name]
        self.users = new_users
        if len(self.users) < old_len:
            print(f'User {name} was deleted')
        else:
            print(f'There is no such user {name}')


a = UserManager()
b = UserManager()
a.add_user("Gasan")
print(a.get_users())

users = ["A", "B", "C"]
manager = UserManager.from_list(users)
print(manager.get_users())
a.remove_user('Fuck')
print(a)