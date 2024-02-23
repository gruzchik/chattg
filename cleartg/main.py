import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

BOT_TOKEN = sys.argv[1]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Start interaction with user
    """
    print("Start function called")
    user = update.message.from_user
    print(user["first_name"])
    print(user)
    await update.message.reply_text("Hello, welcome my bot!")

async def getinfo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Update info about user
    """
    user = update.message.from_user
    await update.message.reply_text(str(user["id"])+":"+user["first_name"]+" "+user["last_name"])


def run():
    pass
    print("Application started")
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", start))
    application.add_handler(CommandHandler("get_info", getinfo))
    application.run_polling()
    # /get_info
    # 33453: Name SecondName

if __name__ == "__main__":
    run()
