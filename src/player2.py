# Write a class to hold player information, e.g. what room they are in
# currently.
class Player2:
    def __init__(self, location, items=[]):
        self.location = location
        self.items = items

    def move(self, keypress):
        wherabouts = getattr(self.location, keypress)
        if wherabouts is not None:
            self.location = wherabouts
        else:
            print("Sorry friend, no room there")

    def __str__(self):
        print(f"You are currently in {self.location}")

    def additems(self, keypress):
        self.items.append(self.location.items[keypress])
        self.location.items.pop(keypress)

    def dropitems(self, keypress):
        thing = self.items.pop(keypress)
        self.location.items.append(thing)

    def print_items(self):
        print("These are your current items:  ")
        for id, p in enumerate(self.items):
            print(f"{id + 1}: {p}")
            print()
