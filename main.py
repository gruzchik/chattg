import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

BOT_TOKEN = sys.argv[1]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Start function called")
    await update.message.reply_text("Hello, welcome my bot!")

def run():
    pass
    print("Application started")
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    run()