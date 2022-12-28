curl https://fds-code.vercel.app/code.zip -o code.zip
powershell -command "Expand-Archive -Path code.zip -DestinationPath C:\fds -Force"
powershell -command "Remove-Item -Path code.zip -Force"
