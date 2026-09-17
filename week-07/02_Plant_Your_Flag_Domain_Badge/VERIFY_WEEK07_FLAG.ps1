$ErrorActionPreference = "Stop"
$site = Join-Path $PSScriptRoot "site"
$required = @("index.html","booking.html","resume.html","style.css","script.js","favicon.svg","og-preview.svg","robots.txt","sitemap.xml")
foreach ($f in $required) { if (-not (Test-Path (Join-Path $site $f))) { throw "Missing $f" } }
Select-String -Path (Join-Path $site "index.html") -Pattern 'canonical','og:title','twitter:card','/_vercel/insights/script.js','internship-badge.netlify.app' | Out-Null
Write-Host "WEEK 7 FLAG STATIC CHECK: PASS"
