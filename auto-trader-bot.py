from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

# ضع توكن البوت هنا مباشرة
TOKEN = "8438135593:AAFYEt4sASDD2L_9vg7GK109G7WZ4DaXKhk"  # غيره بتوكنك الصحيح

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("بوت شغال!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
