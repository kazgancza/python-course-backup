age = 18
weight = 50

if age >= 18:
    if weight >= 50:
        print("Osoba może oddać krew.")
    else:
        print("Osoba nie może oddać krwi, z powodu zbyt małej wagi.")
else:
    print("Osoba nie może oddać krwi, z powodu zbyt młodego wieku")
    if weight < 50:
        print("oraz zbyt małej wagi.") # tego w kursie już nie dał xD

