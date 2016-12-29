from mouse import mouse
#sub class of mouse class
class myMouse(mouse):
    #constructor contains attrinutes to declear mouse color
    def __init__(self,mouseColor):
        super(myMouse, self).__init__(mouseColor)
    #abstract methods with implementation to check click on mouse (right or left )
    def mouseRightClick(self):
        return"riter click"
    def mouseLeftClick(self):
        return "left click"