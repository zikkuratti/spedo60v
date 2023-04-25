апк https://drive.google.com/file/d/1d5epZ_sNJZSjgKHjp_2zzvXmurUUkYkj/view?usp=sharing

Порядок установки на 22 Ubuntu
не из под рута

 mkdir spedo
 
 2006  cd spedo/
 
 2007  nano main.py
 
 2008  pip3 install --user --upgrade buildozer
 
 2009  sudo apt update
 
 2010  sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
 
 2011  pip3 install --user --upgrade Cython==0.29.33 virtualenv
 
 2012  export PATH=$PATH:~/.local/bin/
 
 2015  buildozer init
 
 2016  nano buildozer.spec (пишем название)
 
 2017  buildozer -v android debug deploy
 
 2019  cd bin/
