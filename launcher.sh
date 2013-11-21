

echo "Checking for git"
sudo apt-get install git

echo "Checking for python"
sudo apt-get install python

echo "Updating Presburn Application"
git clone https://github.com/YatesTech/presburn.git
echo "Moving to the required directory."
cd presburn-master
echo "Making Program Launchable"
chmod 755 main.py
echo "Launching..."
./main.py
