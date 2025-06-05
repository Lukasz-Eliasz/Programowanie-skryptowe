"""
szyfrowanie_AES.py

Użycie:
    1. Uruchom skrypt.
    2. Wprowadź ścieżkę do pliku który chcesz zaszyfrować.
    3. Nowy plik z rozszerzeniem “.enc” zostanie stworzony w tym samym katalogu.

Opis skryptu:
  - Używa szyfrowania AES z losowo wygenerowanym kluczem (kluczAES = get_random_bytes(16)).
  - Zaszyfrowany plik jest przechowany w tym samym katalogu co oryginalny plik, z rozszerzeniem “.enc”.

Przykład:
    $ python szyfrowanie_AES.py
    Wprowadź scieżkę do pliku który chcesz zaszyfrować: plik.txt
    Zaszyfrowany plik został zapisany jako: plik.txt.enc
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

kluczAES = get_random_bytes(16)

def zaszyfrujPlik(sciezkaPliku):
    """
    Szyfruje plik przy użyciu algorytmu AES i zapisuje szyfrowanie jako nowy plik.

    Argumenty:
        sciezkaPliku (str): Scieżka do pliku który chcemy zaszyfrować.

    Działanie:
        - Odczytuje wszystkie bajty z podanego pliku.
        - tworzy nowy plik o nazwie sciezkaPliku + .enc.
        - Zapisuje 16 bajtów nonce, 16 bajtów tagu, a potem zaszyfrowane dane.
    """
    szyfr = AES.new(kluczAES, AES.MODE_EAX)

    with open(sciezkaPliku, 'rb') as plik:
        tekstJawny = plik.read()

    tekstZaszyfrowany, tag = szyfr.encrypt_and_digest(tekstJawny)

    sciezkaZaszyfrowanegoPliku = f"{sciezkaPliku}.enc"
    with open(sciezkaZaszyfrowanegoPliku, 'wb') as plik:
        plik.write(szyfr.nonce)
        plik.write(tag)
        plik.write(tekstZaszyfrowany)

    print(f"Zaszyfrowany plik został zapisany jako: {sciezkaZaszyfrowanegoPliku}")


if __name__ == "__main__":
    nazwaPliku = input("Wprowadź scieżkę do pliku który chcesz zaszyfrować: ").strip()
    zaszyfrujPlik(nazwaPliku)

