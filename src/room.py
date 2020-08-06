# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n = None
        self.e = None
        self.s = None
        self.w = None

    def __str__(self):
        return "You are now in {self.name}. {self.description}".format(self=self)
