echo "Checking for git"
sudo apt-get install git

echo "Checking for python"
sudo apt-get install python

echo "Updating Presburn Application"
git clone https://github.com/YatesTech/presburn.git

echo "Launching..."
./main.py
