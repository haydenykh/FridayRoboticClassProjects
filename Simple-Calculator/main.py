# Welcome message
global result
print("""
+ =============== +
+                 +
+  Calculator.py  +
+                 +
+ =============== +
""")

# Get input
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")

# Pick options
title = "Please select your operator."
options = ("+", "-", "*", "/", "**", "//", "%")
operator = input(title + "\n" + str(options))

try:
    n1 and n2
except NameError:
    print("Input 1 and Input 2 has no inputs.")
else:
    if operator == "+":
        result = int(n1) + int(n2)
    elif operator == "-":
        result = int(n1) - int(n2)
    elif operator == "*":
        result = int(n1) * int(n2)
    elif operator == "/":
        result = int(n1) / int(n2)
    elif operator == "**":
        result = int(n1) ** int(n2)
    elif operator == "//":
        result = int(n1) // int(n2)
    elif operator == "%":
        result = int(n1) % int(n2)
    else:
        print("Invalid operator. Exiting...")
        exit(1)

# Print result
print("Result:", result)