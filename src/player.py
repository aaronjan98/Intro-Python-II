# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player():
    def __init__(self, name, roomName, roomDesc):
        self.name = name
        super().__init__(roomName, roomDesc)
        
    def get_room(self, roomName):
        return roomName
