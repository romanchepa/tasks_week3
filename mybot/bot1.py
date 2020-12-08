import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime



logging.basicConfig(filename="bot.log", level=logging.INFO)



def greet_user(update, context):
    print("Вызван/start")

    update.message.reply_text("Приветствую, пользователь!")


def wordcount(update, context):
    print("Вызван/wordcount")
    text = update.message.text
    lines=(len(text.split()))
    if lines !="":
      update.message.reply_text(f'{lines} слова')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(MessageHandler(Filters.text, wordcount))



    logging.info("Bot is running!")
    mybot.start_polling()
    mybot.idle()

if __name__=='__main__':
  main()


    
       