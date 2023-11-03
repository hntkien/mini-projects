#========== Basic Calculator ==========#

# 1. Define the functions needed: add, sub, mul, div 
# 2. Print options for user 
# 3. Ask for values 
# 4. Call the functions 
# 5. While loop to contiue until the user want to exit 

##### Feature Functions #####
def add(a, b):
    print("Addition")
    result = a + b 
    print(f"{a} + {b} = {result}\n")
    
def sub(a, b):
    print("Subtraction")
    result = a - b 
    print(f"{a} - {b} = {result}\n") 

def mul(a, b):
    print("Multiplication")
    result = a * b 
    print(f"{a} * {b} = {result}\n") 

def div(a, b):
    print("Division")
    result = a / b 
    print(f"{a} / {b} = {result}\n") 

##### Main Function #####
def main():

    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    valid_choices = ['A', 'B', 'C', 'D', 'E']

    while True:

        choice = input("Input your choice for operation: ").upper()
        # Continue with the next loop if choice is nto a valid options
        if choice not in valid_choices:
            print("Invalid option.")
            continue 
        # Terminate the program immediately if user enter keyword 'E' 
        elif choice == 'E':
            break 

        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        
        # Conditions 
        if choice == 'A':
            add(a, b) 
        elif choice == 'B':
            sub(a, b)
        elif choice == 'C':
            mul(a, b) 
        elif choice == 'D':
            div(a, b) 
    
    print("Program Terminated.")


##### Execution #####
if __name__ == "__main__":
    main() 
