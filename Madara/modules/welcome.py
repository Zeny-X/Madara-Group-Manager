from telegram import Update, ParseMode
from telegram.ext import MessageHandler, Filters, CallbackContext
from Madara import dispatcher

WELCOME_MESSAGES = [
    "Welcome to the group, {first_name}!",
    "Hello {first_name}, glad to have you here!",
    "Hi {first_name}, welcome aboard!",
    "Hey {first_name}! Welcome to the group!",
    "Greetings {first_name}! We're happy to see you!",
    "Welcome {first_name}, enjoy your stay!"
]

WELCOME_STICKERS = [
    "CAADAgADQAADwDZPE7p6OR3it2bXAg",
    "CAADAgADZwADwDZPE4dKqAEOHi5JAg",
    "CAADAgADaAADwDZPE4dHNNIM5k-bAg",
    "CAADAgADbAADwDZPE5Q6gQ1K5s5GAg",
    "CAADAgADcAADwDZPE8V3lJK7W7O8Ag"
]

def send_welcome_message(update: Update, context: CallbackContext) -> None:
    for new_member in update.message.new_chat_members:
        welcome_text = random.choice(WELCOME_MESSAGES).format(first_name=new_member.first_name)
        update.message.reply_text(welcome_text, parse_mode=ParseMode.HTML)
        sticker_id = random.choice(WELCOME_STICKERS)
        context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=sticker_id)

def main():
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, send_welcome_message))

if __name__ == "__main__":
    main()
