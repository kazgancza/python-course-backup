class SimCard:
    def __init__(self) -> None:
        self.contacts = []

    def addContact(self, name, telephone):
        if isinstance(name, str) and isinstance(telephone, int):
            user = {
                "name": name,
                "telephone": telephone
            }
            self.contacts.append(user)
    
    def showContacts(self):
        for i in self.contacts:
            print(i)

sim = SimCard()
sim.addContact("Ola", 98765432)
sim.addContact("Adam", 12345678)
sim.addContact(100, 12345678)
sim.addContact("Kasia", "numer")

sim.showContacts()