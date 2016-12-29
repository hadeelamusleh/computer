from CPU import CPU
#sub class from CPU class
class mycpu(CPU):
    #constructor contains attributes (size of cpu and type of cpu
    def __init__(self,sizeCPU,typeCPU):
        super(mycpu, self).__init__(sizeCPU,typeCPU)
    #abstract method with implementation to description the cpu
    def description(self):
        return "MY CPU"