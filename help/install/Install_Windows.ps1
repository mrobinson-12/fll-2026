# Note: This script is AI generated. 
$ErrorActionPreference = "Stop"

function Refresh-Path {
    $machinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $extraPaths = @(
        "$env:LOCALAPPDATA\Microsoft\WindowsApps",
        "$env:ProgramFiles\Git\cmd",
        "$env:LOCALAPPDATA\Programs\Python\Python312",
        "$env:LOCALAPPDATA\Programs\Python\Python312\Scripts"
    )

    $paths = @($machinePath, $userPath) + $extraPaths
    $env:Path = ($paths | Where-Object { $_ } | Select-Object -Unique) -join ";"
}

function Test-Command {
    param([Parameter(Mandatory = $true)][string]$Name)
    return $null -ne (Get-Command $Name -ErrorAction SilentlyContinue)
}

function Ensure-Winget {
    Refresh-Path
    if (Test-Command "winget") {
        return
    }

    Write-Host "winget was not found. Trying to register App Installer..."
    try {
        Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe
    } catch {
        Write-Host "App Installer registration did not complete: $($_.Exception.Message)"
    }

    Refresh-Path
    if (Test-Command "winget") {
        return
    }

    Write-Host "Installing winget/App Installer..."
    $wingetInstaller = Join-Path $env:TEMP "Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle"
    Invoke-WebRequest -Uri "https://aka.ms/getwinget" -OutFile $wingetInstaller
    Add-AppxPackage -Path $wingetInstaller

    Refresh-Path
    if (-not (Test-Command "winget")) {
        throw "winget installed, but it is still not available in PATH. Restart Windows or install App Installer from the Microsoft Store, then rerun this script."
    }
}

function Invoke-WingetInstall {
    param(
        [Parameter(Mandatory = $true)][string]$Id,
        [Parameter(Mandatory = $true)][string]$Name
    )

    Write-Host "Installing $Name..."
    winget install --id $Id --exact --source winget --silent --accept-package-agreements --accept-source-agreements --disable-interactivity
    if ($LASTEXITCODE -ne 0) {
        throw "$Name install failed."
    }

    Refresh-Path
}

function Ensure-Git {
    Refresh-Path
    if (-not (Test-Command "git")) {
        Invoke-WingetInstall -Id "Git.Git" -Name "Git"
    }

    Refresh-Path
    if (-not (Test-Command "git")) {
        throw "Git installed, but git.exe is still not available in PATH."
    }
}

function Get-Python312 {
    Refresh-Path

    if (Test-Command "py") {
        try {
            $version = (& py -3.12 --version 2>$null)
            if ($LASTEXITCODE -eq 0 -and $version -match "Python 3\.12") {
                return [PSCustomObject]@{
                    Exe = "py"
                    Args = @("-3.12")
                }
            }
        } catch {
        }
    }

    $candidates = @(
        "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
        "$env:ProgramFiles\Python312\python.exe",
        "${env:ProgramFiles(x86)}\Python312\python.exe"
    )

    foreach ($candidate in $candidates) {
        if (Test-Path $candidate) {
            $version = (& $candidate --version 2>$null)
            if ($version -match "Python 3\.12") {
                return [PSCustomObject]@{
                    Exe = $candidate
                    Args = @()
                }
            }
        }
    }

    if (Test-Command "python") {
        $version = (& python --version 2>$null)
        if ($version -match "Python 3\.12") {
            return [PSCustomObject]@{
                Exe = "python"
                Args = @()
            }
        }
    }

    return $null
}

function Ensure-Python312 {
    $python = Get-Python312
    if ($python) {
        return $python
    }

    Invoke-WingetInstall -Id "Python.Python.3.12" -Name "Python 3.12"
    $python = Get-Python312
    if (-not $python) {
        throw "Python 3.12 installed, but this PowerShell session still cannot find it."
    }

    return $python
}

function Invoke-Python {
    param(
        [Parameter(Mandatory = $true)]$PythonCommand,
        [Parameter(Mandatory = $true)][string[]]$Arguments
    )

    $exe = $PythonCommand.Exe
    $prefixArgs = @($PythonCommand.Args)

    if ([string]::IsNullOrWhiteSpace($exe)) {
        throw "Python 3.12 was detected incorrectly. The executable path was empty."
    }

    & $exe @prefixArgs @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Python command failed: $exe $($prefixArgs -join ' ') $($Arguments -join ' ')"
    }
}

Write-Host "Installing Git, Python, and project dependencies..."

Ensure-Winget
Ensure-Git
$python312 = Ensure-Python312
Write-Host "Using Python command: $($python312.Exe) $($python312.Args -join ' ')"

$fllRoot = Join-Path $env:USERPROFILE "fll"
$repoPath = Join-Path $fllRoot "fll-2026"

if (-not (Test-Path $fllRoot)) {
    New-Item -ItemType Directory -Path $fllRoot | Out-Null
}

if (Test-Path (Join-Path $repoPath ".git")) {
    Write-Host "Repository already exists."
} else {
    Write-Host "Cloning the repository..."
    $githubUser = Read-Host "Enter your GitHub username"
    $githubToken = Read-Host "Enter your token"
    git clone "https://${githubUser}:${githubToken}@github.com/mrobinson-12/fll-2026" $repoPath
    if ($LASTEXITCODE -ne 0) {
        throw "Repository clone failed."
    }
}

Set-Location $repoPath

Write-Host "Setting up Python virtual environment and installing dependencies..."
if (Test-Path ".venv") {
    Write-Host "Removing old virtual environment..."
    Remove-Item ".venv" -Recurse -Force
}

Invoke-Python -PythonCommand $python312 -Arguments @("-m", "venv", ".venv")

$venvPython = Join-Path $repoPath ".venv\Scripts\python.exe"
& $venvPython -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) {
    throw "pip upgrade failed."
}

& $venvPython -m pip install pybricks
if ($LASTEXITCODE -ne 0) {
    throw "pybricks install failed."
}

& $venvPython -m pip install pybricksdev
if ($LASTEXITCODE -ne 0) {
    throw "pybricksdev install failed. If the error says Microsoft Visual C++ 14.0 is required, install Microsoft C++ Build Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/"
}

$gitName = Read-Host "Enter your name"
$gitEmail = Read-Host "Enter your GitHub email"

git config --global user.name $gitName
git config --global user.email $gitEmail

Write-Host "Installation complete."
