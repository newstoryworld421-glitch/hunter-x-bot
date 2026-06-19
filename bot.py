from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("8997747937:AAGpQKTtb2tEoBONXr6eW73TFPPqV_RwnSU")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚔️ Hunter X Bot Online!")

app = Application.builder().token(8997747937:AAGpQKTtb2tEoBONXr6eW73TFPPqV_RwnSU).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
