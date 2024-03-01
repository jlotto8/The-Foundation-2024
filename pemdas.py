# Define PEMDAS
# Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)
# Demonstrate how the order of operations affects numerical and logical expressions

# Example 1: Numerical expression
result = 2 + 3 * 4 / 2
print("Result of numerical expression:", result)  
# Output: 2 + (3 * 4) / 2 = 2 + 12 / 2 = 2 + 6 = 8


# Example 2: Logical expression
x = 10
y = 5
z = 7
result = x > y and y < z or x == z
print("Result of logical expression:", result)  # Output: True since (10 > 5) and (5 < 7) or (10 == 7) => True and True or False => True

# Introduce the concept of variables in programming
# Explain variable declaration, assignment, and naming conventions
# Explore different data types (e.g., integers, floats, strings) and their use in variables

# Example 1: Variable declaration and assignment
x = 5
y = 3.14
name = "Alice"

# Example 2: Data types
a = 10              # Integer
b = 3.5             # Float
c = "Hello, World!" # String

# Example 3: Naming conventions
# Variable names should be descriptive and follow snake_case convention
total_marks = 100
student_name = "Bob"

# Discuss the importance of output in programming
# Introduce the echo command in Bash for printing to the console
# Cover formatting options and escape characters in printing
# Provide examples of printing variables and expressions

# Example 1: Basic printing
print("Hello, world!")  # Output: Hello, world!

# Example 2: Printing variables
x = 10
y = 5
print("The value of x is:", x)  # Output: The value of x is: 10
print("The sum of x and y is:", x + y)  # Output: The sum of x and y is: 15

# Example 3: Formatting options
name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name, age))  # Output: Name: Alice, Age: 25

# Example 4: Escape characters
print("This is a new line.\nThis is another line.")  # Output: This is a new line. This is another line.
