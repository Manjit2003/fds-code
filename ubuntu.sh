# Shell-script to download zip file from github and extract it 
sudo wget https://fds-code.vercel.app/code.zip -O code.zip
sudo unzip code.zip -d /home/code 
sudo rm code.zip
