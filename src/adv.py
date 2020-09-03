from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ["rocks"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     ["An old gold necklace, it could be worth something :o"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     ["Wet Rocks", "torch", "baby penguin"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. You almost walk away but you see a small light shinning in the distance and you see they forgot some things!The only exit is to the south.""",
                     ["Diamonds", "amulet", "letter from the king that makes you the new king"]),
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
#
# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

print('Welcome to my little demo game. The rules are simple, you can go north(n), south(s), east(e),and west(w).To select and item found in a room, press the number (1-3) of the item! Find your way to the treasure room! Good Luck!')
# Write a loop that:
while True:
    #
    # * Prints the current room name
    # print(player.location)
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    vinputs = ['n', 's', 'e', 'w']
    command = input("> ").split(',')

    if command[0] == 'q':
        break
    elif command[0] == 'n':
        # check input, if valid call funciton
        # check if the player can move to the north
        player.move(command[0])

    elif command[0] == 's':
        player.move(command[0])
    elif command[0] == 'e':
        player.move(command[0])

    elif command[0] == 'w':
        player.move(command[0])

    elif command[0] == '1':
        player.additem(0)

    elif command[0] == '2':
        player.additem(1)

    elif command[0] == '3':
        player.additem(2)
    elif command[0] == 'drop' and command[1] == '1':
        player.dropitems(0)
        print("YOU DROP THAT SUCKER")
    elif command[0] == 'drop' and command[1] == '2':
        player.dropitems(1)
        print("YOU DROP THAT SUCKER")
    elif command[0] == 'drop' and command[1] == '3':
        player.dropitems(2)
        print("YOU DROP THAT SUCKER")
    else:
        print('Thats not a valid movement')
    print(player.location)
    player.print_items()
