class emp:
    def getdata(self,id,name): #original
        print("ID:",id)
        print("Name:",name)

class a(emp):
    def getdata(self, id, name): #xerox
        return super().getdata(id, name)

class b(emp):
    def getdata(self, id, name):
        return super().getdata(id, name)
    

a1=a()
a1.getdata("raj 82",'paras')

b1=b()
b1.getdata("raj 81",'dharmik')