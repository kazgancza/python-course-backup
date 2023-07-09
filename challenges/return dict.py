# Moje wykonanie XD
"""
def createUser(name, contact):
    user = {
        name: contact
    }
    if isinstance(contact, str):
        print("Imię:", name + ", Mail:", contact)
    if isinstance(contact, int):
        print("Imię:", name + ", Tel.:", contact)
    
createUser("Kasia", 123456789)
createUser("Ola", "ola@example.com")
"""

# Poprawne rozwiązanie

def createUser(name, contact):
    user = {
        "name": name,
        "email": None,
        "telephone": None,
    }

    if isinstance(contact, str):
        user["email"] = contact
    elif isinstance(contact, int):
        user["telephone"] = contact

    return user

user1 = createUser("Ola", "ola@example.com")
print(user1)
user2 = createUser("Kasia", 123456789)
print(user2)
