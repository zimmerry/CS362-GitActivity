def divisors(a):
    print("Divisors for", a)
    for i in range(1, a+1):
        if a % (i) == 0:
            print(i)

def main():
    a = input("Enter an integer: ")
    divisors(int(a))

if __name__ == "__main__":
    main()
