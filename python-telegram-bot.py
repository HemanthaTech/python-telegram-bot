import telegram
import openai
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

openai.api_key = os.environ['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']

def generate_response(message):
    prompt = f"User: {message}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your AI chatbot!")
    
def reply(update, context):
    message = update.message.text
    response = generate_response(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    updater = Updater(token=os.environ['6174101559:AAGD0F0lXrVZ9aWtPc4TSc8yDKquw7McO5U'], use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    reply_handler = MessageHandler(Filters.text & (~Filters.command), reply)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(reply_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
