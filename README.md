# discord-drive
A simple repository to save files from one of my servers on google drive.

This bot downloads any image/gif/video (or anything that you would be able to use wget) and upload it to Google Drive.

**It only works on Linux** _but it shouldn't be too hard to tweak it to work on windows as well_


## Set Up:
  ### pip requirements
  ```
  pip3 install discord.py pydrive
  ```
  ### bot.ini
  The config file.
  ```
  [BOT]
  TOKEN = your discord token here.
  ```
  
  ### settings.yaml
  You can follow [this authentication guide](https://pythonhosted.org/PyDrive/quickstart.html) to get your client_id and secret.
  The application type should be **Desktop**.
  ```
  client_config_backend: settings
  client_config:
      client_id: your client id from Google Drive API
      client_secret: and your client secret from Google Drive API


  save_credentials: True
  save_credentials_backend: file
  save_credentials_file: credentials.json

  get_refresh_token: True
  ```
  
  ### Code
  This bot was written specifically for my Discord Server so it is in portuguese, but below you will find where to change the code if you want to translate it:
  
  1. Inside the "foto" exception -> ("Alguma coisa deu errado") means ("Something went wrong")
  2. The ctx.send of that same method ("Foto salva com sucesso" means ("Photo sucessfully saved")
  3. You will also want to change the name of the roles on the `@commands.has_any_role('Tchola'...)` to match the roles from your server.
  
## Contact:
You can DM me on Discord @ Samore#6337 and if you need help running it I will do my best to help :).
