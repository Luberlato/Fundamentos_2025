km_rodados = int(input("Quantos quilômetros você percorreu"))
qt_dias = int(input("Quantos dias você rodou:"))
total = (km_rodados*0.15) + (qt_dias*60)
print("O total é pagar: R$ %.2f" %total)