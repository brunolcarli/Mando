from sys import stdout
from settings import TOKEN
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

'''

if __name__ == "__main__":
    stdout.write(banner)
    client.run(TOKEN)