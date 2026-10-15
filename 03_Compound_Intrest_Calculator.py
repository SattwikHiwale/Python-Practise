principle = float(input("enter a amount: "))
rate = float(input("enetr a rate of intrest"))
time = float(input("eneter a time period")
             )
amount1 = principle * (1 + rate / 100) ** time
amount2 = principle * pow((1 + rate / 100), time)
print(round(amount1, 2), round(amount2, 2))
compound_intrest = amount1 - principle
print("compound intrest is: ", round(compound_intrest, 2))
