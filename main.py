import time, redis, os, json, re, requests, asyncio
from aiohttp import web
from pyrogram import *

# ========== توكن البوت من متغير البيئة ==========
token = os.environ.get("8633959798:AAEg6VRZPlbN4mEuCW90EMD3lPTred3dIOo")
if not token:
    token = input('[+] Enter the bot token : ')

Dev_Zaid = token.split(':')[0]
owner_id = 8588392906  # مثبت حسب طلبك

# ========== إعداد Redis (بياناتك مباشرة) ==========
r = redis.Redis(
    host='redis-13109.c281.us-east-1-2.ec2.cloud.redislabs.com',
    port=13109,
    password='exuXI8ubbZbsHc3eQ9dXDi5Wbl65kapB',
    decode_responses=True
)

# ========== إعداد config.py بنفس اتصال Redis ==========
to_config = f'''
import redis
r = redis.Redis(
    host='redis-13109.c281.us-east-1-2.ec2.cloud.redislabs.com',
    port=13109,
    password='exuXI8ubbZbsHc3eQ9dXDi5Wbl65kapB',
    decode_responses=True
)
'''

# ========== أمور الإعداد الأولية ==========
print('Loading…')
if not r.get(f'{Dev_Zaid}botowner'):
    r.set(f'{Dev_Zaid}botowner', owner_id)

if not os.path.exists('information.py'):
    with open('information.py', 'w+') as f:
        f.write(f'token = "{token}"\nowner_id = {owner_id}')

to_config += f"\ntoken = '{token}'"
to_config += f"\nDev_Zaid = token.split(':')[0]"
to_config += f"\nsudo_id = {owner_id}"
username = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()["result"]["username"]
to_config += f"\nbotUsername = '{username}'"
to_config += "\nfrom kvsqlite.sync import Client as DB"
to_config += "\nytdb = DB('ytdb.sqlite')"
to_config += "\nsounddb = DB('sounddb.sqlite')"
to_config += "\nwsdb = DB('wsdb.sqlite')"

with open('config.py', 'w+') as w:
    w.write(to_config)

print('50% ready...')

app = Client(
    f'{Dev_Zaid}r3d', 9398500, 'ad2977d673006bed6e5007d953301e13',
    bot_token=token,
    plugins={"root": "Plugins"},
)

# الإعدادات الافتراضية
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

# ========== سيرفر ويب بسيط لمنع السبات ==========
async def handle_health(request):
    return web.Response(text="OK")

async def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    app_web = web.Application()
    app_web.router.add_get('/', handle_health)
    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Health server started on port {port}")

# ========== تشغيل البوت + السيرفر ==========
async def main():
    await app.start()
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
''')
    if r.get(f'DevGroup:{Dev_Zaid}'):
        id = int(r.get(f'DevGroup:{Dev_Zaid}'))
        try:
            await app.send_message(id, "تم اتشغيل البوت بنجاح ✔️")
        except:
            pass

    # تشغيل سيرفر الويب بنفس حلقة الحدث
    await run_web_server()
    await idle()

if __name__ == "__main__":
    app.loop.run_until_complete(main())
