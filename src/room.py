# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, roomName, roomDesc, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = roomName
        self.desc = roomDesc
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to