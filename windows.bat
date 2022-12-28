curl https://raw.githubusercontent.com/Manjit2003/fds-code/main/code.zip -o code.zip
powershell -command "Expand-Archive -Path code.zip -DestinationPath C:\fds -Force"
powershell -command "Remove-Item -Path code.zip -Force"
