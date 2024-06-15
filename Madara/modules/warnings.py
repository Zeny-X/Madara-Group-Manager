from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from Madara import dispatcher
import json
import os

WARNINGS_FILE = 'user_warnings.json'

# Load existing warnings from file
def load_warnings():
    if os.path.exists(WARNINGS_FILE):
        with open(WARNINGS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save warnings to file
def save_warnings(warnings):
    with open(WARNINGS_FILE, 'w') as file:
        json.dump(warnings, file)

# Dictionary to store warnings
WARNINGS = load_warnings()

MAX_WARNINGS = 3  # Maximum number of warnings before action is taken

def warn_user(update: Update, context: CallbackContext) -> None:
    user = update.message.reply_to_message.from_user if update.message.reply_to_message else None
    if not user:
        update.message.reply_text("Please reply to the user you want to warn.")
        return

    chat_id = update.effective_chat.id
    user_id = user.id

    # Check if the user is already warned
    if chat_id not in WARNINGS:
        WARNINGS[chat_id] = {}
    if user_id not in WARNINGS[chat_id]:
        WARNINGS[chat_id][user_id] = 0

    WARNINGS[chat_id][user_id] += 1
    save_warnings(WARNINGS)

    warnings_count = WARNINGS[chat_id][user_id]
    update.message.reply_text(f"{user.first_name} has been warned. Total warnings: {warnings_count}")

    if warnings_count >= MAX_WARNINGS:
        try:
            context.bot.kick_chat_member(chat_id, user_id)
            update.message.reply_text(f"{user.first_name} has been kicked from the group due to exceeding the maximum number of warnings.")
            del WARNINGS[chat_id][user_id]
            save_warnings(WARNINGS)
        except Exception as e:
            update.message.reply_text(f"Failed to kick user. Error: {e}")

def reset_warnings(update: Update, context: CallbackContext) -> None:
    user = update.message.reply_to_message.from_user if update.message.reply_to_message else None
    if not user:
        update.message.reply_text("Please reply to the user you want to reset warnings for.")
        return

    chat_id = update.effective_chat.id
    user_id = user.id

    if chat_id in WARNINGS and user_id in WARNINGS[chat_id]:
        del WARNINGS[chat_id][user_id]
        save_warnings(WARNINGS)
        update.message.reply_text(f"Warnings for {user.first_name} have been reset.")
    else:
        update.message.reply_text(f"{user.first_name} has no warnings.")

def main():
    dispatcher.add_handler(CommandHandler("warn", warn_user))
    dispatcher.add_handler(CommandHandler("resetwarns", reset_warnings))

if __name__ == "__main__":
    main()
