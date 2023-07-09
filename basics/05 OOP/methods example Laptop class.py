
class Laptop:
    def __init__(self, cpu, gpu="integrated", ram=2048, price=9999):
        self.setCpu(cpu)
        self.gpu = gpu
        self.setRam(ram)
        self.price = price

    def setCpu(self, cpu):
        if cpu.lower() == "amd" or cpu.lower() == "intel" or cpu.lower() == "arm":
            self.cpu = cpu
        else:
            self.cpu = "unkown"

    def setRam(self, ram):
        if isinstance(ram, int) and ram >= 2048:
            self.ram = ram
        else:
            self.ram = 2048

        
    def printData(self):
        print(self.cpu, self.gpu, self.ram, self.price)

laptop1 = Laptop("Intel", ram=8192)
laptop1.printData()

laptop2 = Laptop("AMD", ram=32000)
laptop2.printData()