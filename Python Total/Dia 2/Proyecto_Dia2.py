print("Hola bienvenido a Kire's sales")

name = input("Por favor escribe tu nombre: ")
sales = input("Escribe tus ventas totales: ")

total_sales = float(sales)

commissions = round(total_sales / 100 * 13 ,2)

print(f"Tus comisiones son: {commissions} dolares, buen trabajo {name}!")
