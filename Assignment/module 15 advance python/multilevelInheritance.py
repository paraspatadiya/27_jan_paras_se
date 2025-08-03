class paras:
    pid:int
    pdes:str

    def p_getdata(self):
        self.pid=input("Enter paras emp. id:")
        self.pdes=input("Enter paras designation:")

class hardik(paras):
    hid:int
    hdes:str

    def h_getdata(self):
        self.hid=input("Enter hardik emp. ID:")
        self.hdes=input("Enter hardik designation:")
class tss(hardik):
    def printdata(self):
        print("------paras's Info------")
        print("paras's emp. id:",self.pid)
        print("paras's designation:",self.pdes)
        print("------hardik's Info------")
        print("hardik's emp. ID:",self.hid)
        print("hardik's designation:",self.hdes)
tc=tss()
tc.p_getdata()
tc.h_getdata()
tc.printdata()
