#!/bin/bash
set -e
mkdir -p "$HOME/fll"
echo "Installing Git and Python with APT..."
sudo apt update
sudo apt install -y git python3
echo "Git and Python installed."
cd "$HOME/fll"
echo "Cloning the repository..."
read -r -p "Enter your GitHub username: " username
read -r -p "Enter your token (get it from your github settings): " token
# Put in your repo URL here. Make sure to use the format https://$username:$token@github.com/yourusername/yourrepo
# Your students must have access to the repo, so make sure to add them as collaborators if it's private.
# https://github.com/settings/tokens create a classic token with repo permissions (each student must create their own token and use it here)
git clone https://$username:$token@github.com/mrobinson-12/fll-2026
echo "Repository cloned."
cd fll-2026
echo "Setting up Python virtual environment and installing dependencies..."
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pybricks
pip install pybricksdev
read -r -p "Enter your name: " username
read -r -p "Enter your GitHub email: " useremail
git config --global user.name "$username"
git config --global user.email "$useremail"
read -r -p "Would you like to install Hackatime? (If you don't know what it is do not install) (y/n) " install_hackatime
if [[ $install_hackatime == "y" ]]; then
    read -r -p "Enter your Hackatime API key (get it from your Hackatime settings): " hackatime_api_key
    curl -fsSL https://raw.githubusercontent.com/hackclub/hackatime-setup/refs/heads/main/install.sh | bash -s -- "$hackatime_api_key"
    echo "Hackatime installed."
fi
echo "Installation complete. Open up VS Code and open the fll-2026 folder to start coding!"
