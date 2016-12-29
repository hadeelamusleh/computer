import abc
from myKeys import myKeys
#abstract class keybourd
class keybourd():
    #to define it is a abstract class
    __metaclass__ = abc.ABCMeta
    #constructor contains attribute color of keybourd m number of keys  and type of it
    def __init__(self ,color,numOfKeys,typeOfKeys):
       self.keybourdColor=color
       #create object from mykeys class
       self.keys = myKeys(numOfKeys,typeOfKeys)
    #abstract method
    @abc.abstractmethod
    def clickKeybourd(self):pass

    @abc.abstractmethod
    def designKeybourd(self): pass