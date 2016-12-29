import abc

#abstract class cpu
class CPU(object):
    #to define it is a abstract class
    __metaclass__ = abc.ABCMeta
    #constructor contains attributes (size of cpu and type of cpu
    def __init__(self, size,type):
        self.CPUsize = size
        self.CPUtype=type
   # abstract method to description the cpu
    @abc.abstractmethod
    def description(self, click):pass


