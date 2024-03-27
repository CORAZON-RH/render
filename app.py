import os
os.system("pip install fake_email") 
os.system("pip install thread")
os.system("pip install telebot")
os.system("pip install uuid")
os.system("pip install flask")
import telebot
import time
import random
from uuid import uuid4
from fake_email import Email
import re
import requests
from telebot import types
from flask import Flask, request
from threading import Thread
app = Flask('')
head ={
    "accept": "*/*",
    "accept-language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded",
    "dpr": "2.75",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
    "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-model": "\"Redmi Note 5\"",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-ch-ua-platform-version": "\"9.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "viewport-width": "393",
    "x-asbd-id": "129477",
    "x-csrftoken": "21gZFaWAF0U1zuCydPb8p9j827i8v6o9",
    "x-ig-app-id": "1217981644879628",
    "x-ig-www-claim": "0",
    "x-instagram-ajax": "1008803833",
    "x-mid": "ZQ3pAAABAAFZ5Xxm4l7zMaSU3SFp",
    "x-requested-with": "XMLHttpRequest"
}

bot = telebot.TeleBot("7088256457:AAHoi9xxJNyCJMFqemWpto7dfJJL06tC3cg")

@bot.message_handler(commands=["start"])
def startt(message):
    uid = uuid4()
    uis = uuid4()
    day = random.randint(1, 30)
    month = random.randint(1, 12)
    years = random.randint(1995, 2003)
    omar = 'omar'
    omar2 = ''.join(str(random.randint(1, 6)) for _ in range(6))
    random_omar = omar + omar2
    emaill = Email().Mail()
    email = emaill["mail"]
    print(email)
    bot.send_message(chat_id=message.chat.id, text=email)
    
    url1 = 'https://www.instagram.com/api/v1/accounts/send_verify_email/'
    data1= {
        'device_id': uis,
        'email': email,
    }
    
    r1 = requests.post(url1, headers=head, data=data1).text
    bot.send_message(chat_id=message.chat.id, text='انتظر')
    
    if 'email_sent' in r1:
        om = 'تم'
        bot.send_message(chat_id=message.chat.id, text=om)
    else:
        bot.send_message(chat_id=message.chat.id, text='مجاش لكود')
        time.sleep(13)
        messages = Email(emaill["session"]).inbox()
        message = str(messages)
        code = re.search(r'\d{6}', message).group()
        
        r2 = requests.post('https://www.instagram.com/api/v1/accounts/check_confirmation_code/', headers=head, data={
            'code': code,
            'device_id': uis,
            'email': email,
        }).json()
        
        rm = r2['signup_code']
    
        nn = '157.245.34.18:80'
        proxies = {f'http': 'https://{nn}'}
        password = 'omar dz'
        url = 'https://www.instagram.com/accounts/web_create_ajax/'
        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1695564035:{password}',
            'day': '24',
            'email': email,
            'first_name': random_omar,
            'month': '9',
            'username': random_omar,
            'year': years,
            'client_id': uis,
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': rm,
        }
        
        r3 = requests.post(url, headers=head, data=data, proxies=proxies).text
        
        if 'account_created' in r3:
            bot.send_message(chat_id=message.chat.id, text='تم إنشاء الحساب بنجاح')
            print(r3)
            bot.send_message(chat_id=message.chat.id, text='انتظر ريثما يصل الكود الى الايميل')
            
        else:
            bot.send_message(chat_id=message.chat.id, text='فشل في إنشاء الحساب')
            

@app.route('/')
def home():
    return "<b>telegram @X0_XV</b>"
def run():
    app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()
   
if __name__ == "__main__": 

    keep_alive() 
    
    bot.infinity_polling(skip_pending=True)