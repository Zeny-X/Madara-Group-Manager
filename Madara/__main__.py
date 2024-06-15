import logging
from telegram.ext import Updater
from Madara import config

# Import modules to ensure their handlers are registered
from Madara.modules import admin, afk, rules, logging as logging_module, warnings, welcome, faq

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Initialize the Updater and Dispatcher
    updater = Updater(token=config.API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    # Register the modules (if not automatically registered)
    admin.main()
    afk.main()
    rules.main()
    logging_module.main()
    warnings.main()
    welcome.main()
    faq.main()

    # Start the Bot
    updater.start_polling()
    logger.info("Bot started successfully.")
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
