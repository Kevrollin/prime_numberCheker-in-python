num = int(input("Enter a random Number: "))

flag = False

if num == 1:
    print(f"{num}, is not a Prime Number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

            if flag:
                print(f"{num}, is not a Prime Number")
            else:
                print(f"{num}, is a Prime Number")