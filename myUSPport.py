from uspPort import uspPort
#sub class of usp port class
class myUspPort(uspPort):
    #constructor contains attributer (number of usp ports)
    def __init__(self,numOfUspport):
        super(myUspPort, self).__init__(numOfUspport)
    #abstract method and implementation it
    def uspPortType(self):
       return "my types of USP port  with number = %d"%self.uspPortNum