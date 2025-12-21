def even():
    for i in range(0, 20, 2):
        yield i

for num in even():
    print(num)