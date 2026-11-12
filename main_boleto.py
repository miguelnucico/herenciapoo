from clases.boletos_cine import boleto, boleto_estudiante, boleto_cortesia

def main():
    boleto1 = boleto("Regina","Función A")
    boleto2 = boleto_estudiante("Yamel", 90, "Función B")
    boleto3 = boleto_cortesia("Erick", "Función C")

    print(boleto1.ticket())
    print(boleto2.ticket())
    print(boleto3.ticket())



if __name__ == "__main__":
    main()