attaandance=[]

def atttandance():
    name=input("enter student name:")
    roll=input("enter roll no.:")
    course=input("enter course")
    date=input("enter date:")
    attand=input("present/absent(P/A):")

    record={"name":name,"roll":roll,"course":course,"date":date,"attand":attand.upper()}
    attaandance.append(record)
    print("\nattandance marked!")

def sreport():
    roll=input("enter roll no.:")
    total=0
    present=0
    absent=0
    for rep in attaandance:
        if rep["roll"]==roll:
            total+=1
            if rep["attand"] == "P":
                present+=1
            else:
                absent+=1
    if total==0:
        print("\nno record found!")
    else:
        Per=(present/total)*100
        print(f"\nreport for roll no:{roll}")
        print("total days:",total)
        print("present:",present)
        print("absent",absent)
        print("attandance%:",Per)
        if present< 80:
            print("defaulter!!!")
        else:
            print("good attandance")
def creport():
    if len(attaandance)==0:
        print("\nno attandance yet...")
        return
    students={}
    for rep in attaandance:
        roll=rep["roll"]
        if roll not in students:
            students[roll]={"present":0,"absent":0}
        students[roll]["total"]+=1
        if rep["attand"]=="p":
            students[roll]["present"]+=1

    print("\n class report")
    print("roll\tpresent\ttotal\t& attandance\tstatus")
    for roll, data in students.items():
        per=(data["present"]/data["total"])*100
        status="defaulter" if per<80 else "ok"
        print(f"{roll}\t{data['present']}\t{data['total']}\t{per:.2f}%\t{status}")
    print()

while True:
    print("==== student app ====")
    print("1. Mark Attendance")
    print("2. Student Report")
    print("3. Class Report")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        atttandance()
    elif choice == "2":
        sreport()
    elif choice == "3":
        creport()
    elif choice == "4":
        print("have a good day !!!!")
        break
    else:
        print("Invalid choice!\n")