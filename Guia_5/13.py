cantidad = int(input("¿Cuántos productos desea comprar? "))

total = 0

for i in range(1, cantidad + 1):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    total += precio

descuento = 0
if total > 100000:
    descuento = 0.20
elif total > 50000:
    descuento = 0.10

monto_descuento = total * descuento
monto_final = total - monto_descuento

print("\n--- Resumen de la compra ---")
print(f"Monto antes del descuento: ${total:,.0f}")
print(f"Descuento aplicado: {descuento*100:.0f}% -> ${monto_descuento:,.0f}")
print(f"Monto final a pagar: ${monto_final:,.0f}")
