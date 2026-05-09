#!/bin/bash
echo "جاري تنصيب رعد..."
sudo apt-get update -y
sudo apt-get install ffmpeg redis-server python3-pip -y
sudo service redis-server start

pip3 install -r requirements.txt

echo "✅ تم التنصيب بنجاح"
echo "شغل البوت بـ: screen -S r3d python3 main.py"
