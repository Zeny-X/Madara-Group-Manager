from telegram import Update, ParseMode
from telegram.ext import MessageHandler, Filters, CallbackContext
from Madara import dispatcher

WELCOME_MESSAGE = "Welcome to the group, {first_name}!"

def welcome(update: Update, context: CallbackContext) -> None:
    for new_member in update.message.new_chat_members:
        welcome_text = WELCOME_MESSAGE.format(first_name=new_member.first_name)
        update.message.reply_text(welcome_text, parse_mode=ParseMode.HTML)

def main():
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

if __name__ == "__main__":
    main()
