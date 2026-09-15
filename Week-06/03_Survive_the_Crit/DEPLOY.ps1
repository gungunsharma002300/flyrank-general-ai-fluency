# Safe deployment helper for Windows PowerShell
# Run this from your local flyrank-general-ai-fluency repository root.
# Review changes before committing.

$packageSite = Join-Path $PSScriptRoot "site"
$target = Join-Path (Get-Location) "Week-06\02_Open_It_on_Your_Phone\site"

if (!(Test-Path $target)) {
  New-Item -ItemType Directory -Path $target -Force | Out-Null
}

Copy-Item "$packageSite\*" $target -Recurse -Force

Write-Host ""
Write-Host "Portfolio files copied to:" $target
Write-Host ""
Write-Host "Next commands:"
Write-Host "git status"
Write-Host "git add Week-06/02_Open_It_on_Your_Phone/site"
Write-Host 'git commit -m "Fix Week 6 portfolio after peer critique"'
Write-Host "git push origin main"
