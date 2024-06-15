# Madara/modules/admin.py
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def promote(update: Update, context: CallbackContext) -> None:
    if update.effective_chat.get_member(update.effective_user.id).status != 'administrator':
        update.message.reply_text("You need to be an admin to use this command.")
        return

    if not context.args:
        update.message.reply_text("You need to specify a user to promote.")
        return

    user_id = int(context.args[0])
    chat = update.effective_chat

    try:
        chat.promote_member(user_id, can_change_info=True, can_delete_messages=True,
                            can_invite_users=True, can_restrict_members=True,
                            can_pin_messages=True, can_promote_members=True)
        update.message.reply_text("User promoted successfully!")
    except Exception as e:
        update.message.reply_text(f"Failed to promote user: {e}")

def ban(update: Update, context: CallbackContext) -> None:
    if update.effective_chat.get_member(update.effective_user.id).status != 'administrator':
        update.message.reply_text("You need to be an admin to use this command.")
        return

    if not context.args:
        update.message.reply_text("You need to specify a user to ban.")
        return

    user_id = int(context.args[0])
    chat = update.effective_chat

    try:
        chat.kick_member(user_id)
        update.message.reply_text("User banned successfully!")
    except Exception as e:
        update.message.reply_text(f"Failed to ban user: {e}")

def main(dispatcher):
    dispatcher.add_handler(CommandHandler("promote", promote, pass_args=True))
    dispatcher.add_handler(CommandHandler("ban", ban, pass_args=True))

if __name__ == "__main__":
    from Madara import dispatcher  # Ensure this matches your directory structure
    main(dispatcher)
