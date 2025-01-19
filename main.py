def factorial(n):
    if n==0 or n==1:
        return 1
    return factorial(n-1) * n

def main():

    try:
        number = int(input("Enter your number:  "))

        if number < 0:
            print("[-] YOU SHOULD ENTER POSITIVE NUMBER!!!\n")
        else:
            print(f"{factorial(number)} is the factorial of {number}\n")

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()