# Good code is self-documenting.

print("Learn Python Step by Step!")

# Define a list of months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# Function to print the calender months
def showCalendar(months):
    # For loop that traverses the list and prints the name of each month
    for month in months:
        print(month)
showCalendar(months)

# Note: The symbol(  # ) is also known as the octothorpe.
# The term came from a group of engineers at Bell Labs while working on a first of the touch-tone keypads project.

# To Learn any language you must follow the below rules.
# 1. Know the basic syntax, data types, control structures and conditional statements.
# 2. Learn error handling and file I/O.
# 3. Read about advanced data structures.
# 4. Write functions and follow OOPs concepts.
def main():
    print("Let's start to learn Python.")
main()

# You can access them using the following special variable
# myobj.__doc__

def theFunction():
    '''
This function demonstrate the use of docstring in Python.
Second line test. I mean, this is suppose to be an example of MULTI-LINE...
    '''
    print("Python docstrings are not comments.")


print("\nJust printing the docstring value...")
print(theFunction.__doc__)