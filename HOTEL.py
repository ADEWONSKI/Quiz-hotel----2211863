class Hotel:
    def __init__(self, num_habitaciones):
        self.num_habitaciones = num_habitaciones
        self.habitaciones_ocupadas = {}
        self.libro_entradas = {}
        self.libro_salidas = {}

    def asignar_habitacion(self, numero_habitacion, cedula, nombre_cliente):
        if numero_habitacion in self.habitaciones_ocupadas:
            print(f"La habitación {numero_habitacion} ya está ocupada.")
        elif numero_habitacion < 1 or numero_habitacion > self.num_habitaciones:
            print(f"Habitación {numero_habitacion} no válida.")
        else:
            self.habitaciones_ocupadas[numero_habitacion] = (cedula, nombre_cliente)
            self.libro_entradas[cedula] = (numero_habitacion, nombre_cliente)

    def registrar_salida(self, cedula):
        if cedula in self.libro_entradas:
            numero_habitacion, nombre_cliente = self.libro_entradas[cedula]
            del self.habitaciones_ocupadas[numero_habitacion]
            del self.libro_entradas[cedula]
            self.libro_salidas[cedula] = (numero_habitacion, nombre_cliente)
        else:
            print(f"Huésped con cédula {cedula} no encontrado en el libro de entradas.")

    def consulta_individual(self, cedula):
        if cedula in self.libro_entradas:
            numero_habitacion, nombre_cliente = self.libro_entradas[cedula]
            print(f"Cédula: {cedula}")
            print(f"Nombre del cliente: {nombre_cliente}")
            print(f"Número de habitación: {numero_habitacion}")
        else:
            print(f"Huésped con cédula {cedula} no encontrado en el libro de entradas.")

    def consulta_total_por_cedula(self, cedula):
        if cedula in self.libro_entradas:
            self.consulta_individual(cedula)
        else:
            print(f"Huésped con cédula {cedula} no encontrado en el libro de entradas.")

    def consulta_total_por_orden_de_llegada(self):
        for cedula, (numero_habitacion, nombre_cliente) in self.libro_entradas.items():
            print(f"Cédula: {cedula}")
            print(f"Nombre del cliente: {nombre_cliente}")
            print(f"Número de habitación: {numero_habitacion}")

    def lista_habitaciones_disponibles(self):
        habitaciones_disponibles = [i for i in range(1, self.num_habitaciones + 1) 
        if i not in self.habitaciones_ocupadas]
        print("Habitaciones disponibles:", habitaciones_disponibles)

    def lista_habitaciones_ocupadas(self):
        print("Habitaciones ocupadas:")
        for numero_habitacion, (cedula, nombre_cliente) in self.habitaciones_ocupadas.items():
            print(f"Número de habitación: {numero_habitacion}")
            print(f"Cédula: {cedula}")
            print(f"Nombre del cliente: {nombre_cliente}")


hotel = Hotel(10)  

hotel.asignar_habitacion(1, "1234567890", "diego camacho")
hotel.asignar_habitacion(2, "9876543210", "Carlos camacho")
hotel.asignar_habitacion(3, "5678901234", "carlos pimienta")

hotel.registrar_salida("9876543210")

print("consulta individual:")
hotel.consulta_individual("1234567890")

print("\nConsulta total por orden de llegada:")
hotel.consulta_total_por_orden_de_llegada()

print("\nHabitaciones disponibles:")
hotel.lista_habitaciones_disponibles()

print("\nHabitaciones ocupadas:")
hotel.lista_habitaciones_ocupadas()
