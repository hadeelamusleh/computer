from keys import keys


# sub class  myKeys from abstract class keys
class myKeys(keys):
    # constructor contains attributer (number of keys and type of it )
    def __init__(self, numOfKeys, typeOfKeys):
        super(myKeys, self).__init__(numOfKeys,typeOfKeys)


    # abstract method with implementation to  declear job of each key
    def job(self):
       return "my jobs of keys"
