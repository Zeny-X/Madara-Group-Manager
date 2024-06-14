from telegram import Update, ParseMode
from telegram.ext import CommandHandler, CallbackContext
from Madara import dispatcher

GROUP_RULES = {}

def set_rules(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    if update.effective_chat.get_member(update.effective_user.id).status in ('administrator', 'creator'):
        rules_text = ' '.join(context.args)
        if rules_text:
            GROUP_RULES[chat_id] = rules_text
            update.message.reply_text("Group rules have been updated.")
        else:
            update.message.reply_text("Please provide the rules text.")
    else:
        update.message.reply_text("You need to be an admin to set group rules.")

def get_rules(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    rules_text = GROUP_RULES.get(chat_id, "No rules have been set for this group.")
    update.mes
