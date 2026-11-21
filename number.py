while True:
    try:
        x = int(input("Enter a value of x:"))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")