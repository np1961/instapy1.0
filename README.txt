

#install instapy1.0 
#1080x1920 display

sudo apt-get install python3-tk python3-dev
sudo apt install python3-venv
sudo apt install python3-pip

git clone https://github.com/np1961/instapy1.0 instagram



#venv
mkdir environments
cd environments
python3 -m venv instapy1.0
source instapy1.0/bin/activate
cd 



#pip install python libs
cd instagram/config
python3 -m pip install --upgrade pip
pip install -r requirements.txt
cd ..




cd instagram/<<<username>>>/

#cookies generate !!!
python3 new_cookies.py

#play
python3 application.py
