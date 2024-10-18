import uuid


class User:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name):
        self.name = new_name

    def increment_rate(self, increment_value=1):
        self.rate += increment_value

    def ban_user(self):
        self.is_banned = True

    def unban_user(self):
        self.is_banned = False

    def repr(self):
        return (f"User(id={self.id}, "
                f"name={self.name}, "
                f"comments_count={self.comments_count}, "
                f"rate={self.rate}, "
                f"is_banned={self.is_banned})")
