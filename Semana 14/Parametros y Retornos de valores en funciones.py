def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento dado un porcentaje y el total de la compra.
    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (10% por defecto).
    :return: Monto del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Definir un producto específico
producto = "Laptop Gamer"
monto = 1500.00  # Precio de la laptop
descuento_por_defecto = 10  # Descuento del 10%
descuento_personalizado = 15  # Otro descuento del 15%

# Calcular descuentos
descuento1 = calcular_descuento(monto, descuento_por_defecto)
descuento2 = calcular_descuento(monto, descuento_personalizado)

# Calcular montos finales
monto_final1 = monto - descuento1
monto_final2 = monto - descuento2

# Mostrar resultados
print("\nResumen de la compra:")
print(f"Producto comprado: {producto}")
print(f"Precio original: ${monto:.2f}")

print(f"\nCon un descuento del {descuento_por_defecto}% en {producto}:")
print(f"Descuento aplicado: ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}")

print(f"\nCon un descuento del {descuento_personalizado}% en {producto}:")
print(f"Descuento aplicado: ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")

print("\nGracias por su compra!")
