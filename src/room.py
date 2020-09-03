# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=['nothing, haha loser']):
        self.name = name
        self.description = description
        self.items = items
        self.n = None
        self.e = None
        self.s = None
        self.w = None

    def __str__(self):
        if self.items == None:
            print("There are no items here")
        else:
            return "You are now in {self.name}. {self.description}. You look around for items and find... {self.items}".format(self=self)

    def print_items(self):
        for id, p in enumerate(self.items):
            print(f"{id}: {p}")
            print()
