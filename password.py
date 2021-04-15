import string
import random

def pwgen(size):
    print(''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size)))

def main():
    a = input("Enter the password length you want: ")
    pwgen(int(a))

if __name__ == "__main__":
    main()
