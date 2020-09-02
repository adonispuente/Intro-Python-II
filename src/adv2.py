from room import Room
from player2 import Player2
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south, but you see a bunch of Minotaurs eating a freshly made salad. Underneath this salad there seems to be some chocolate, which I hear the Queen pays a hefty amount for. Minotaurs HATE chocolate so they wont eat it, but if you enter 'boo', you might be able to scare off the vegetarian Minotaurs and get to the chocolate!"""),
}


# Link rooms together

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']

#
# Main

# player = Player(room['outside'])

#
# player = Player2(room['outside'])
player2 = Player2(room['outside'])
print("Welcome to this magical land! Explore the cave and come out with riches, or die and absolutely horrific death! >:D")
# Make a new player object that is currently in the 'outside' room.
while True:
    # Write a loop that:

    # If the user enters "q", quit the game.
    vinputs = ('n', 's', 'e', 'w')
    print(player2.location)

    command = input("> ").split(',')

    if command[0] == 'n' or command[0] == 's' or command[0] == 'w' or command[0] == 'e':
        player2.move(command[0])
    elif command[0] == 'q':
        print('looks like its game over! See ya next time!')
        sys.exit()
    elif player2.location == room['treasure'] and command[0] == 'boo':
        print('You scared off the Vegetarian Minotaurs and managed to snatch the chocolate! With the money you get from the Queen, Lady Bebop, youll be set for life! Congratulations Adventure, now leave me alone!')
        sys.exit()
    else:
        print("That is not a valid location")
