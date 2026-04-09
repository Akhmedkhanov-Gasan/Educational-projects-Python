class UserManager:
    def __init__(self):
        self.users = []

    def __str__(self):
        return f'{self.__class__.__name__}(users={self.users})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, list):
            return self.users == other
        if not isinstance(other, UserManager):
            return False
        return self.users == other.users

    def __len__(self):
        return len(self.users)

    def __contains__(self, item):
        return item in self.users

    def __iter__(self):
        return iter(self.users)

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

a = UserManager.from_list(["A", "B"])
b = UserManager.from_list(["A", "B"])
c = UserManager.from_list(["A"])
