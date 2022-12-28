# Shell-script to download zip file from github and extract it 
wget https://raw.githubusercontent.com/Manjit2003/fds-code/main/code.zip -O code.zip
unzip code.zip -d /home/code 
rm code.zip
