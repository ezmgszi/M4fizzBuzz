
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + " fizzbuzz!")
    elif i % 5 == 0:
        print(str(i) + " buzz")
    elif i % 3 == 0:
        print(str(i) + " fizz")
    else:
        print(i)