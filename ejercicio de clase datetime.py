import datetime

semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
hoy = datetime.datetime.now()

print (hoy)

fecha = input("ingrese la fecha del vuelo(dia/mes/año): ")
fecha_sis = datetime.datetime.strptime(fecha,"%d/%m/%y")
print(fecha_sis)

dia = fecha_sis.weekday()
print(dia)

print(semana[dia])
