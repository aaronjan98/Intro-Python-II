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


print('outside:', room["outside"].roomName, room["outside"].roomDesc)

player1 = Player(name="John", room=room["outside"])

while True:
    # print current room name
    print("Current Room: ", player1.get_room())

    # Prints the current description (the textwrap module might be useful here).
    print(f"\n** {player1.get_roomDesc()} **\n")

    # Waits for user input and decides what to do.
    choice = input("Your options are: \nn: North\ns: South\ne: East\nw: West\nq: Quit\n")
    
    if choice == "q":
        print("Thanks for playing!")
        break
    
    try:
        if(choice == "n" and player1.room.dir_exists(choice)):
            player1.room = player1.room.n_to
        elif (choice == "s" and player1.room.dir_exists(choice)):
            player1.room = player1.room.n_to
        elif(choice == "e" and player1.room.dir_exists(choice)):
            player1.room = player1.room.n_to
        elif(choice == "w" and player1.room.dir_exists(choice)):
            player1.room = player1.room.n_to
        else:
            print("You can't go that way")
    except ValueError:
        print("Invalid Response")

#     def one():
#     return "January"
 
# def two():
#     return "February"
 
# def three():
#     return "March"
 
# def four():
#     return "April"
 
# def five():
#     return "May"
 
# def six():
#     return "June"
 
# def seven():
#     return "July"
 
# def eight():
#     return "August"
 
# def nine():
#     return "September"
 
# def ten():
#     return "October"
 
# def eleven():
#     return "November"
 
# def twelve():
#     return "December"
 
 
# def numbers_to_months(argument):
#     switcher = {
#         1: one,
#         2: two,
#         3: three,
#         4: four,
#         5: five,
#         6: six,
#         7: seven,
#         8: eight,
#         9: nine,
#         10: ten,
#         11: eleven,
#         12: twelve
#     }
#     # Get the function from switcher dictionary
#     func = switcher.get(argument, lambda: "Invalid month")
#     # Execute the function
#       print func()