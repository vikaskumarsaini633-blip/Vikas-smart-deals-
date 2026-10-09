import os
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("8829356253:AAHwnkTRdVcKnDAjTkITm3M6irCZxWYBkp4")
AMAZON_TAG = os.environ.get("vikassmartdea-21")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("नमस्ते! मुझे कोई भी Amazon product link भेजें, मैं उसे आपके Affiliate Link में बदल दूंगा।")

async def convert_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    amazon_urls = re.findall(r'(https?://[^\s]+)', text)
    
    if not amazon_urls:
        return

    for url in amazon_urls:
        if "amazon" in url or "amzn" in url:
            if "?" in url:
                affiliate_url = f"{url}&tag={AMAZON_TAG}"
            else:
                affiliate_url = f"{url}?tag={vikassmartdea-21}"
            
            await update.message.reply_text(f"🛒 **आपका Affiliate Link:**\n{affiliate_url}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(8829356253:AAHwnkTRdVcKnDAjTkITm3M6irCZxWYBkp4).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, convert_link))
    app.run_polling()

