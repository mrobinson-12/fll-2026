set -e
mkdir -p "$HOME/fll"
brew install git
brew install python@3.13
cd "$HOME/fll"
read -r -p "Enter your GitHub username: " username
read -r -p "Enter your token: " token
git clone https://$username:$token@github.com/mrobinson-12/fll-2026
cd fll-2026
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