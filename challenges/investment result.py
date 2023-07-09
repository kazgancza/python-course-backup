capital = 5000
rateOfIntrest = 0.08
inflationRate = 0.15

returnAmount = capital * rateOfIntrest
inflationCut = capital * inflationRate

print("Zwrot z inwestycji:", returnAmount)
print("O ile spadła wartość kapitału przez inflację:", inflationCut)

result = capital + returnAmount - inflationCut
print("Wynik:", result)
