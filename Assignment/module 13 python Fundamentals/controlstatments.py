fruit=["apple","mango","grapes","banana"]
for fruit in fruit:
    if fruit == 'banana':
        continue
    print(fruit)
for fruit in fruit:
    if fruit == 'banana':
        print("Banana found!")
        break
    else:
        print("not found")