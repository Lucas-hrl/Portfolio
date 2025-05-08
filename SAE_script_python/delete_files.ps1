Write-Output "Script PowerShell pour supprimer des fichiers sans confirmation"
Write-Output "Attention : cette suppression est définitive ..."
$reponse = Read-Host "Veuillez confirmer la suppression de tous ces fichiers : (OUI)"
if ($reponse -eq "OUI") {
    $confirmation = Read-Host "Êtes-vous bien certain(e) ? (OUI)"
    if ($confirmation -eq "OUI") {
        Remove-Item -Path "H:\IUT\Sae 1.02 - s'initier au réseau\Temp.zip.001" -Force
        Remove-Item -Path "H:\IUT\Sae 1.02 - s'initier au réseau\EVE-NG_SAE12.rar" -Force
        Remove-Item -Path "H:\IUT\EVE-NG_SAE12.7z" -Force
    } else {
        Write-Output "Opération annulée..."
    }
} else {
    Write-Output "Opération annulée..."
}