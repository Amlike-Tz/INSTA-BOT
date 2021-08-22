#! usr/bin/bash

clear

center() {
  termwidth=$(stty size | cut -d" " -f2)
  padding="$(printf '%0.1s' ={1..500})"
  printf '%*.*s %s %*.*s\n' 0 "$(((termwidth-2-${#1})/2))" "$padding" "$1" 0 "$(((termwidth-1-${#1})/2))" "$padding"
}

echo -e "\033[92m"
echo
echo

center "STARING TO INSTALL DEPENDENCIES"
sleep 3

cod="\033[0m"
o="\033[91m"
grn="\033[92m"
blu="\033[34m"

cd $SCHOME

#Pillow Installatation


python3 -m pip install --upgrade pip

pip install wheel

pkg install libjpeg-turbo LDFLAGS="-L/system/lib/" CFLAGS="-I/data/data/com.termux/files/usr/include/"

clear

center "STARING TO INSTALL PILLOW"

sleep 2

pip install Pillow

clear

echo
echo
echo
center "STARING TO INSTALL INSTA-BOT BY AMKIKETZ"

sleep 3

pip install instabot
 
pip install requests

clear

sleep 1

echo
echo

echo -e "$blue HONGERA INSTALLATION COMPLITED"

sleep 2

cd

cd INSTA-BOT

python start.py

