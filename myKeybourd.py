from keybourd import keybourd
# sub class  myKeybourd from abstract class keybourds
class myKeybourd(keybourd):
    #constructor contains attribute color of keybourd m number of keys  and type of it
    def __init__(self, keybourcolor, numOfKeysKeybourd,typeOfKeys):
        super(myKeybourd,self).__init__(keybourcolor, numOfKeysKeybourd,typeOfKeys)
    # abstract method with implementation to  declear design of keybourd ans click on it
    def designKeybourd(self):
        return "spical design"
    def clickKeybourd(self):
        return "click keybours"
