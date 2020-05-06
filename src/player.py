# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room
class Player():
    def __init__(self, name, room):
        self.name = name
        # super().__init__(roomName, roomDesc)
        self.room=room
        
    def travel(self):
        choice = input(
            "Your options are:\n1: Nevermind\n2:Go North\n3:Go East\n4:Go South\n5:Go West\n")
        if(choice == "1"):
            pass
        elif (choice == "2" and self.room.n_to != None):
            self.room = self.room.n_to.name
        elif(choice == "3" and self.room.e_to != None):
            self.room = self.room.e_to.name
        elif(choice == "4" and self.room.s_to != None):
            self.room = self.room.s_to.name
        elif(choice == "5" and self.room.w_to != None):
            self.room = self.room.w_to.name
        else:
            print("You can't go that way")