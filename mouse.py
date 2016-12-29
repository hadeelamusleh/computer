import abc

#abstract class mouse
class mouse(object):
    #to define it is a abstract class
    __metaclass__ = abc.ABCMeta
    #constructor contains attribute color of mouse
    def __init__(self, color):
        self.mouseColor = color
    #abstract methods  to check click on mouse (right or left )
    @abc.abstractmethod
    def mouseRightClick(self):pass
    @abc.abstractmethod
    def mouseLeftClick(self):pass
