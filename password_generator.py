import string
import random
def get_password_length():
    while True:
        try:
            passlen = int(input("\nPlease enter the password length: "))
            if passlen > 0:
                return passlen
            else:
                print(" Length must be greater than 0.")
        except ValueError:
            print(" Invalid input! Please enter numbers only.")

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation

sA = []
sA.extend(list(s1))
sA.extend(list(s2))

sB = []
sB.extend(list(s1))
sB.extend(list(s2))
sB.extend(list(s3))

sC = []
sC.extend(list(s1))
sC.extend(list(s2))
sC.extend(list(s3))
sC.extend(list(s4))
def get_strength_choice():
    while True:
        print("\nENTER HOW STRONG PASSWORD YOU NEED")
        print("1 - Normal strength (letters only)")
        print("2 - Strong strength (letters + digits)")
        print("3 - Very strong strength (letters + digits + special characters)")
        print("4 - EXIT")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print(" Invalid choice! Please enter 1, 2, 3, or 4.")
        except ValueError:
            print(" Invalid input! Please enter numbers only.")
while True:
    passlen = get_password_length()
    choice = get_strength_choice()

    if choice == 1:
        random.shuffle(sA)
        password = "".join(sA[:passlen])
        print(f"Generated Password: {password}")

    elif choice == 2:
        random.shuffle(sB)
        password = "".join(sB[:passlen])
        print(f"Generated Password: {password}")

    elif choice == 3:
        random.shuffle(sC)
        password = "".join(sC[:passlen])
        print(f"Generated Password: {password}")

    elif choice == 4:
        print("\n THANKS FOR USING THIS PASSWORD GENERATOR. Goodbye!")
        break

