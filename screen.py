import abc

#abstract class screen
class screen(object):
    #to define it is a abstract class
    __metaclass__ = abc.ABCMeta
    #constructor contains attributer (color of screen , size of screen and type of screen
    def __init__(self, color,size,type):
        self.screenColor = color
        self.screenSize=size
        self.screenType=type
    #abstract method declears system of color in screen
    @abc.abstractmethod
    def screenColorSystem(self):pass
    #abstract method declears system of screen
    @abc.abstractmethod
    def screenSystem(self): pass
