from datetime import datetime

mi_hora = datetime.today()
print(mi_hora.minute)  # tambien se pueden imprimir solo ciertos atributos como la hora( .hour ), minuto ( .minute) y segundos
# ( .second)

# mi_fecha = datetime.date(2004, 3, 13)
# print(mi_fecha)

# mi_fecha2 = datetime.datetime(2004, 3, 13, 2, 30, 0)
# print(mi_fecha2)
# mi_fecha2 = mi_fecha2.replace(month=9)
# print(mi_fecha2)

# nacimiento = date(1995, 3, 5)
# defuncion = date(2095, 5 ,19)

# vida = defuncion - nacimiento
# print(vida)

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)


vigilia = duerme - despierta
print(vigilia)
