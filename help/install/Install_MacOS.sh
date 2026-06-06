#!/bin/bash
set -e
echo "Installing Homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo "Homebrew installed."
mkdir -p "$HOME/fll"
echo "Installing Git and Python..."
brew install git
brew install python@3.13
echo "Git and Python installed."
cd "$HOME/fll"
echo "Cloning the repository..."
read -r -p "Enter your GitHub username: " username
read -r -p "Enter your token: " token
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
echo "Installation complete."
