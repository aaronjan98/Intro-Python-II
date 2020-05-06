from room import Room
from player import Player

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
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
 #Is
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


'''
def lookAround():
    return(player1.room.desc)

print(f"You open your eyes to {player1.room}")
while(user_input != "q"):

    if(user_input == "1"):
        print(lookAround())
    elif(user_input == "2"):
        player1.travel()
    print("\nYour options are:\n1: Look Around\n2: Travel\nq: Quit game")
    user_input = input("What do you do? Please enter number.\n")
'''
player1 = Player("John", "outside")


while True:
    # print current room name
    print("Current Room: ", player1.get_room())

    # Prints the current description (the textwrap module might be useful here).
    print(room['outside'])

    # Waits for user input and decides what to do.

    choice = input("Your options are: \nn: North\ns: South\ne: East\nw: West\nq: Quit\n")

    if choice == "q":
        print("Thanks for playing!")
    
    try:
        if(choice == "1"):
            pass
        elif (choice == "2" and player1.room.n_to != None):
            player1.room = player1.room.n_to.name
        elif(choice == "3" and player1.room.e_to != None):
            player1.room = player1.room.e_to.name
        elif(choice == "4" and player1.room.s_to != None):
            player1.room = player1.room.s_to.name
        elif(choice == "5" and player1.room.w_to != None):
            player1.room = player1.room.w_to.name
        else:
            print("You can't go that way")
    except ValueError:
        print("Please enter your choice as a number")
