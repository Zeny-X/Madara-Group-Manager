from telegram import Update, ParseMode
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext
from Madara import dispatcher
import json
import os

FAQ_FILE = 'faq.json'

# Load existing FAQs from file
def load_faqs():
    if os.path.exists(FAQ_FILE):
        with open(FAQ_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save FAQs to file
def save_faqs(faqs):
    with open(FAQ_FILE, 'w') as file:
        json.dump(faqs, file, indent=4)

# Dictionary to store FAQs
FAQS = load_faqs()

def add_faq(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 2:
        update.message.reply_text("Usage: /addfaq <question> - <answer>")
        return

    faq_text = ' '.join(context.args)
    if '-' not in faq_text:
        update.message.reply_text("Usage: /addfaq <question> - <answer>")
        return

    question, answer = faq_text.split('-', 1)
    question = question.strip()
    answer = answer.strip()

    FAQS[question] = answer
    save_faqs(FAQS)
    update.message.reply_text(f"FAQ added: {question} -> {answer}")

def remove_faq(update: Update, context: CallbackContext) -> None:
    question = ' '.join(context.args).strip()
    if question in FAQS:
        del FAQS[question]
        save_faqs(FAQS)
        update.message.reply_text(f"FAQ removed: {question}")
    else:
        update.message.reply_text(f"No FAQ found for: {question}")

def list_faqs(update: Update, context: CallbackContext) -> None:
    if FAQS:
        faqs = "\n".join([f"{q} -> {a}" for q, a in FAQS.items()])
        update.message.reply_text(f"FAQs:\n{faqs}", parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text("No FAQs found.")

def handle_faq(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text.strip().lower()
    for question, answer in FAQS.items():
        if question.lower() in message_text:
            update.message.reply_text(answer, parse_mode=ParseMode.HTML)
            return

def main():
    dispatcher.add_handler(CommandHandler("addfaq", add_faq, pass_args=True))
    dispatcher.add_handler(CommandHandler("removefaq", remove_faq, pass_args=True))
    dispatcher.add_handler(CommandHandler("listfaqs", list_faqs))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_faq))

if __name__ == "__main__":
    main()
