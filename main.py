from calculator import *

def main():
    while True:
        print("Calculator Time!")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. power")
        print("6. square root")
        print("7. exit")

        while True:
            try:
                choice = int(input("Enter your choice (1-7): "))
                if 1 <= choice <= 7:
                    break
                else:
                    print("Please enter a number between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if choice == 7:
            print("Goodbye!")
            break
        elif choice == 6:
            if (num1 > 0):
                print(square_root(num1))
                break
            else:
                print ("cannot take square root of negative numbers")
        elif choice in [1,2,3,4,5]:
            try:
                num1 = float(input("enter your first number!"))
                num2 = float(input("enter your second number!"))
            except ValueError:
                print("invalid input")
                continue
            if choice == 1:
                print(add(num1,num2))
                break
            elif choice == 2:
                print(subtract(num1,num2))
                break
            elif choice == 3:
                print(multiply(num1,num2))
                break
            elif choice == 4:
                if num2 > 0:
                    print(divide(num1,num2))
                    break
                else:
                    print("Cannot divide by 0")
                    continue
            elif choice == 5:
                print(power(num1,num2))
                break
if __name__ == "__main__":
    main()
        
