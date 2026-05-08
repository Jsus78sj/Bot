from config import *
import re
def get_rank(id, cid) -> str:
   if id == 6646631745 or id == 6646631745:
      return 'Aec🎖️'
   if id == int(Dev_Zaid):
      return 'البوت'
   if id == int(r.get(f'{Dev_Zaid}botowner')):
      return 'Dev🎖️'
   if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return 'Dev²🎖'
   if r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return 'Myth🎖️'
   if r.get(f'{id}:gban:{Dev_Zaid}'):
      return 'محظور عام'
   if r.get(f'{id}:mute:{Dev_Zaid}'):
      return 'محظور عام'
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      if r.get(f'{cid}:RankGowner:{Dev_Zaid}'):
         return r.get(f'{cid}:RankGowner:{Dev_Zaid}')
      return 'المالك الاساسي'
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      if r.get(f'{cid}:RankOwner:{Dev_Zaid}'):
         return r.get(f'{cid}:RankOwner:{Dev_Zaid}')
      return 'المالك'
   if r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
      if r.get(f'{cid}:RankMod:{Dev_Zaid}'):
         return r.get(f'{cid}:RankMod:{Dev_Zaid}')
      return 'المدير'
   if r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
      if r.get(f'{cid}:RankAdm:{Dev_Zaid}'):
         return r.get(f'{cid}:RankAdm:{Dev_Zaid}')
      return 'ادمن'
   if r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
      if r.get(f'{cid}:RankPre:{Dev_Zaid}'):
         return r.get(f'{cid}:RankPre:{Dev_Zaid}')
      return 'مميز'
   else:
      if r.get(f'{cid}:RankMem:{Dev_Zaid}'):
         return r.get(f'{cid}:RankMem:{Dev_Zaid}')
      return 'عضو'

def admin_pls(id, cid) -> bool:
   # ...
def mod_pls(id, cid) -> bool:
   # ...
def owner_pls(id, cid) -> bool:
   # ...
def gowner_pls(id, cid) -> bool:
   # ...
def dev_pls(id, cid) -> bool:
   # ...
def dev2_pls(id, cid) -> bool:
   # ...
def devp_pls(id, cid) -> bool:
   # ...
def pre_pls(id, cid) -> bool:
   # ...
def get_devs_br():
   # ...
def isLockCommand(fid: int, cid: int, text: str):
   # ...
# (جميع الدوال كما في الملف الأصلي غير مذكورة للاختصار)
