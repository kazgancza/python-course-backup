# email = input("Enter Your Email: ").strip()
# 
# username = email[:email.index('@')]
# domain = email[email.index('@') + 1:]
# 
# print(f"Your username is {username} & domain is {domain}")

def emailSlicer(email):
    username = email[:email.index("@")]
    domain = email[email.index("@") + 1:]
    return username, domain

emailKazik = "kazik@gmail.com"
emailPaula = "paula@gmail.com"

emailKazikSliced = emailSlicer(emailKazik)