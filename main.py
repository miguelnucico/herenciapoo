from clases.empleados import Empleado, EmpleadoPorHora, Vendedor

def main():
    empleado = Empleado("Regina",1500)
    vendedor = Vendedor("Yamel",2500,3000)
    empleadoHora = EmpleadoPorHora("Erick",20,100)

    print(empleado.descripcion())
    print(vendedor.descripcion())
    print(empleadoHora.descripcion())

if __name__ == "__main__":
    main()