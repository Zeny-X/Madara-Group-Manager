import logging
from logging.handlers import RotatingFileHandler
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext
from Madara import dispatcher

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('madara_bot.log', maxBytes=5000000, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

def start_logging(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    logger.info(f"User {user.id} - {user.first_name} started the bot in chat {update.effective_chat.id}.")

def log_new_member(update: Update, context: CallbackContext) -> None:
    for member in update.message.new_chat_members:
        logger.info(f"New member {member.id} - {member.first_name} joined the chat {update.effective_chat.id}.")

def log_left_member(update: Update, context: CallbackContext) -> None:
    member = update.message.left_chat_member
    logger.info(f"Member {member.id} - {member.first_name} left the chat {update.effective_chat.id}.")

def log_message_deletion(update: Update, context: CallbackContext) -> None:
    logger.info(f"Message {update.message.message_id} deleted in chat {update.effective_chat.id}.")

def log_command(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    logger.info(f"User {user.id} - {user.first_name} issued command {update.message.text} in chat {update.effective_chat.id}.")

def main():
    dispatcher.add_handler(CommandHandler("start", start_logging))
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, log_new_member))
    dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, log_left_member))
    dispatcher.add_handler(MessageHandler(Filters.command, log_command))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.update.edited_message, log_message_deletion))

if __name__ == "__main__":
    main()
