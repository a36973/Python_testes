Peso= int(input("peso :"))
Unit=input("K: or L:")
if Unit.upper()=="K":
    converted=Peso/0.45
    print("Peso em L:" + str(converted))

else:
     converted=Peso*0.45
     print("Peso em K:" + str(converted))