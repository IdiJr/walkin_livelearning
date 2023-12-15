class Zoom:
    """public attributes can be accessed by everyone and outside the class"""
    participants = []
    meeting_title = []
    number_of_participants = 0
    """private attributes can only be accessed within the class. assigned with a single underscore"""
    __permissions = []
    __host = ()
    """protected attribute. assigned with a single underscore"""
    _co_host = ""

class car:
    """Public attributes"""
    number_of_tyres = 5
    manufacturer = "Toyota"
    model_number = "corollaS"
    """Private attributes"""
    __serial_number = "853009237"
    __licence_number = "GR 2344 W"
    """protected attributes"""
    _material = "Iron"

print(Zoom().__dict)
