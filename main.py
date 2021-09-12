def print_hi(name):
    print(f'Hello, {name}')


def getUserData():
    userdata = int(input("Enter your number : "))
    print(userdata)


def calculator(operator, firstnum, secnum):
    if operator == "+":
        print(firstnum + secnum)
    elif operator == "-":
        print(firstnum - secnum)
    elif operator == "**":
        print(firstnum ** secnum)


if __name__ == '__main__':
    print_hi('World')
    getUserData()
    calculator("+", 4, 5)
    calculator("**", 2, 3)
