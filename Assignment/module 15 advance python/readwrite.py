a = open("demo.txt", "w")
lines = ["hello worls\n", "hello python"]
a.writelines(lines)
a.close()

a = open("demo.txt", "r")
print(a.read())
a.close()
