# Write a class to hold player information, e.g. what room they are in
# currently.
from items import Item


class Player:
    def __init__(self, location, items=[]):
        self.location = location
        self.items = items

    def move(self, keypress):
        newRoom = getattr(self.location, keypress)
        if newRoom is not None:
            self.location = newRoom
            # print(self.location.name)

        else:
            print('Sorry, theres no room there')

    def __str__(self):
        return 'Location: {self.location}'.format(self=self)

    def print_items(self):
        print("Your items contents: ", [f"{i}" for i in self.items], '\n')

    def additem(self, keypress):
        # print(keypress)
        # print(self.location.items)
        self.items.append(self.location.items[keypress])
        self.location.items.pop(keypress)

    def dropitems(self, keypress):
        # print(self.items)
        # self.items.remove(keypress)
        boom = self.items.pop(keypress)
        print(boom)
        self.location.items.append(boom)
