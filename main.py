import time, redis, os, json, re, requests, asyncio
from pyrogram import *

# ========== توكن البوت (من متغير البيئة للحماية) ==========
token = os.environ.get("8633959798:AAEg6VRZPlbN4mEuCW90EMD3lPTred3dIOo")
if not token:
    token = input('[+] Enter the bot token : ')

Dev_Zaid = token.split(':')[0]

# ========== معرف المطور (مثبت داخل الكود كما طلبت) ==========
owner_id = 8588392906

# ========== إعداد Redis المضمّن (بياناتك مباشرة) ==========
r = redis.Redis(
    host='redis-13109.c281.us-east-1-2.ec2.cloud.redislabs.com',
    port=13109,
    password='exuXI8ubbZbsHc3eQ9dXDi5Wbl65kapB',
    decode_responses=True
)

# ========== ملف config.py بنفس اتصال Redis ==========
to_config = f'''
import redis
r = redis.Redis(
    host='redis-13109.c281.us-east-1-2.ec2.cloud.redislabs.com',
    port=13109,
    password='exuXI8ubbZbsHc3eQ9dXDi5Wbl65kapB',
    decode_responses=True
)
'''

print('''
Loading…
█▒▒▒▒▒▒▒▒▒''')
print('\n\n')

# حفظ المطور في Redis (لن يؤثر إذا كان موجوداً مسبقاً)
if not r.get(f'{Dev_Zaid}botowner'):
    r.set(f'{Dev_Zaid}botowner', owner_id)

# إنشاء information.py للاستخدام المحلي (اختياري)
if not os.path.exists('information.py'):
    with open('information.py', 'w+') as f:
        f.write(f'token = "{token}"\nowner_id = {owner_id}')

print('''
10% 
███▒▒▒▒▒▒▒ ''')

to_config += f"\ntoken = '{token}'"
to_config += f"\nDev_Zaid = token.split(':')[0]"
to_config += f"\nsudo_id = {owner_id}"
username = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()["result"]["username"]
to_config += f"\nbotUsername = '{username}'"
to_config += "\nfrom kvsqlite.sync import Client as DB"
to_config += "\nytdb = DB('ytdb.sqlite')"
to_config += "\nsounddb = DB('sounddb.sqlite')"
to_config += "\nwsdb = DB('wsdb.sqlite')"

print('''
30% 
█████▒▒▒▒▒ ''')
with open('config.py', 'w+') as w:
    w.write(to_config)
print('''
50% 
███████▒▒▒ ''')

app = Client(f'{Dev_Zaid}r3d', 9398500, 'ad2977d673006bed6e5007d953301e13',
    bot_token=token,
    plugins={"root": "Plugins"},
)

# إعدادات افتراضية
if not r.get(f'{Dev_Zaid}:botkey'):
    r.set(f'{Dev_Zaid}:botkey', '⇜')
if not r.get(f'{Dev_Zaid}botname'):
    r.set(f'{Dev_Zaid}botname', 'رعد')
if not r.get(f'{Dev_Zaid}botchannel'):
    r.set(f'{Dev_Zaid}botchannel', 'eFFb0t')

def Find(text):
    m = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(m, text)
    return [x[0] for x in url]

app.start()

print('''
[===========================]

█████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░

[===========================]

🔮 Your bot started successfully on R 3 D ☆ Source 🔮

•••••••• @yqyqy66 - @yqyqy66 •••••••••


''')
print('''

100% 
██████████''')

if r.get(f'DevGroup:{Dev_Zaid}'):
    id = int(r.get(f'DevGroup:{Dev_Zaid}'))
    try:
        app.send_message(id, "تم اتشغيل البوت بنجاح ✔️")
    except:
        pass

idle()
