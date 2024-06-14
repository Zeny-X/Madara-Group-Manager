from telegram import Update, ParseMode
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext
from Madara import dispatcher

AFK_USERS = {}

def afk(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    reason = ' '.join(context.args) if context.args else 'No reason provided'
    AFK_USERS[user.id] = reason
    update.message.reply_text(f"{user.first_name} is now AFK: {reason}")

def no_longer_afk(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    if user.id in AFK_USERS:
        del AFK_USERS[user.id]
        update.message.reply_text(f"Welcome back, {user.first_name}!", quote=True)

def mention_handler(update: Update, context: CallbackContext) -> None:
    for user_id in AFK_USERS:
        if update.message.reply_to_message and update.message.reply_to_message.from_user.id == user_id:
            reason = AFK_USERS[user_id]
            update.message.reply_text(f"{update.message.reply_to_message.from_user.first_name} is AFK: {reason}", quote=True)
        elif f"@{update.message.from_user.username}" in update.message.text:
            reason = AFK_USERS[user_id]
            update.message.reply_text(f"{update.message.from_user.first_name} is AFK: {reason}", quote=True)

def main():
    dispatcher.add_handler(CommandHandler("afk", afk, pass_args=True))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, mention_handler))
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, no_longer_afk))

if __name__ == "__main__":
    main()
