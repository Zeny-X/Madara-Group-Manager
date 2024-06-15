import json
import os
from telegram import Update, ParseMode
from telegram.ext import CommandHandler, CallbackContext
from Madara import dispatcher

RULES_FILE = 'group_rules.json'

# Load existing rules from file
def load_rules():
    if os.path.exists(RULES_FILE):
        with open(RULES_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save rules to file
def save_rules(rules):
    with open(RULES_FILE, 'w') as file:
        json.dump(rules, file, indent=4)

# Dictionary to store rules
GROUP_RULES = load_rules()

def set_rules(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    if update.effective_chat.get_member(update.effective_user.id).status in ('administrator', 'creator'):
        rules_text = ' '.join(context.args)
        if rules_text:
            GROUP_RULES[chat_id] = rules_text
            save_rules(GROUP_RULES)
            update.message.reply_text("Group rules have been updated.")
        else:
            update.message.reply_text("Please provide the rules text.")
    else:
        update.message.reply_text("You need to be an admin to set group rules.")

def get_rules(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    rules_text = GROUP_RULES.get(chat_id, "No rules have been set for this group.")
    update.message.reply_text(rules_text, parse_mode=ParseMode.HTML)

def main():
    dispatcher.add_handler(CommandHandler("setrules", set_rules, pass_args=True))
    dispatcher.add_handler(CommandHandler("rules", get_rules))

if __name__ == "__main__":
    main()
