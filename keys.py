import abc

#abstract class keys
class keys():
    #to define it is a abstract class
    __metaclass__ = abc.ABCMeta
    #constructor contains attributer (number of keys and type of it )
    def __init__(self ,numOfKeys,typeOfKeys):
       self.keysType=typeOfKeys
       self.NumOfKeys=numOfKeys
    #abstract method declears job of each key
    @abc.abstractmethod
    def job(self):pass

