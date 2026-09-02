temp=float(input("qual a temperatura de hoje?"))

if temp>28:
    print("Calor")
elif (temp>16 and temp<28):
    print("Tempo bom")
elif temp==28:
    print("Temperatura ideal")
else:
    print("esta frio")
