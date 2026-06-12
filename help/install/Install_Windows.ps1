$ErrorActionPreference = 'Stop'
#Ensure stopping if errors occur. This is important for installation scripts to prevent partial installations.
mkdir "$HOME\fll"
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
Write-Host "Repository cloned succesfully" -ForgroundColor Green
#Report succesful cloning
cd fll-2026
#Navigate to cloned repo
Write-Host "Setting up python venv and installing required dependencies..."
#inform user of next steps - python venv and dependencies
python -m venv.venv
#setup python virtual envirmnt


#!/bin/bash
#set -e✅
#echo "Installing Homebrew if not already installed..."✅
#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"✅
#echo "Homebrew installed."✅
#mkdir -p "$HOME/fll"✅
#echo "Installing Git and Python with Homebrew..."✅
#brew install git✅
#brew install python@3.13✅
#echo "Git and Python installed."✅
#cd "$HOME/fll"✅
#echo "Cloning the repository..."✅
#read -r -p "Enter your GitHub username: " username✅
#read -r -p "Enter your token (get it from your github settings): " token✅
# Put in your repo URL here. Make sure to use the format https://$username:$token@github.com/yourusername/yourrepo
# Your students must have access to the repo, so make sure to add them as collaborators if it's private.
# https://github.com/settings/tokens create a classic token with repo permissions (each student must create their own token and use it here)
#git clone https://$username:$token@github.com/mrobinson-12/fll-2026✅
#echo "Repository cloned."✅
#cd fll-2026✅
#echo "Setting up Python virtual environment and installing dependencies..."✅
#python3 -m venv .venv✅
#source .venv/bin/activate
#pip install --upgrade pip
#pip install pybricks
#pip install pybricksdev
#read -r -p "Enter your name: " username
#read -r -p "Enter your GitHub email: " useremail
#git config --global user.name "$username"
#git config --global user.email "$useremail"
#read -r -p "Would you like to install Hackatime? (If you don't know what it is do not install) (y/n) " install_hackatime
#if [[ $install_hackatime == "y" ]]; then
    #read -r -p "Enter your Hackatime API key (get it from your Hackatime settings): " hackatime_api_key
    #curl -fsSL https://raw.githubusercontent.com/hackclub/hackatime-setup/refs/heads/main/install.sh | bash -s -- "$hackatime_api_key"
    #echo "Hackatime installed."
#fi
#echo "Installation complete. Open up VS Code and open the fll-2026 folder to start coding!"
