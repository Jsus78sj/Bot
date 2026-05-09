import time, redis, os, json, re, requests, asyncio, sys
from pyrogram import Client, idle
from datetime import datetime

r = redis.Redis('localhost', decode_responses=True)

print('''
Loading…
█▒▒▒▒▒▒▒▒▒''')

# === توليد الملفات ===
if not os.path.exists('information.py'):
    token = input('[+] Enter the bot token : ')
    Dev_Zaid = token.split(':')[0]
    if not r.get(f'{Dev_Zaid}botowner'):
        owner_id = int(input('[+] Enter SUDO ID : '))
        r.set(f'{Dev_Zaid}botowner', owner_id)
    else:
        owner_id = int(r.get(f'{Dev_Zaid}botowner'))
    
    with open('information.py', 'w') as f:
        f.write(f'token = "{token}"\nowner_id = {owner_id}\n')
else:
    from information import token, owner_id
    Dev_Zaid = token.split(':')[0]

print('''
30% 
█████▒▒▒▒▒ ''')

# === config.py ===
config_content = f'''
import redis
r = redis.Redis('localhost', decode_responses=True)
token = "{token}"
Dev_Zaid = token.split(':')[0]
sudo_id = {owner_id}
botUsername = "{requests.get(f"https://api.telegram.org/bot{token}/getMe").json()["result"]["username"]}"
from kvsqlite.sync import Client as DB
ytdb = DB('ytdb.sqlite')
sounddb = DB('sounddb.sqlite')
wsdb = DB('wsdb.sqlite')
'''

with open('config.py', 'w') as w:
    w.write(config_content)

from config import *

app = Client(
    f'{Dev_Zaid}r3d',
    api_id=9398500,
    api_hash="ad2977d673006bed6e5007d953301e13",
    bot_token=token,
    plugins={"root": "Plugins"}
)

if not r.get(f'{Dev_Zaid}:botkey'):
    r.set(f'{Dev_Zaid}:botkey', '⇜')

if not r.get(f'{Dev_Zaid}botname'):
    r.set(f'{Dev_Zaid}botname', 'رعد')

print('''
[===========================]
█████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚╝╚═════╝░╚═════╝░
[===========================]
🔮 R 3 D Source Started Successfully 🔮
''')

if r.get(f'DevGroup:{Dev_Zaid}'):
    try:
        app.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')), "تم تشغيل البوت بنجاح ✔️")
    except:
        pass

app.start()
idle()
