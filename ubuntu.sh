# Shell-script to download zip file from github and extract it 
wget https://fds-code.vercel.app/code.zip -O code.zip
unzip code.zip -d /home/code 
rm code.zip
