from telegram import Update
from telegram.ext import MessageHandler, Filters, CallbackContext
from Madara import dispatcher
import logging

# Set up the logging configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("group_events.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def user_joined(update: Update, context: CallbackContext) -> None:
    for new_member in update.message.new_chat_members:
        logger.info(f"User {new_member.username} (ID: {new_member.id}) joined the group {update.effective_chat.title} (ID: {update.effective_chat.id}).")

def user_left(update: Update, context: CallbackContext) -> None:
    user = update.message.left_chat_member
    logger.info(f"User {user.username} (ID: {user.id}) left the group {update.effective_chat.title} (ID: {update.effective_chat.id}).")

def user_kicked(update: Update, context: CallbackContext) -> None:
    user = update.message.left_chat_member
    if user:
        logger.info(f"User {user.username} (ID: {user.id}) was kicked from the group {update.effective_chat.title} (ID: {update.effective_chat.id}).")

def main():
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, user_joined))
    dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, user_left))
    dispatcher.add_handler(MessageHandler(Filters.status_update.kicked_chat_member, user_kicked))

if __name__ == "__main__":
    main()
