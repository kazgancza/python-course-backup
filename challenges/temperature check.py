raining = False
haveUmbrella = False
temperature = 14

if temperature >= 40 or temperature <= 0:
    print("Zostań w domu")
elif temperature > 0 and temperature < 10 and haveUmbrella and raining:
    print("Możesz wyjść z parasolką")
elif not raining and temperature >= 10:
    print("Możesz wyjść bez parasolki")
else:
    print("Zostań w domu")
