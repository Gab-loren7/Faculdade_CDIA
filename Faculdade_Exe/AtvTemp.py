temperatura = "9"
calibracao:float = 1.0
temperatura_num = float(temperatura)

temperatura_Calib = temperatura_num + calibracao

if temperatura_Calib < 2.0:
    print("Temperatura Inferior ao Limite! \nTemperatura igual = ",temperatura_num,"°C")
elif temperatura_Calib <= 2 and temperatura_Calib >= 8:
    print("Temperatura está dentro do Limite! \nTemperatura igual = ",temperatura_num,"°C")
else:
    print("Temperatura está Acima do Limite! \nTemperatura igual = ",temperatura_num,"°C")