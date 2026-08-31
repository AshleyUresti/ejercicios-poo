from Carro import Carro

carro1 = Carro()
carro2 = Carro("Rojo", 2025, "AB-CD")

print("=== Carro 1 ===")
print("Color: ", carro1.get_color())
print("Año: ", carro1.get_año())
print("Matricula:", carro1.get_matricula())

print("\n=== Carro 2 ===")
print("Color: ", carro2.get_color())
print("Año: ", carro2.get_año())
print("Matricula: ", carro2.get_matricula())

from Scooter import Scooter
scooter1 = Scooter()
scooter2 = Scooter("S-055", 0, True)

print("\n=== Scooter1 ===")
print("Color: ", scooter1.get_scooter_ID())
print("Año: ", scooter1.get_bateria())
print("Matricula: ", scooter1.get_estaDisponible())

print("\n=== Scooter2 ===")
print("Color: ", scooter2.get_scooter_ID())
print("Año: ", scooter2.get_bateria())
print("Matricula: ", scooter2.get_estaDisponible())

print("\nIniciar viaje en el scooter1 ====")
if scooter1.desbloquear():
    print("Comenzando viaje!")
else:
    print("No se puede desbloquear este scooter")

print("\nIniciar viaje en el scooter 2 ====")
if scooter2.desbloquear():
    print("Comenzando viaje!")
else:
    print("No se puede desbloquear este scooter):")
