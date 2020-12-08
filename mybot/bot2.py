import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime



logging.basicConfig(filename="bot.log", level=logging.INFO)

CITIES = [Москва, Питер, Казань, Челябинск]

BOT_CITIES = [Альметьевск, Рязань, Новосибирск, Калининград]

def greet_user(update, context):
    print("Вызван/start")

    update.message.reply_text("Приветствую, пользователь!")


def cities (update, context):
    print("Вызван/cities")
    text = update.message.text
    
def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cities", cities))
    dp.add_handler(MessageHandler(Filters.text, wordcount))



    logging.info("Bot is running!")
    mybot.start_polling()
    mybot.idle()

if __name__=='__main__':
  main()

