<#
.SYNOPSIS
    Skrypt szyfruje plik a następnie zapisuje wynik działania w pliku.

.DESCRIPTION
    Skrypt szyfruje plik wejściowy o rozszerzeniu .txt następnie za pomocą algorytmu
    AES szyfruje dane w nim zawarte. Wyniki tego szyfrowania skrypt zapisuje do pliku 
    wyjściowego podanego przez użytkownika. Skrypt generuje losowy klucz AES i wyświetla 
    go do przyszłego odszyfrowania.

.PARAMETER sciezkaPlikuWejsciowego
    Pełna ścieżka do pliku wejściowego, który ma zostać zaszyfrowany.

.PARAMETER sciezkaPlikuWyjsciowego
    Pełna ścieżka do pliku wyjściowego, w którym zapisane zostanie wynik szyfrowania.

.EXAMPLE
    .\Szyfrowanie_AES.ps1 C:\Users\PC\bezSzyfrowania.txt C:\Users\PC\zSzyfrowaniem.txt

    Szyfruje plik "bezSzyfrowania.txt" i zapisuje zaszyfrowany wynik do "zSzyfrowaniem.txt"

.NOTES
    - Skrypt używa AES w trybie CBC
    - Klucz generowany jest losowo podczas każdego uruchomienia
#>

function utworzObiektAES($klucz, $IV) {
    $obiektAES = New-Object "System.Security.Cryptography.AesManaged"

    $obiektAES.Mode = [System.Security.Cryptography.CipherMode]::CBC

    $obiektAES.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
    $obiektAES.BlockSize = 128
    $obiektAES.KeySize = 256

    if ($IV) {
        if ($IV.getType().Name -eq "String") {
            $obiektAES.IV = [System.Convert]::FromBase64String($IV)
        }
        else {
            $obiektAES.IV = $IV
        }
    }

    if ($klucz) {
        if ($klucz.getType().Name -eq "String") {
            $obiektAES.Key = [System.Convert]::FromBase64String($klucz)
        }
        else {
            $obiektAES.Key = $klucz
        }
    }
    $obiektAES
}

function utworzKluczAes() {
    $obiektAES = utworzObiektAES
    $obiektAES.GenerateKey()
    [System.Convert]::ToBase64String($obiektAES.Key)
}

function zaszyfrujPlik($klucz, $sciezkaPliku) {
    $bajty = [System.IO.File]::ReadAllBytes($sciezkaPliku)
    $obiektAES = utworzObiektAES $klucz $null
    $szyfrator = $obiektAES.CreateEncryptor()
    $zaszyfrowaneDane = $szyfrator.TransformFinalBlock($bajty, 0, $bajty.Length);
    [byte[]] $pelneDane = $obiektAES.IV + $zaszyfrowaneDane
    [System.Convert]::ToBase64String($pelneDane)
}

$sciezkaPlikuWejsciowego = $Args[0]
$sciezkaPlikuWyjsciowego = $Args[1]

$klucz = utworzKluczAES

Write-Host "Szyfrowanie AES"
Write-Host "Klucz: $klucz"

$zaszyfrowanyPlik = zaszyfrujPlik $klucz $sciezkaPlikuWejsciowego

[System.IO.File]::WriteAllText($sciezkaPlikuWyjsciowego, $zaszyfrowanyPlik)

Write-Host "Plik zaszyfrowany i zapisany do: $sciezkaPlikuWyjsciowego"