curl -L -o https://raw.githubusercontent.com/Manjit2003/fds-code/main/code.zip
powershell -command "Expand-Archive -Path code.zip -DestinationPath C:\fds -Force"
powershell -command "Remove-Item -Path code.zip -Force"
powershell -command "Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine"
powershell -command "Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser"
powershell -command "Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process"