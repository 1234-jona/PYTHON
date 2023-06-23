p_normaL=55
descuento=.1
p_ahora=49.5
plantilla="El precio normal del producto ABC es de {:8.2f} y con el descuento del {:.2%} el precio de ahora es de {}"
mensaje=""
mensaje=plantilla.format(p_normaL,descuento,p_ahora)
print(mensaje)