#Split the email as username, domain 
def email_slicing():
    print("")
    print("SLICE THE EMAIL")
    print("")
    email_id = input("Enter an email_address: ")
    print("")
    (username,domain) = email_id.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username: ",username)
    print("Domain: ",domain)
    print("extension: ",extension)
    print("")
while True:
    email_slicing()
