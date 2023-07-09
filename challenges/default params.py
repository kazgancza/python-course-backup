def person(email, country = "Polska", company = "Example Ltd"):
    personDict = {
        "email": email,
        "country": country,
        "company": company
    }
    return personDict

print(person("ola@example.com"))
print(person("kasia@example.com", "UK"))
print(person("adam@example.com", "UK", "Test Sp Zoo"))
