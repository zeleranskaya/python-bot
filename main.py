from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import random

TOKEN = '1674333840:AAFLZArcrir6XRox4Sssy8FGlZysmsOq1qI'

hi = ['приветствую, мой друг', 'я рад видеть тебя!', 'давно не виделись!']
help = ['чем тебе помочь?', 'у тебя есть какие-то проблемы?']
what = ['выбери команду, я не понимаю тебя']

randomizer = random.SystemRandom()

def main():
    updater = Updater(token=TOKEN)  # объект, который ловит сообщения от Telegram

    dispather = updater.dispatcher

    handler = MessageHandler(Filters.all, do_echo)
    start_handler = CommandHandler('start', do_start)
    help_handler = CommandHandler('help', do_help)

    dispather.add_handler(help_handler)
    dispather.add_handler(start_handler)
    dispather.add_handler(handler)

    updater.start_polling()
    updater.idle()


def do_echo(update, context):

    update.message.reply_text(randomizer.choice(what))


def do_start(update, context):

    update.message.reply_text(randomizer.choice(hi))


def do_help(update: Update, context):

    user_id = update.message.from_user.id
    name = update.message.from_user.first_name
    update.message.reply_text(text=f'привет, {name}!\nтвой id: {user_id}')


main()
