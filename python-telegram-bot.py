import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your bot!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    updater = Updater(token='6174101559:AAGD0F0lXrVZ9aWtPc4TSc8yDKquw7McO5U', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
