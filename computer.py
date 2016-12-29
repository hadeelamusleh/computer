from myKeybourd import myKeybourd
from myMouse import myMouse
from myCPU import mycpu
from myUSPport import myUspPort
from myScreen import myScreen
#computer class
class computer():
    #constructor contains attributes
    def __init__(self,keybourcolor,numOfKeysKeybourd,mouseColor,sizeScreen,typeScreen,colorScreen,numOfUspport,sizeCPU,typeCPU,typeOfKeys):
       #create object form different classes and get it the attributes
        self.keybourd =myKeybourd(keybourcolor,numOfKeysKeybourd,typeOfKeys)
        self.mouse=myMouse(mouseColor)
        self.screen=myScreen(colorScreen,sizeScreen,typeScreen)
        self.uspPort=myUspPort(numOfUspport)
        self.CPU=mycpu(sizeCPU,typeCPU)
    #method to description the computer
    def description(self):
        return("about you computer :\n keybourd:\t color %s ,number of keys %s \n "
               "Mouse:\t color %s \n Screen:\t size %d ,Color %s , Type %s \n "
               "USP Port:\t number of USP ports = %d\n CPU:\t size %d, type %s"%(self.keybourd.keybourdColor,self.keybourd.keys,self.mouse.mouseColor,self.screen.screenSize,self.screen.screenColor,self.screen.screenType,self.uspPort.uspPortNum,self.CPU.CPUsize,self.CPU.CPUtype))



