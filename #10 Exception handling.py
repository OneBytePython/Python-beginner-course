try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Always runs.")

age = int(input("Enter a number: "))

if age < 0:
    raise ValueError("Age can't be negative.")