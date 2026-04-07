class UserManager:
    def __init__(self):
        self.users = []

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
        try:
            self.users.remove(name)
            print(f'User {name} was deleted')
        except ValueError:
            print('There is no such username')



a = UserManager()
b = UserManager()
a.add_user("Gasan")
print(a.get_users())

users = ["A", "B", "C"]
manager = UserManager.from_list(users)
print(manager.get_users())
a.remove_user('Gasan')
print(a.get_users())