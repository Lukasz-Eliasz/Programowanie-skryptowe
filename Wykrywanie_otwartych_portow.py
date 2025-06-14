import socket
from concurrent.futures import ThreadPoolExecutor

def sprawdzPort(adresIP, port):
    """
    Ta funkcja próbuje połączyć się z danym portem na określonym adresie IP, aby sprawdzić, czy jest otwarty.

    Argumenty:
    adresIP (str): Adres IP serwera.
    port (int): Port do sprawdzenia.

    Zwraca:
    int: Numer portu, jeśli jest otwarty.
    """
    try:
        gniazdo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        gniazdo.settimeout(1)
        wynik = gniazdo.connect_ex((adresIP, port))

        if wynik == 0:
            return port

        gniazdo.close()
        return None

    except socket.error:
        return None

def skanowaniePortow(adresIP, portStartowy, portKoncowy):
    """
    Ta funkcja skanuje podany zakres portów na określonym serwerze w celu wykrycia otwartych portów.
    Wykonuje skanowanie jednocześnie przy użyciu ThreadPoolExecutor w celu szybszego wykonania.

    Argumenty:
    adresIP (str): Adres IP serwera do skanowania.
    portStartowy (int): Początkowy numer portu w zakresie.
    portKoncowy (int): Końcowy numer portu w zakresie.
    """

    with ThreadPoolExecutor(max_workers=100) as executor:
        wynik = executor.map(lambda port: sprawdzPort(adresIP, port), range(portStartowy, portKoncowy + 1))

    otwartePorty = [port for port in wynik if port is not None]

    if otwartePorty:
        print("\nOtwarte porty to:", otwartePorty)
    else:
        print("\nBrak otwartych portów.")

adresIP = input("Wprowadź adres IP który chcesz przeskanować pod kątem otwartych portów: ")
portStartowy = int(input("Wprowadź numer portu startowego: "))
portKoncowy = int(input("Wprowadź numer portu końcowego: "))

skanowaniePortow(adresIP, portStartowy, portKoncowy)
