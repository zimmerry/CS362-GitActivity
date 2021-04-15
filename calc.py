def calc(a, b):
    print(a, "+", b, "=", a+b)
    print(a, "-", b, "=", a-b)
    print(a, "*", b, "=", a*b)
    print(a, "/", b, "=", a/b)

def main():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    calc(int(a), int(b))

if __name__ == "__main__":
    main()
