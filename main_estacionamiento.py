from clases.estacionamiento import estancia, pension, noche

def main():
    estancia1 = estancia("ABC123", 3)
    pension1 = pension("XYZ789")
    noche1 = noche("LMN456", 5)

    print(estancia1.ticket())
    print(pension1.ticket())
    print(noche1.ticket())
if __name__ == "__main__":
    main()