from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from Madara import dispatcher
import random

def echo(update: Update, context: CallbackContext) -> None:
    text_to_echo = ' '.join(context.args)
    if text_to_echo:
        update.message.reply_text(text_to_echo)
    else:
        update.message.reply_text("You didn't provide any text to echo.")

def roll_dice(update: Update, context: CallbackContext) -> None:
    dice_result = random.randint(1, 6)
    update.message.reply_text(f"You rolled a {dice_result}!")

def joke(update: Update, context: CallbackContext) -> None:
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you get when you cross a snowman with a vampire? Frostbite.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    update.message.reply_text(random.choice(jokes))

def main():
    dispatcher.add_handler(CommandHandler("echo", echo, pass_args=True))
    dispatcher.add_handler(CommandHandler("roll", roll_dice))
    dispatcher.add_handler(CommandHandler("joke", joke))

if __name__ == "__main__":
    main()
