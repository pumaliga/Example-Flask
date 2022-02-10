class Registration:

    def __init__(self):
        self.user_to_reg = []

    def create(self, username, password, time_register):
        self.user_to_reg.append(User(password=password, username=username, time_register=time_register))

    def exist_user(self, username):
        search = username
        for i in self.user_to_reg:
            if i.username == search:
                return False
        return True

    def update_time(self, username, password, time_register):
        for user in self.user_to_reg:
            if user.username == username:
                user.password = password
                user.time_register = time_register


class User:

    def __init__(self, username='', password='', time_register=''):
        self.username = username
        self.password = password
        self.time_register = time_register


new_user = Registration()

