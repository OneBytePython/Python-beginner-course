# Explicit conversion (manually)

# String to integer
num = int("42")
print("String to intiger:", type(num))

# Integer to string
text = str(42)
print("Intiger to string:", type(text))

# Float to integer (truncates the decimal)
whole = int(3.14)  # becomes 3
print("Float to intiger:", type(whole))

# String to float
decimal = float("3.14")
print("String to float:", type(decimal))

# Implicit conversion (automatic)
x = 5        # int  
y = 2.0      # float  
result = x + y   # result is 7.0 (a float)
print("Type of result:", type(result))

# Boolean conversion
bool(0)        # False  
bool(1)        # True  
bool("")       # False  
bool("Hello")  # True