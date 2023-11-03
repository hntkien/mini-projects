#========== Basic Calculator ==========#

# 1. Define the functions needed: add, sub, mul, div 
# 2. Print options for user 
# 3. Ask for values 
# 4. Call the functions 
# 5. While loop to contiue until the user want to exit 

##### Feature Functions #####

# Addition
def add(a, b):
    print("Addition")
    result = a + b 
    print(f"{a} + {b} = {result}\n")

# Subtraction    
def sub(a, b):
    print("Subtraction")
    result = a - b 
    print(f"{a} - {b} = {result}\n") 

# Multiplication
def mul(a, b):
    print("Multiplication")
    result = a * b 
    print(f"{a} * {b} = {result}\n") 

# Division
def div(a, b):
    print("Division")
    result = a / b 
    print(f"{a} / {b} = {result}\n") 

# Function to display available options
def display_choices():
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    # Dictionay of lists. The first element of the list is the flag.
    # If True, run the operation (second element). If False, terminate the program
    available_operations = {
        'A': [True, add],
        'B': [True, sub],
        'C': [True, mul],
        'D': [True, div],
        'E': [False, None]
    }
    return available_operations 

##### Main Function #####
def main():

    while True:

        available_operations = display_choices()
        choice = input("Input your choice for operation: ").upper()

        # Next loop if choice is not valid 
        if choice not in available_operations.keys():
            print("Invalid option.\n")
            continue 
        else:
            flag, operation = available_operations[choice]

        # If flag is False, exit the loop
        if flag == False:
            break 

        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        # Run the selected function with parameters a, b
        operation(a, b)
    
    print("Program Terminated.")


##### Execution #####
if __name__ == "__main__":
    main() 
