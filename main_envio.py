from clases.paqueteria import Envio, EnvioExpress, EnvioSobre

def main():
    envio = Envio("Regina", 5)
    sobre = EnvioSobre("Yamel")
    express = EnvioExpress("Erick", 10)

    print(envio.resumen())
    print(sobre.resumen())
    print(express.resumen())

if __name__ == "__main__":
    main()