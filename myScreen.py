from screen import screen
#sub class of screen class
class myScreen(screen):
    #constructor contains attributes (size of screen , type of screen and color of screen
    def __init__(self,sizeScreen,typeScreen,colorScreen):
        super(myScreen, self).__init__(sizeScreen,typeScreen,colorScreen)
    #abstract method with implementation to declear type of system screen
    def screenSystem(self):
        return "Screen type System is %s" % self.screenType
    #abstract method with implementation to declear type of system color  screen
    def screenColorSystem(self, type):
        return "color system of screen is %s" %type