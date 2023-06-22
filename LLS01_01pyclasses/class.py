class Zoom:
    __number_of_meetings = 0

    def __init__(self):
        #private instance attribute
        self.__name = new_name
        #public instance attribute
        #self.name = new_name
        Zoom.number_of_meetings += 1

    def change_name(self): #current instance attribute
        self.name = new_name

    @classmethod

c12 = Zoom("c12 meeting")
print("c12 old name is {c12.name}")
c12.change_name("c12 Live Learning Zoom meeting")
print("c12 new name is {c12.name}")
c06 = Zoom("c06 meeting")
print(Zoom.__number_of_meeting)
