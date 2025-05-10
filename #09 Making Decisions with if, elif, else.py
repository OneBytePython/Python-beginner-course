print("------------------ Using or -----------------")

x = 0
if x == 0 or x == 10:
    print("x is either 0 or 10")

print("-----------------Using not ------------------")

is_logged_in = 0
if not is_logged_in:
    print("Please log in first")

print("------------ Nested if statement ------------")

age = 20
if age > 0:
    if age < 18:
        print("You're a minor")
    else:
        print("You're an adult")
else:
    print("Invalid age")