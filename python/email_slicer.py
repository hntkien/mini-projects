#========== Email Slicer ==========#

# 1. Collect email form user
# 2. Split the email using the @ , the first part as the user name, the second part is the domain
# 3. Split domain using . 

def main():
    print("Welcome to the email slicer.\n")

    email_input = input("Enter your email address: ")

    (username, domain) = email_input.split("@")
    (domain, *extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain) 
    print("Extension: ", extension)

if __name__ == "__main__":
    main() 