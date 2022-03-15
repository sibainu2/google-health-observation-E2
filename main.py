import requests
import datetime
import time


print("googleフォーム健康観察自動入力\nこの機能はアンケート入力をサポートする機能です。\n万一、アンケートが未入力、誤解答が発生しても作成者は一切責任をとりません。")

name=str(input("名前を入力してください。:"))
number=int(input("名簿番号を入力してください。:"))
sh=int(input("送信時:"))
sm=int(input("送信分:"))

dt_now = datetime.datetime.now()
url="https://docs.google.com/forms/d/e/1FAIpQLSckXp1xUTS7ktwprUtXeLYJyfZeZjr6O_3tE-aIqx7xNjrrTg/formResponse"

params = {
  'entry.246484525_year': f'{dt_now.year}',
  'entry.246484525_month': f'{dt_now.month}',
  'entry.246484525_day': f'{dt_now.day}',
  'entry.55904372': f'{number}',
  'entry.1112197045': f'{name}',
  'entry.401148155': '36.5度～36.9度',
  'entry.1258887026': '特になし',
}

def task():
    r = requests.get(url, params=params)
    print(r.url)
    print(r.status_code)
    
while True:
    now=datetime.datetime.now()
    if now.hour==sh and now.minute==sm and now.second ==0:
        task()
    time.sleep(1)
    
