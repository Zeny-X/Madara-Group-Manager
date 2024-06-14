import logging
from Madara import config  # Make sure this matches your directory and config structure
from Madara.modules import *  # This imports all modules
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define a start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am Madara, your group manager bot.')

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(config.Config.API_KEY)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
