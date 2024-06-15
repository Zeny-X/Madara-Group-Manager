# Madara/dispatcher.py
from telegram.ext import Updater
import logging
from config import API_KEY

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Initialize Updater and Dispatcher
updater = Updater(token=API_KEY, use_context=True)
dispatcher = updater.dispatcher
