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
  'entry.1322117479_year': f'{dt_now.year}',
  'entry.1322117479_month': f'{dt_now.month}',
  'entry.1322117479_day': f'{dt_now.day}',
  'entry.1571997150': f'{number}',
  'entry.545271842': f'{name}',
  'entry.71655832': '36.0度～36.4度',
  'entry.1288998435': '特になし',
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
    
