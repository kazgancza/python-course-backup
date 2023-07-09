def printCar(brand, /, name = "concept", *, year = 1960, color = "black"):
    print(brand, name, year, color)


printCar("Ford", "Mustang", color = "blue", year = 1973)

# przed / nie może być pozycyjy (np. brand = "Ford")
# za * musi być pozycyjny (np. color = "blue")