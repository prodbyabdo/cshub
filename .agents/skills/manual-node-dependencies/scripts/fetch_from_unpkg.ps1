param (
    [Parameter(Mandatory=$true)]
    [string]$Package,

    [Parameter(Mandatory=$false)]
    [string]$Version = "latest",

    [Parameter(Mandatory=$false)]
    [string]$OutDir = "node_modules",

    [Parameter(Mandatory=$false)]
    [string]$Type = "cjs" # cjs, bundle, or es
)

$BaseUrl = "https://unpkg.com/$Package@$Version"

# Define common file paths based on type
$FileMap = @{
    "cjs" = "dist/index.cjs";
    "bundle" = "dist/$Package.bundle.js";
    "es" = "dist/index.mjs"
}

# If it's a specific file request (e.g. jszip.min.js), use that directly
if ($Package -match "\.js$") {
    $Url = "https://unpkg.com/$Package"
    $FileName = Split-Path $Package -Leaf
} else {
    $RelPath = $FileMap[$Type]
    $Url = "$BaseUrl/$RelPath"
    $FileName = "index.js"
}

$PackageDir = Join-Path $OutDir $Package
if (-not (Test-Path $PackageDir)) {
    New-Item -ItemType Directory -Path $PackageDir -Force | Out-Null
}

$OutFile = Join-Path $PackageDir $FileName

Write-Host "Fetching $Url to $OutFile..."
try {
    Invoke-WebRequest -Uri $Url -OutFile $OutFile -ErrorAction Stop
    Write-Host "[OK] Downloaded $Package"
} catch {
    Write-Error "Failed to download $Package from UNPKG. URL tried: $Url"
    exit 1
}
