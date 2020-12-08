import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime



logging.basicConfig(filename="bot.log", level=logging.INFO)



def greet_user(update, context):
    print("Вызван/start")

    update.message.reply_text("Приветствую, пользователь!")


def full_moon(update, context):
    print("Вызван/moon")
    if update.message.text == 'Когда ближайшее полнолуние?':
      d1 = ephem.next_full_moon('2019')
      update.message.reply_text(f'next_fool_moon {d1}')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("moon", full_moon))
    dp.add_handler(MessageHandler(Filters.text, full_moon))



    logging.info("Bot is running!")
    mybot.start_polling()
    mybot.idle()

if __name__=='__main__':
  main()


    
       
