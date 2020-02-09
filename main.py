from sys import stdout
from settings import TOKEN, __version__
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
    client.run(TOKEN)
