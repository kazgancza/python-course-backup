def getUserInformation(name, surname, job):
    name = name.strip().upper()

    surname = surname.strip().upper()

    job = job.strip().lower()

    text = "imię: " + name + ", nazwisko: " + surname + ", zawód: " + job
    return text

print(getUserInformation("Ania", "Kowalska", "Programistka"))
print(getUserInformation("Daniel", "Lis", "Administrator"))
