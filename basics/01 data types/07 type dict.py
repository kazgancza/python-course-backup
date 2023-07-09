contacts = {
    "Ola" : "ola@example.com",
    "Daniel" : 30,
    "Ania" : "ania@example.com"
}

contacts["Rafał"] = "rafal@example.com"

print(contacts["Ola"])
print(contacts["Daniel"])
print(type(contacts))
print(len(contacts)) # W słowniku elementy nie są po kolei, ale można wyświetlić ich ilość


print(contacts.keys()) # Klucze słownika
print(contacts.values()) # Wartości słownika

for key in contacts:
    print(key + " " + str(contacts[key]))

print("Przerwa")

for key, value in contacts.items():
    print(key, " ", value)


