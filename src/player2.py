# Write a class to hold player information, e.g. what room they are in
# currently.
class Player2:
    def __init__(self, location):
        self.location = location

    def move(self, keypress):
        wherabouts = getattr(self.location, keypress)
        if wherabouts is not None:
            self.location = wherabouts
        else:
            print("Sorry friend, no room there")

    def __str__(self):
        print(f"You are currently in {self.location}")
