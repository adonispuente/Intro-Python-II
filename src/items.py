class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        print(f"{self.name} does {self.desc}".format(self=self))
