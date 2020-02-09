from sys import stdout
from settings import TOKEN, SETTINGS_MODULE, __version__
from core.keep_alive import keep_alive
from core.commands import client


banner = r'''
       _______
    ,-'       `-,
   /             \
|`|   __/| |\__   |
|]|_______________|
| |\___       ___/|
| |    `\   /'    |
 \`-,    | |    ,-'
  |  \   | |   /  |
  |   \  | |  /   |
  |    | | | |    |
  |,_  | | | |  _,|
     `-|_|-|_|-'


   ╔╦╗┌─┐┌┐┌┌┬┐┌─┐
   ║║║├─┤│││ │││ │
   ╩ ╩┴ ┴┘└┘─┴┘└─┘
     Discord Bot
'''

if __name__ == "__main__":
    stdout.write(banner)
    stdout.write(f'Running Mando version: {__version__}\n')
    stdout.write(f'Settings module: {SETTINGS_MODULE}\n')

    if SETTINGS_MODULE == 'production':
        keep_alive()

    client.run(TOKEN)
