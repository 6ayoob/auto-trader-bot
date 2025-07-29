from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from strategies import momentum_strategy, swing_strategy
from config import TELEGRAM_TOKEN, ALLOWED_USER_IDS

strategy_mode = "momentum"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_USER_IDS:
        return
    await update.message.reply_text("🤖 مرحبًا بك في Auto Trader Bot!")

async def trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_USER_IDS:
        return
    # البيانات التجريبية فقط
    data = {'price': 1.0, 'volume_change_15m': 2.0}
    rsi = 25
    ma20, ma50, market_cap = 0.9, 0.95, 15000000
    if strategy_mode == "momentum":
        decision = momentum_strategy(data, rsi)
    else:
        decision = swing_strategy(data, rsi, ma20, ma50, market_cap)

    await update.message.reply_text(f"📈 الاستراتيجية الحالية: {strategy_mode}\n📊 القرار: {decision}")

async def strategy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global strategy_mode
    if update.effective_user.id not in ALLOWED_USER_IDS:
        return
    if context.args:
        if context.args[0] in ["momentum", "swing"]:
            strategy_mode = context.args[0]
            await update.message.reply_text(f"✅ تم تفعيل استراتيجية: {strategy_mode}")
        else:
            await update.message.reply_text("❌ اختر: momentum أو swing")
    else:
        await update.message.reply_text(f"🔍 الاستراتيجية الحالية: {strategy_mode}")

def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("trade", trade))
    app.add_handler(CommandHandler("strategy", strategy))
    app.run_polling()
