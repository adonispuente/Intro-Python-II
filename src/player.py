# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, location):
        self.location = location

    def move(self, keypress):
        newRoom = getattr(self.location, keypress)
        if newRoom is not None:
            self.location = newRoom
            # print(self.location.name)

        else:
            print('Sorry, theres no room there')

    def __str__(self):
        return 'Location: {self.location}'.format(self=self)
