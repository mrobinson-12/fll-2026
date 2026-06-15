$ErrorActionPreference = 'Stop'
#Ensure stopping if errors occur. This is important for installation scripts to prevent partial installations.
mkdir "$HOME\fll" -Force
#makes fll directory
Write-Host "Intstalling Git and Python via winget..."
#Inform user of installing git and python
winget install --id Git.Git -e 
#Git install
winget install --id Python.Python3 -e
#Python install
Write-Host "Git and Python installed succesfully" -ForegroundColor Green
#inform user of successful install
cd "$HOME\fll"
#navigate to fll folder
Write-Host "Cloning Repository..."
#Inform user of cloning repo
$Username = Read-Host "Enter your Github username: "
#Get GitHub username
$Token = Read-Host "Enter your token (Get it from your GitHub settings): "
#Get token
git clone "https://$($Username):$($Token)@github.com/mrobinson-12/fll-2026"
#Clone repo
Write-Host "Repository cloned succesfully" -ForegroundColor Green
#Report succesful cloning
cd fll-2026
#Navigate to cloned repo
Write-Host "Setting up python venv and installing required dependencies..."
#inform user of next steps - python venv and dependencies
python -m venv .venv
#setup python virtual envirmnt
.venv\Scripts\Activate.ps1
#activate python virtual envirmnt
python -m pip install --upgrade pip
#upgrade pip
python -m pip install pybricks
#install pybricks
python -m pip install pybricksdev
#install pybricksdev
#$User_name = Read-Host "Enter your name: "
#get user name imma not use bc why tf is this in the bash
$Useremail = Read-Host "Enter your GitHub email: "
#get user email
git config --global user.name "$Username"
git config --global user.email "$Useremail"
$install_hackatime = Read-Host "Would you like to install Hackatime? (If you don't know what it is do not install) (y/n)"
#ask user if they want to install hackatime
if ($install_hackatime -eq "y") {
$hackatime_api_key = Read-Host "Enter your Hackatime API key (get it from your Hackatime settings): "
#Get hackatime api key
irm https://raw.githubusercontent.com/hackclub/hackatime-setup/main/install.ps1 | iex; & hackatime-setup --yes -- "$hackatime_api_key"
#stuff i dont understand but it installs hackatime
Write-Host "Hackatime installed succesfully" -ForegroundColor Green
}
Write-Host "Installation complete. Open up VS Code and open the fll-2026 folder to start coding!" -ForegroundColor Green

