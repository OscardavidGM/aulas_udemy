class Vehicle:  # CLASE BASE O PRINCIPAL

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):  # CLASE HIJA O SECUNDARIA, SUBCLASE
    pass


School_bus = Bus("School Volvo", 180, 12)  # CREANDO EL OBJETO DE BUS

print("Vehicle Name:", School_bus.name, "Speed:",
      School_bus.max_speed, "Mileage:", School_bus.mileage)  # ACCESANDO A LA INFO VEHICULO (CLASE PRINCIPAL) USANDO EL OBJETO BUS
