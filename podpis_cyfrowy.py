"""
podpis_cyfrowy.py

Użycie:
    1. Uruchom skrypt.
    2. Wprowadź ścieżkę do pliku który chcesz podpisać.
    3. W terminalu otrzymasz podpis cyfrowy podanego pliku.

Opis skryptu:
  - Generuje losowy 256-bitowy tajny klucz i przy jego użyciu oblicza podpis korzystając z
    HMAC-SHA256 zawartości pliku określonego przez użytkownika.

Przykład:
    $ python podpis_cyfrowy.py
    Wprowadź scieżkę do pliku który chcesz zaszyfrować: plik.txt
    Podpis pliku plik.txt = 4b8d26a9de17d3ed249fe736d17c5057ec6670ccfecbf4bce179e1f520a1bab0
"""
import os
import hmac
import hashlib

tajnyKlucz = os.urandom(32)
print(f"Wygenerowany tajny klucz: {tajnyKlucz.hex()}")

def podpiszPlik(sciezkaPliku: str, klucz: bytes) -> str:
    """
       Oblicza podpis HMAC-SHA256 zawartości podanego pliku używająć tajnego klucza.

       Argumenty:
           sciezkaPliku (str): Sciezka do pliku który chcemy podpisać.
           klucz (bytes): Tajny klucz dla HMAC.

        Działanie:
           - Odczytuje plik w trybie binarnym i przetwarza go we fragmentach po 8192 bajtów.
           - Aktualizuje obiekt HMAC-256SHA przy każdym fragmencie.
           - Zwraca podpis zakodowany w formacie szesnastkowym.
    """
    HMAC = hmac.new(klucz, digestmod=hashlib.sha256)
    with open(sciezkaPliku, "rb") as plik:
        while True:
            fragment = plik.read(8192)
            if not fragment:
                break
            HMAC.update(fragment)
    return HMAC.hexdigest()


if __name__ == "__main__":
    sciezkaPliku = input("Wprowadź scieżkę do pliku który chcesz podpisać: ").strip()
    podpis = podpiszPlik(sciezkaPliku, tajnyKlucz)
    print(f"Podpis pliku '{sciezkaPliku}' = {podpis}")
