attdata=[]

def attendance():
    print("----attendance----\n")
    name=input("enter student name:")
    roll=input("enter roll no:")
    course=input("enter course:")
    date=input("enter date:")
    status=input("student is present or absent P/A?").upper()

    for record in attdata:
        if record['roll']==roll and record['date']==date:
            print("attendance already marked!")
            return
    attdata.append({
        'name':name,
        'roll':roll,
        'course':course,
        'date':date,
        'status':status
    })
    print("attendance marked successfully")
def report():
    print("\n----attendance report----")
    choice=input("1.student report\n2.class report\nchoose:")
    if choice=='1':
        roll=input("enter roll no.")
        stdata=[r for r in attdata if r['roll']==roll]
        if not attdata:
            print("no records found!")
            return
        total=len(attdata)
        present=sum(1 for r in attdata if r['status']=='P')
        percent=(present/total)*100
        print("\nname:",attdata[0]['name'])
        print("total days:",total)
        print("present:",present)
        print("absent:",total-present)
        print("attendance in %:",percent)
        if percent<75:
            print("bad attandance(defaulters)")
    elif choice=='2':
        print("\nroll\tname\tcourse\tdate\tstatus")
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        for r in attdata:
            print(f"{r['roll']}\t{r['name']}\t{r['course']}\t{r['date']}\t{r['status']}")
    else:
        print("invalid choice!")
def main():
    while True:
        print("\n==== menu ====")
        print("1.record attendance")
        print("2.view report")
        print("3.exit program")
        ch=input("enter your choice:")

        if ch=='1':
            attendance()
        elif ch=='2':
            report()
        elif ch=='3':
            print("exiting program...good bye!")
            break
        else:
            print("invalid choice please try again.")
main()