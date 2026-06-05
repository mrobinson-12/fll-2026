# PowerShell installer adapted from Install_MacOS.sh
$ErrorActionPreference = 'Stop'

# Create target folder
$dest = Join-Path $env:USERPROFILE 'fll'
if (-not (Test-Path -Path $dest)) {
    New-Item -ItemType Directory -Path $dest | Out-Null
}

function Install-WithPackageManager {
    param(
        [string]$wingetId,
        [string]$chocoId,
        [string]$name
    )

    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Write-Host "Installing $name with winget..."
        winget install --id $wingetId -e --accept-package-agreements --accept-source-agreements
    } elseif (Get-Command choco -ErrorAction SilentlyContinue) {
        Write-Host "Installing $name with choco..."
        choco install $chocoId -y
    } else {
        Write-Host "No package manager (winget or choco) found. Please install $name manually and re-run this script."
        exit 1
    }
}

# Install Git if missing
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Install-WithPackageManager -wingetId 'Git.Git' -chocoId 'git' -name 'Git'
}

# Ensure Python 3.13 is available (install if necessary)
function Test-PythonVersion {
    param(
        [string]$cmd,
        [string]$args
    )
    try {
        if ([string]::IsNullOrEmpty($args)) {
            $out = & $cmd -c "import sys, json; print(json.dumps([sys.version_info.major, sys.version_info.minor]))" 2>$null
        } else {
            $out = & $cmd $args -c "import sys, json; print(json.dumps([sys.version_info.major, sys.version_info.minor]))" 2>$null
        }
        if (-not $out) { return $null }
        $ver = $out | ConvertFrom-Json
        return $ver
    } catch {
        return $null
    }
}

function Ensure-Python313 {
    # Try common Python launchers
    $candidates = @(
        @{cmd='py'; args='-3.13'},
        @{cmd='python'; args=''},
        @{cmd='py'; args='-3'},
        @{cmd='py'; args=''}
    )

    foreach ($c in $candidates) {
        $ver = Test-PythonVersion -cmd $c.cmd -args $c.args
        if ($ver -and $ver[0] -eq 3 -and $ver[1] -eq 13) {
            return $c
        }
    }

    # Attempt to install Python 3.13 via winget/choco
    Install-WithPackageManager -wingetId 'Python.Python.3.13' -chocoId 'python' -name 'Python 3.13'

    # Re-check after install
    foreach ($c in $candidates) {
        $ver = Test-PythonVersion -cmd $c.cmd -args $c.args
        if ($ver -and $ver[0] -eq 3 -and $ver[1] -eq 13) {
            return $c
        }
    }

    Write-Host 'Python 3.13 was not found or installed. Please install Python 3.13 and re-run this script.'
    exit 1
}

# Ensure Python 3.13 is present and get command/args
$pythonLauncher = Ensure-Python313
if ($null -eq $pythonLauncher) { exit 1 }

$pythonCmd = $pythonLauncher.cmd
$pythonArgs = $pythonLauncher.args

Set-Location -Path $dest

# Prompt for GitHub credentials
$username = Read-Host -Prompt 'Enter your GitHub username'
$tokenSecure = Read-Host -Prompt 'Enter your token' -AsSecureString
$ptr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($tokenSecure)
$token = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($ptr)
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)

# Escape token for URL (basic)
$tokenEscaped = [System.Uri]::EscapeDataString($token)

# Clone repository
$repoUrl = "https://$($username):$($tokenEscaped)@github.com/mrobinson-12/fll-2026"
git clone $repoUrl

Set-Location -Path (Join-Path $dest 'fll-2026')

# Create and activate virtual environment using the discovered Python 3.13
if ([string]::IsNullOrEmpty($pythonArgs)) {
    & $pythonCmd -m venv .venv
} else {
    & $pythonCmd $pythonArgs -m venv .venv
}

# Activate the venv for this script session
$activatePath = Join-Path (Get-Location) '.venv\Scripts\Activate.ps1'
if (Test-Path $activatePath) {
    & $activatePath
} else {
    Write-Host "Activation script not found at $activatePath. You can activate manually: .\.venv\Scripts\Activate.ps1"
}

# Upgrade pip and install packages inside the selected interpreter
if ([string]::IsNullOrEmpty($pythonArgs)) {
    & $pythonCmd -m pip install --upgrade pip
    & $pythonCmd -m pip install pybricks pybricksdev
} else {
    & $pythonCmd $pythonArgs -m pip install --upgrade pip
    & $pythonCmd $pythonArgs -m pip install pybricks pybricksdev
}

# Configure git user
$name = Read-Host -Prompt 'Enter your name'
$useremail = Read-Host -Prompt 'Enter your GitHub email'
git config --global user.name "$name"
git config --global user.email "$useremail"

Write-Host 'Installation complete.'
