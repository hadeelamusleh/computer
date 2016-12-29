import abc

#abstract class USP ports
class uspPort(object):
    #to define it is a abstract class
    __metaclass__ = abc.ABCMeta
    #constructor contains attributes of ports's number
    def __init__(self, num):
        self.uspPortNum = num
    #abstract method call usp port type to clear the type of port
    @abc.abstractmethod
    def uspPortType(self):pass


