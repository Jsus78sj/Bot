import requests
from config import r

def get_creation_date(id: int) -> str:
    if r.get(f'{id}:CreateDate'):
      return r.get(f'{id}:CreateDate')
    else:
      url = "https://restore-access.indream.app/regdate"
      headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Nicegram/92 CFNetwork/1390 Darwin/22.0.0",
        "x-api-key": "e758fb28-79be-4d1c-af6b-066633ded128",
        "accept-language": "en-US,en;q=0.9"
      }
      data = {"telegramId":id}
      res = requests.post(url, headers=headers, json=data)
      r.set(f'{id}:CreateDate',res.json()['data']['date'].replace('-','/'))
      return res.json()['data']['date'].replace('-','/')
