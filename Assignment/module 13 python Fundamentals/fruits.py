fru = ['annanas', 'orange', 'mango']
for fru in fru:
    print(fru)

for fru in fru:
    print(f"{fru}: {len(fru)}")

find = input("Enter fruit to search: ")
for fru in fru:
    if fru == find:
        print("Found!")
    else:
        print("not found")
