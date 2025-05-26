<#
    .SYNOPSIS
    Skrypt monitoruje folder źródłowy i przenosi pliki .txt do folderu docelowego.

    .DESCRIPTION
    Skrypt monitoruje folder źródłowy i automatycznie przenosi pliki z rozszerzeniem .txt
    do określonego folderu docelowego. Jeśli folder docelowy nie istnieje, jest tworzony.
    Skrypt działa w pętli, sprawdzając folder źródłowy co 10 sekund.

    .PARAMETER folderZrodlowy
    Ścieżka do folderu, który jest monitorowany pod kątem nowych plików .txt.

    .PARAMETER folderDocelowy
    Ścieżka do folderu, do którego przenoszone są pliki .txt.

    .EXAMPLE
    PS> .\PrzenoszeniePlikow.ps1
    Skrypt monitoruje folder źródłowy i przenosi pliki .txt do folderu docelowego.
#>

$folderZrodlowy = "C:\Users\PC\FolderZrodlowy"
$folderDocelowy = "C:\Users\PC\FolderDocelowy"

if (!(Test-Path $folderDocelowy)) { mkdir $folderDocelowy }

Write-Host "Monitoruje folder źródłowy (naciśnij Ctrl+C żeby zakończyć monitorowanie)."

while ($true) {
    Get-ChildItem -Path $folderZrodlowy -Filter *.txt | ForEach-Object {
        $plikPrzenoszony = Join-Path $folderDocelowy $_.Name
        Move-Item $_.FullName $plikPrzenoszony -Force
        Write-Host "Przeniesiono: $($_.Name)"
    }
    Start-Sleep -Seconds 10
}

