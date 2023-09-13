try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print(f"{num1}/{num2}Result is {num1/num2}")
except ValueError:
    print("Please Enter Only Number")
except ZeroDivisionError:
    print("Cannot divide by Zero")
except Exception:
    print("Something went Wrong", Exception)
