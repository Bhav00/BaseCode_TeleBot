## importing the essentials
import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot started....")

    ## The very first message that the user can see as soon as the bot starts
def start_command(update,context):
    update.message.reply_text(f"Hey! my name is {keys.NAME}. This is my bot, {keys.BOT_NAME}.\n Feel free to look around and if you dont understand what is going on, use the '/help' command and something to show you the way should pop up.")
    print(context)


    ## Help message that can be triggered by the user accessing the bot through telegram
def help_command(update,context):
    update.message.reply_text("The context to let people better understand what your bot does and how it can be helpful to them goes here.")
    print(context)

    ## Reply Handler
    ## recieves user messages and returns the appropriate replies as mentioned in responses.py
def handle_message(update,context):
    text = str(update.message.text).lower()
    response = R.sample_res(text)
    update.message.reply_text(response)
    print(context)

    ## Error handler
def error(update,context):
    print(f"Update {update} caused error {context.error}")


def main():

    updater = Updater(keys.API_KEY, use_context = True)
    dp = updater.dispatcher

    ## More '/commands' can be created and bound with the functions like done here but
    ## This should be done only for certain important commands

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(1)
    updater.idle()

if __name__ == '__main__':
    main()