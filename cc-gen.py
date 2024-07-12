import telebot
from requests import get
import time,random,os
from telebot import types

token = '7323465079:AAEzXRyWhCJ4x6VrEdIcMIRt7Rvg93QxXw0'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    n = message.chat.first_name
    bot.reply_to(message, f'𝐇𝒊 » {n} \nSend Your Bin 6 Numper')
  
@bot.message_handler(func=lambda m:True)
#تلي @ttxxxn

def r(message):
    
    iy = message.text

    num = '1234567890'
    
    for i in range(3000):
        
        us = str("".join(random.choice(num)for i in range(10)))
        ue = str("".join(random.choice(num)for i in range(3)))
        
        ii = '01','02','03','04','05','06','07','08','09','10','11','12'
        
        um = random.choice(ii)
        num = '456789'
        u = str("".join(random.choice(num)for i in range(1)))
        
        us = str(iy + us + '|' + um + '|' + f'202{u}' + '|' + ue)
#جميع الحقوق محفوضه لدى حسو ال علي        

        with open("visa.txt", "a") as file:
            file.write(us + "\n")
    
    with open("visa.txt", "rb") as file:
        
        bot.send_document(message.chat.id, file)
        bot.send_message(message.chat.id,'<b>Good 3000 Vise\n~ ~ ~ ~ ~ ~ ~ ~ ~\nBy:@B_0_ta </b>',parse_mode='HTML')
        #الحقوق شرفك
        
        os.remove("visa.txt")
        
        
print('Running')

bot.infinity_polling()

